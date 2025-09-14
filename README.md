# Catalogo\_repuestos

Catálogo e inventario de repuestos automotrices construido con **Django** (patrón **MVT**). Incluye autenticación básica, perfiles de usuario y CRUDs para entidades como **Clase**, **Marca**, **Modelo**, **Parte**, **Elemento** y **Estructura** (relación entre todas).

> Repo: [https://github.com/SebastianFurquet/Catalogo\_repuestos](https://github.com/SebastianFurquet/Catalogo_repuestos)

---

## 🧭 Tabla de contenidos

* [Características](#-características)
* [Tecnologías](#-tecnologías)
* [Modelo de datos](#-modelo-de-datos)
* [Módulos y rutas](#-módulos-y-rutas)
* [Plantillas](#-plantillas)
* [Requisitos](#-requisitos)
* [Instalación y ejecución](#-instalación-y-ejecución)
* [Migraciones y superusuario](#-migraciones-y-superusuario)
* [Estructura del proyecto](#-estructura-del-proyecto)
* [Comandos rápidos](#-comandos-rápidos)
* [Licencia](#-licencia)

---

## ✨ Características

Esta web simula la logica de un catalogo de repuestos Automotriz

* ✅ **CRUD de inventario** (Clase, Marca, Modelo, Parte, Elemento, Estructura).
* ✅ **Búsqueda** por texto en listados (método `GET`).
* ✅ **Autenticación**: login, logout, cambio de contraseña, perfil y edición de perfil.
* ✅ **Herencia de plantillas** (`base.html` con bloques `title`, `content` y `content_title`).
* ✅ **Bootstrap 5** para maquetado rápido.
* ✅ (Opcional) **Carga y previsualización de imágenes** para entidades (p.ej., Marca/Modelo) si el proyecto está configurado con `MEDIA_*`.


---

## 🛠 Tecnologías

* **Python** 3.10+
* **Django** 4.x / 5.x
* **SQLite** (dev) 
* **Bootstrap** 5 (CDN)

---

## 🧱 Modelo de datos

Entidades principales de la app `inventario` (nombres orientativos):

* `Clase`
* `Marca`
* `Modelo` (campos típicos: `cod_modelo`, `clase` → Clase, `marca` → Marca, `descripcion`, `cod_veh`)
* `Parte`
* `Elemento`
* `Estructura` (referencia a Clase/Marca/Modelo/Parte/Elemento + `nro_pieza`, `precio`, etc.)


## 🔗 Módulos y rutas

### App `inventario`

* **Listados** (ej.): `clase_list`, `marca_list`, `modelo_list`, `estructura_list`.
* **ABM** (ej.): `*_create`, `*_update`, `*_delete`.
* **Búsqueda** en listados mediante `?busqueda=` o `?q=` (según vista).

### App `usuarios`

* **Autenticación**: `login`, `logout`.
* **Perfil**: `perfil`, `editar_perfil`, `editar_contrasenia`.

> Los nombres exactos pueden variar por rama; consulta `inventario/urls.py` y `usuarios/urls.py`.

Rutas de ejemplo:

```py
# inventario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('clases/', views.clase_list, name='clase_list'),
    path('clases/nueva/', views.clase_create, name='clase_create'),
    path('clases/<int:pk>/editar/', views.clase_update, name='clase_update'),
    path('clases/<int:pk>/eliminar/', views.clase_delete, name='clase_delete'),

    path('modelos/', views.ModeloListView.as_view(), name='modelo_list'),
    path('estructuras/', views.estructura_list, name='estructura_list'),
]
```

---

## 🧩 Plantillas

* `templates/inventario/base.html` — layout general + navbar/footer.
* `templates/inventario/*_list.html` — listados con formulario de búsqueda y tabla.
* `templates/inventario/*_form.html` — formularios de alta/edición.
* `templates/usuarios/*` — páginas de login, perfil y edición de contraseña.

Fragmento típico (lista con búsqueda + tabla):

```django
<form method="get" class="d-flex gap-2">
  <input name="busqueda" class="form-control" placeholder="Buscar" />
  <button class="btn btn-primary">Buscar</button>
</form>

<table class="table table-light table-striped mt-3">
  <thead>
    <tr>
      <th>Marca</th><th>Modelo</th><th>Parte</th><th>Elemento</th><th>N° pieza</th><th>Precio</th>
    </tr>
  </thead>
  <tbody>
    {% for e in objetos %}
      <tr>
        <td>{{ e.modelo.marca }}</td>
        <td>{{ e.modelo.descripcion }}</td>
        <td>{{ e.parte }}</td>
        <td>{{ e.elemento }}</td>
        <td>{{ e.nro_pieza|default:"-" }}</td>
        <td>{{ e.precio|default:"-" }}</td>
      </tr>
    {% empty %}
      <tr><td colspan="6" class="text-center">Sin resultados</td></tr>
    {% endfor %}
  </tbody>
</table>
```

---

## 📦 Requisitos

* Python 3.10+
* pip
* (Opcional) virtualenv
* Git

---

## 🚀 Instalación y ejecución

Cloná el repo y levantá el entorno.

**Windows (PowerShell):**

```ps1
# 1) Clonar
git clone https://github.com/SebastianFurquet/Catalogo_repuestos.git
cd Catalogo_repuestos

# 2) Entorno virtual
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1   # en CMD: .\\.venv\\Scripts\\activate.bat

# 3) Dependencias
pip install -r requirements.txt  # si existe
# o bien (mínimo)
pip install django

# 4) Migraciones
python manage.py migrate

# 5) Superusuario (opcional)
python manage.py createsuperuser

# 6) Ejecutar
python manage.py runserver
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt || pip install django
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

Abrí: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

---

## 🗃 Migraciones y superusuario

```bash
python manage.py makemigrations inventario usuarios
python manage.py migrate
python manage.py createsuperuser
```

Admin: `/admin/`

---

## 🗂 Estructura simplificada del proyecto

```text
Catalogo_repuestos/
├─ Catalogo_repuestos/         # settings/urls/wsgi/asgi
├─ inventario/                 # app de catálogo
│  ├─ admin.py / models.py / views.py / urls.py / forms.py
│  └─ templates/inventario/
│     ├─ base.html
│     ├─ navbar.html
│     ├─ *_list.html
│     └─ *_form.html
├─ usuarios/                   # app de usuarios (auth + perfil)
│  ├─ views.py / urls.py / forms.py
│  └─ templates/usuarios/
│     ├─ login.html
│     ├─ perfil.html
│     └─ editar_contrasenia.html
├─ manage.py
├─ requirements.txt 
└─ README.md
```

---

## ⚡ Comandos rápidos

```bash
# Ejecutar servidor
python manage.py runserver

# Crear app
python manage.py startapp <nombre_app>

# Shell de Django
python manage.py shell

# Exportar dependencias (si usas venv)
pip freeze > requirements.txt
```


## 🧑‍💻 Autor

**Sebastian Furquet** — *Inspecciones & Cotizaciones / Catálogo de Repuestos*
