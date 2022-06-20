# Proyecto2020

<p align="center">
  <img src="/home/franco/Documentos/django/Proyecto/Proyecto2020/Proyecto/static/logo1.png" width="150">
  <br />
  <br />
  
  
Nuestro Mercado De Jugadores es una pagina que busca dar la oportunidad a los jóvenes promesas del mundo a mejorar sus equipos mediante un eficiente sistema de fichajes y un sincero y eficaz programa 

# Requirements
| Paquete           | Version |
|-------------------|---------|
| beautifulsoup4    | 4.9.3   |
| click             | 7.1.2   |
| Django            | 2.2     |
| django-bootstrap4 | 2.3.1   |
| django-jet        | 1.0.8   |
| Pillow            | 8.0.1   |
| pytz              | 2020.4  |
| soupsieve         | 2.0.1   |
| sqlparse          | 0.4.1   |
| svgwrite          | 1.4     |
| Tree              | 0.2.4   |

* **para instalar requirements.txt** en el entorno virtual:
```bash
pip install -r requirements.txt
```

# Python
| 3.8.5 | Version |
|-------|---------|


#### Instalacion
```
git clone https://github.com/francogarcia02/Proyecto2020

mkvirtualenv tuvirtualenv

pip install -r requirements.txt

cd ~/.Proyecto
./manage.py makemigrations
./manage.py migrate
```

#### Creacion de superusuario

```
./manage.py createsuperuser
```

#### Ejecucion
```
./manage.py runserver
```