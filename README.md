# SSH Multitunnel

Creates an ssh tunnel through local port forwarding between multiple stations.
The last station is forwarded through dynamic forwarding.

This allows the usage of tools such as proxychains(-ng) and redsocks to access the internet through the tunnel.

## Usage:
```python
import sys

from ssh_multitunnel import Station, tunnel

with tunnel(
        [
            Station(host='host1', port=22, user='user', password='Password1', bind_port=7777),
            Station(host='host2', port=22, user='root', password='toor', bind_port=8888),
            Station(host='host3', port=2222, user='bla', password='blabla123', bind_port=1234)
        ],
        local_bind_port=9999,
        logfile=sys.stdout
) as p:
    while True:
        pass

```

This will create a tunnel using the following command:
```
ssh -t -L 9999:localhost:7777 user@host1 -p 22 ssh -t -L 7777:localhost:8888 root@host2 -p 22 ssh -D 8888 -N bla@host3 -p 2222 
```
The tunnel can be used with `proxychains wget google.com` (with proxychains configured to proxy through port 9999)