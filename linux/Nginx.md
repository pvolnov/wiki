
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
        server_name         rpc.testnet.cryptohere.app;

        ssl_certificate      /etc/letsencrypt/live/rpc.testnet.cryptohere.app/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/rpc.testnet.cryptohere.app/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;


        location / {
                proxy_pass http://127.0.0.1:3031;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_http_version 1.1;
                proxy_redirect off;
                proxy_buffering off;

                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "Upgrade";
                proxy_set_header Host $host;
        }
}

server {
        listen 443 ssl;
        server_name         zmq.testnet.cryptohere.app;

        ssl_certificate      /etc/letsencrypt/live/zmq.testnet.cryptohere.app/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/zmq.testnet.cryptohere.app/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;


        location / {
                proxy_pass http://127.0.0.1:9556;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_http_version 1.1;
                proxy_redirect off;
                proxy_buffering off;

                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "Upgrade";
                proxy_set_header Host $host;
        }
}

server {
        listen 443 ssl;
        server_name         api.testnet.cryptohere.app;

        ssl_certificate      /etc/letsencrypt/live/api.testnet.cryptohere.app/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/api.testnet.cryptohere.app/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;


        location / {
                proxy_pass http://127.0.0.1:4002;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_http_version 1.1;
                proxy_redirect off;
                proxy_buffering off;

                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "Upgrade";
                proxy_set_header Host $host;
        }
}

server {
        listen 443 ssl;
        server_name         rpc.cryptohere.app;

        ssl_certificate      /etc/letsencrypt/live/rpc.cryptohere.app/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/rpc.cryptohere.app/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;


        location / {
                proxy_pass http://127.0.0.1:3030;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_http_version 1.1;
                proxy_redirect off;
                proxy_buffering off;
        }
}


server {
        listen 443 ssl;
        server_name         zmq.cryptohere.app;

        ssl_certificate      /etc/letsencrypt/live/zmq.cryptohere.app/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/zmq.cryptohere.app/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;


        location / {
                proxy_pass http://127.0.0.1:9555;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_http_version 1.1;
                proxy_redirect off;
                proxy_buffering off;
        }
}


server {
        listen 443 ssl;
        server_name         testnet.api.cryptohere.app;

        ssl_certificate      /etc/letsencrypt/live/testnet.api.cryptohere.app/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/testnet.api.cryptohere.app/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;


        location / {
                proxy_pass http://127.0.0.1:4002;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_http_version 1.1;
                proxy_redirect off;
                proxy_buffering off;

                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "Upgrade";
                proxy_set_header Host $host;
        }
}

server {
        listen 443 ssl;

        server_name 100x100.space;

        ssl_certificate      /etc/letsencrypt/live/100x100.space/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/100x100.space/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;

        index index.html;

        root /root/wannaspin/web-application/dist;

        autoindex on;
        autoindex_exact_size on;
}



server {
        listen 443 ssl;

        server_name dev.oops.finance;

        ssl_certificate      /etc/letsencrypt/live/dev.oops.finance/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/dev.oops.finance/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
	ssl_prefer_server_ciphers on;

        location / {
                 proxy_pass http://127.0.0.1:9191;
                 proxy_set_header Host $server_name;
                 proxy_set_header X-Real-IP $remote_addr;
                 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}

server {
        listen 443 ssl;

        server_name testnet.api.wannaspin.xyz;

        ssl_certificate      /etc/letsencrypt/live/testnet.api.wannaspin.xyz/fullchain.pem;
    	ssl_certificate_key  /etc/letsencrypt/live/testnet.api.wannaspin.xyz/privkey.pem;
  
  	# Improve HTTPS performance with session resumption
  	ssl_session_cache shared:SSL:10m;
  	ssl_session_timeout 10m;

	# Enable server-side protection against BEAST attacks
  	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
	ssl_prefer_server_ciphers on;

        location / {
                 proxy_pass http://127.0.0.1:10002;
                 proxy_set_header Host $server_name;
                 proxy_set_header X-Real-IP $remote_addr;
                 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```