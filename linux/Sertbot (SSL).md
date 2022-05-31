(origin)[https://certbot.eff.org/]

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt update
sudo apt install certbot

sudo certbot certonly --standalone -d api.cryptohere.app
```

Далее
```python
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_verify_locations(cafile="/etc/letsencrypt/live/sw.neafiol.site/fullchain.pem")
    context.load_cert_chain("/etc/letsencrypt/live/sw.neafiol.site/cert.pem",
                            keyfile="/etc/letsencrypt/live/sw.neafiol.site/privkey.pem")
```

sudo certbot certonly --standalone -d api.oops.finance
