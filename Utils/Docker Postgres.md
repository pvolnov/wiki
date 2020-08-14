```
mkdir -p $HOME/docker/volumes/postgres

docker pull postgres

docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=nef441 -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres

docker exec -it pg-docker psql


```

[Ссылка](https://medium.com/faun/postgresql-in-docker-mount-volume-3220fbd0afc4)
