# DevOpsFestDemo
demo for DevOpsFest2020

## Install WireGuard *

`https://www.wireguard.com/install/`

### generate keys for WireGuard. One per node

`wg genkey | tee <filename>.key |  wg pubkey > <filename>-public.key`

### install

for ubuntu 20.04
`sudo apt update && sudo apt install wireguard -y`

### setup WireGuard on server and clients

`sudo nano /etc/wireguard/<interface name>.conf`

```
sudo nano /etc/wireguard/wg0.conf
```

server config
```
[Interface]
Address = 10.11.12.1/32
ListenPort = 51820
PrivateKey = KBy4hSOGvnyyqhEUF2K4BziSyhV1S6IB9oSzc3iqfGk=
[Peer]
# WSL
PublicKey = 9L+y5+ONLBE1qfiPq3c/TFFUOwDRDvp98QUmraDPHA8=
AllowedIPs = 10.11.12.10/32
[Peer]
# wsl2
PublicKey = CCbaaxkOOLu1AuTORThd8oYgz7xKxUBf2H7zOVC/Yj8=
AllowedIPs = 10.11.12.20/32
[Peer]
# win
PublicKey = 6aHBFU9Y1BLkW/sSZHUncCGnuhRjakdKuAZZc6kHDmY=
AllowedIPs = 10.11.12.30/32
[Peer]
# vagrant
PublicKey = ulNypyxr4KCVJ4sqvNNnLshTZ5uEF9oGalwV932Qaws=
AllowedIPs = 10.11.12.40/32
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

if as result you have this last line

`/etc/resolvconf/update.d/libc: Warning: /etc/resolv.conf is not a symbolic link to /run/resolvconf/resolv.conf`

than do

`sudo dpkg-reconfigure resolvconf`

and you can add this as a service

`sudo systemctl enable wg-quick@wg0.service`


### *

#### install WG for WSL2

https://medium.com/@centerorbit/installing-wireguard-in-wsl-2-dd676520cb21 

if not exists `sudo mkdir /etc/wireguard`

## Install k3s 

### install k3sup **

https://github.com/alexellis/k3sup

### k3s master 

`k3sup install --ip <internal IP> --ssh-key <path to the ssh key file> --user <user for ssh> --k3s-extra-args '--flannel-iface wg0'`
```
k3sup install --ip 10.11.12.1 --ssh-key /home/pss/DevOps1/VIF/k3s1.pem --user ubuntu --k3s-extra-args '--flannel-iface wg0'
```

### k3s node

`k3sup join --user <user for ssh> --server-ip <internal master IP> --ip <internal node IP> --ssh-key <path to the ssh key file> --k3s-extra-args '--flannel-iface wg0 --node-label dde.role=DevVM --node-name <custom node name> --with-node-id'`

```
k3sup join --user ubuntu --server-ip 10.11.12.1 --ip 10.11.12.X0 --ssh-key ~/DevOps1/VIF/k3s1.pem --k3s-extra-args '--flannel-iface wg0  --node-name  devnode --with-node-id'
```

or withot k3sup

```
curl -sfL https://get.k3s.io/ | K3S_URL='https://10.11.12.1:6443' K3S_TOKEN='<token>' INSTALL_K3S_VERSION='v1.17.2+k3s1' sh -s - --flannel-iface wg0 --node-label dde.role=DevVM --node-name devnode --with-node-id

where token = `sudo cat /var/lib/rancher/k3s/server/node-token` on master node
```


### **

#### something go wrong and we need to remove k3s

`/usr/local/bin/k3s-agent-uninstall.sh`

`/usr/local/bin/k3s-uninstall.sh`
