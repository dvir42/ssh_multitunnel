import pexpect
from contextlib import contextmanager

from .station import Station


def local_bind(port, host, hostport): return f'-t -L {port}:{host}:{hostport}'


def dynamic_bind(port): return f'-D {port} -N'


def ssh_command(host, port, user, params): return f'ssh {params} {user}@{host} -p {port}'


def build_command(stations: [Station], local_bind_port):
    command = ''
    bind_port = local_bind_port
    for i, station in enumerate(stations):
        if i < len(stations) - 1:
            command += ssh_command(station.host, station.port, station.user,
                                   local_bind(bind_port, 'localhost', station.bind_port))
        else:
            command += ssh_command(station.host, station.port, station.user, dynamic_bind(bind_port))
        command += ' '
        bind_port = station.bind_port
    return command


@contextmanager
def tunnel(stations: [Station], local_bind_port, logfile=None):
    command = build_command(stations, local_bind_port)
    tunnel_process = pexpect.spawn(command, logfile=logfile, timeout=None, encoding='utf-8')
    for station in stations:
        prompt = tunnel_process.expect(['Password:', 'password:', r'yes/no', pexpect.EOF])
        if prompt == 2:
            tunnel_process.sendline('yes')
            tunnel_process.expect(['Password:', 'password:'])
            tunnel_process.sendline(station.password)
        elif prompt == 0 or prompt == 1:
            tunnel_process.sendline(station.password)
    yield tunnel_process
    tunnel_process.close()
