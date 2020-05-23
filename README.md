# DevOpsFestDemo
demo for DevOpsFest2020

## Install WireGuard *

`https://www.wireguard.com/install/`


### generate keys for WireGuard. One per node

`wg genkey | tee <filename>.key |  wg pubkey > <filename>-public.key`


### setup WireGuard on server and clients

if not exists `sudo mkdir /etc/wireguard`

`sudo nano /etc/wireguard/<interface name>.conf` we wil use wg0

server config
```
[Interface]
# server IP
Address = 10.11.12.1/32
ListenPort = 51820
PrivateKey = 
[Peer]
PublicKey = 
AllowedIPs = 10.11.12.10/32
[Peer]
PublicKey = 
AllowedIPs = 10.11.12.20/32
[Peer]
PublicKey = 
AllowedIPs = 10.11.12.30/32
```

client config
```
[Interface]
Address = 10.11.12.10/32
PrivateKey = 
[Peer]
# server
PublicKey = 
AllowedIPs = 10.11.12.0/24
Endpoint = <external server IP>:51820
```
### startup WireGuard once per node

`sudo wg-quick up wg0`

`sudo systemctl enable wg-quick@wg0.service`

## k3s 

### install k3sup *

https://github.com/alexellis/k3sup

### k3s master 

`k3sup install --ip <internal IP> --ssh-key <path to the ssh key file> --user <user for ssh> --k3s-extra-args '--flannel-iface wg0'`
```
`k3sup install --ip 10.11.12.1 --ssh-key /home/pss/DevOps1/VIF/k3s1.pem --user ubuntu --k3s-extra-args '--flannel-iface wg0'`
```

### k3s node


`k3sup join --user ubuntu --server-ip 10.11.12.1 --ip 10.11.12.30 --ssh-key ~/DevOps1/VIF/k3s1.pem --k3s-extra-args '--flannel-iface wg0  --node-name <custom node name> --with-node-id'`

```
k3sup join --user <user for ssh> --server-ip <internal master IP> --ip <internal node IP> --ssh-key <path to the ssh key file> --k3s-extra-args '--flannel-iface wg0 --node-label dde.role=DevVM --node-name devnode --with-node-id'
```

or withot k3sup

```
curl -sfL https://get.k3s.io/ | K3S_URL='https://10.11.12.1:6443' K3S_TOKEN='<token>' INSTALL_K3S_VERSION='v1.17.2+k3s1' sh -s - --flannel-iface wg0 --node-label dde.role=DevVM --node-name devnode --with-node-id

where token = sudo cat /var/lib/rancher/k3s/server/node-token on master node
```


### *

#### install WG for WSL2

https://medium.com/@centerorbit/installing-wireguard-in-wsl-2-dd676520cb21 

#### something go wrong and we need to remove k3s

`/usr/local/bin/k3s-agent-uninstall.sh`

`/usr/local/bin/k3s-uninstall.sh`