from dataclasses import dataclass


@dataclass
class Station:
    host: str = 'localhost'
    port: int = 22
    user: str = 'root'
    password: str = ''
    bind_port: int = 9999
