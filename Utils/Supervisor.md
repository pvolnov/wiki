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
[program:elfin]
command=python3 app.py
directory=/home/elfin
environment=SERVER=SW
autostart=true
autorestart=true
stderr_logfile=/var/log/elfin.err.log
stdout_logfile=/var/log/elfin.out.log
```