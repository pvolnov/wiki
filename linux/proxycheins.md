## Installing
```
sudo systemctl start tor 
sudo systemctl enable tor

sudo apt-get install git gcc
sudo apt-get remove proxychains
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng/
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
```

## Setting

1. `nano  /etc/proxychains.conf`
2. Add in end
```
socks4  127.0.0.1 9050
socks5 95.217.213.249   1080    neafiol   nef441
```