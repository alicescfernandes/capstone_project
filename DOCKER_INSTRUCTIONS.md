## Development

### Start up Dev Environment

### First-Time Run

```sh
docker-compose up --build
```

### Running the dev env

```sh
docker-compose up 
```

### Run commands on the Web service

```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Clear the Dev Enviroment

This also clears the databases since it removes the volumes

```sh
docker-compose down -v
```

## Start up Production Environment

All of the commands above still apply, but the docker-compose file is different

To quickly get the Production environment going:

```sh
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

```

On Debian 12 (Bookworm)

```sh
docker compose -f docker-compose.prod.yml down -v
docker compose -f docker-compose.prod.yml up -d --build
docker compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

```

## Other usefull docker commands

docker container prune
docker volume prune

# docker run --name some-nginx -p 80:80 nginx

docker-compose down -v

docker ps -aq | xargs docker rm -f

docker ps -a
