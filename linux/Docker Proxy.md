```
docker run -d --name socks5 -p 1080:1080 -e PROXY_USER=<PROXY_USER> -e PROXY_PASSWORD=<PROXY_PASSWORD> serjs/go-socks5-proxy
```

docker run -d --name socks5 -p 1080:1080 -e PROXY_USER=neafiol -e PROXY_PASSWORD=nef441 serjs/go-socks5-proxy