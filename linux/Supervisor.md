Install
---

```
apt-get install supervisor
service supervisor restart
```

Web Panel

В `/etc/supervisor/supervisord.conf`

```
[inet_http_server]
port=0.0.0.0:9001
username=neafiol
password=admin4
```

Setting
---
Create file on `/etc/supervisor/conf.d`

```
[program:itmo_fizra]
command=python3 tgadmin.py
directory=/home/fl/itmo_fizra
environment=SERVER=SW
autostart=true
autorestart=true
stderr_logfile=/var/log/itmo_fizra-mon.err.log
stdout_logfile=/var/log/itmo_fizra-mon.out.log
```