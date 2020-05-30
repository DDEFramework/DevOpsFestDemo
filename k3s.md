## k3s 

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