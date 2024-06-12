# PortafolioCursoOnlineDjango

## Descripción del Proyecto

PortafolioCursoOnlineDjango es un proyecto educativo desarrollado como parte de un curso de Django proporcionado por SENCE. Este proyecto tiene como objetivo enseñar los conceptos básicos y avanzados de Django a través de la creación de un portafolio web. 

## Características

- Creación y configuración de un proyecto Django.
- Desarrollo de una aplicación básica llamada "homeapp".
- Configuración de vistas y URLs.
- Integración de la aplicación en el proyecto principal.

## Colaboradores

- **Álvaro**
- **Aquiles**
- **Bastián**
- **Sbecerra**
- **Rafael**

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/PortafolioCursoOnlineDjango.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd PortafolioCursoOnlineDjango
   ```

3. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

4. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

5. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

6. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

7. Abre tu navegador y visita [http://127.0.0.1:8000](http://127.0.0.1:8000) para ver la aplicación en funcionamiento.

## Estructura del Proyecto

```
PortafolioCursoOnlineDjango/
│
├── homeapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── portafolio/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

## Agradecimientos

Este proyecto fue desarrollado bajo la guía del curso de Django ofrecido por SENCE. Agradecemos a los instructores y a todos los colaboradores por su dedicación y esfuerzo en la realización de este proyecto educativo.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

¡Gracias por visitar nuestro proyecto! No dudes en colaborar o hacer preguntas si tienes alguna duda.
