sudo apt install postgresql-server-dev-all
sudo apt-get install build-essential libssl-dev libffi-dev python-dev libpq-dev
sudo apt install postgresql

psycopg2

`sudo -u postgres psql`
`\password postgres`

Данные: `/var/lib/postgresql/10/main`

Drop
----

```
sudo apt-get --purge remove postgresql\*
sudo apt autoremove

```