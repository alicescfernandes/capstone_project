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

## Start up Production Environment (TBD)

docker-compose -f docker-compose.prod.yml up -d --build

docker-compose -f docker-compose.prod.yml down -v

-d --> detached mode

cd backend && node build.js

docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

## Other usefull docker commands

docker container prune
docker volume prune

# docker run --name some-nginx -p 80:80 nginx

docker-compose down -v

docker ps -aq | xargs docker rm -f

docker ps -a
