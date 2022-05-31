docker run -d -p 8181:5000 --name registry registry:2


docker image tag ubuntu cb.neafiol.site:8181/myfirstimage

docker push cb.neafiol.site:8181/myfirstimage

docker pull cb.neafiol.site:8181/myfirstimage


docker run \
  --entrypoint htpasswd \
  httpd:2 -Bbn testuser testpassword > auth/htpasswd

docker container stop registry

docker run -d \
  -p 8181:5000 \
  --restart=always \
  --name registry \
  -v "$(pwd)"/auth:/auth \
  -e "REGISTRY_AUTH=htpasswd" \
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  registry:2