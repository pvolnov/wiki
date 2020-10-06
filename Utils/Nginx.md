
Installing
---
`sudo apt install nginx`

* /etc/nginx/nginx.conf - главный файл конфигурации
* /etc/nginx/sites-available/* - файлы конфигурации для виртуальных хостов, проще говоря для каждого сайта.
* /etc/nginx/sites-enabled/* - файлы конфигурации активированных сайтов.

`nginx -s reload`


Sanic exemple
---
`gunicorn app:app --bind 0.0.0.0:8082 --worker-class sanic.worker.GunicornWorker`


staticfile in `/etc/nginx/sites-available/default`

nginx default:

```conf
server {
         listen 443 ssl;
         server_name         sw.neafiol.site;
         ssl_certificate     /etc/letsencrypt/live/sw.neafiol.site/cert.pem;
         ssl_certificate_key /etc/letsencrypt/live/sw.neafiol.site/privkey.pem;
         ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
         ssl_ciphers         HIGH:!aNULL:!MD5;

        location ~ \.(gif|jpg|png)$  {
                root /data/images;
        }

        location / {
                 proxy_pass http://127.0.0.1:8082;
                 proxy_set_header Host $server_name;
                 proxy_set_header X-Real-IP $remote_addr;
                 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

}
```