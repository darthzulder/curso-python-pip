# Game Project

Para correr las aplicaciones debes seguir las siguientes instrucciones en terminal
Para la version en Docker se debe tener instalado docker.


#Juego de piedra papel o tijeras
```sh
git clone
cd game
python3 main.py
```

#Aplicacion de datos de paises
```sh
git clone
cd app
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
En docker

```
git clone
cd app
docker-compose build
docker-compose up -d
docker-compose exec app bash
```
#Aplicacion de graficos
```sh
git clone
cd charts
python3 main.py
```
#Aplicacion de servidor-web
```sh
git clone
cd web-server
source env/bin/activate
uvicorn main:app
```
En docker
```sh
git clone
cd web-server
docker-compose build
docker-compose up -d
```
