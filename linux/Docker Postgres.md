```
mkdir -p $HOME/docker/volumes/postgres

docker pull postgres

docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=nef441-d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres -N 500

docker run  --name pg-docker -e POSTGRES_PASSWORD=tgbotdb -d -p 5433:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres:13 -N 500

docker run  --name pg-docker -e POSTGRES_PASSWORD=test -e POSTGRES_USER=test -e POSTGRES_DB=test -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres:13 -N 500

docker run --name postgres -e POSTGRES_PASSWORD=postgres -e  POSTGRES_USER=postgres -e POSTGRES_DB=postgres -d -p 5432:5432 postgres


docker exec -it -u postgres pg-docker psql

`show max_connections;`


pg_dump -h localhost -U postgres -W  yamarket >  export.dmp

```

[Ссылка](https://medium.com/faun/postgresql-in-docker-mount-volume-3220fbd0afc4)


