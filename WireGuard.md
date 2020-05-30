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

`sudo systemctl enable wg-quick@wg0.service`


### *

#### install WG for WSL2

https://medium.com/@centerorbit/installing-wireguard-in-wsl-2-dd676520cb21 

if not exists `sudo mkdir /etc/wireguard`
