# Expense Tracker

Expense Tracker es una aplicación web desarrollada en Django para gestionar departamentos, empleados y sus gastos asociados. Permite registrar y visualizar los gastos filtrados por rango de fechas, ofreciendo un resumen de gastos agrupados por departamento.

## Características

- **Gestión de Departamentos:** Crear, editar y eliminar departamentos.
- **Gestión de Empleados:** Vincula empleados con departamentos y realiza operaciones CRUD completas.
- **Gestión de Gastos:** Asocia cada gasto a un empleado y departamento, y permite visualizar los gastos con filtros de fechas.
- **Resumen por Departamento:** Muestra el total de gastos agrupados por departamento en un rango de fechas seleccionado.

---

## Tecnologías y Dependencias

El proyecto utiliza las siguientes tecnologías:

- **Backend:** Django 5.1.1  
- **Servidor de producción:** Gunicorn 23.0.0  
- **Base de datos:** SQLite3 (por defecto en Django)  
- **Despliegue:** Railway (usando `Procfile` y `requirements.txt`)

---

## Instrucciones para Despliegue

### Clonar el repositorio

Clona este repositorio para usarlo localmente o desplegarlo en un servidor:

```bash
git clone https://github.com/andresguaman0621/minicore_gastos.git
cd minicore_gastos
```

### Configurar el entorno

1. **Crea un entorno virtual:**
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las migraciones:**
   ```bash
   python manage.py migrate
   ```

4. **Ejecuta el servidor local:**
   ```bash
   python manage.py runserver
   ```

Visita `http://127.0.0.1:8000` en tu navegador para acceder a la aplicación.

### Despliegue en Railway

Para desplegar en Railway, sigue los pasos:

1. **Sube el código al repositorio en GitHub.**
2. **Conecta tu repositorio a Railway.**
3. **Configura las variables de entorno si es necesario.**
4. **Railway detectará automáticamente el archivo `Procfile` y `requirements.txt` para el despliegue.

---

## Uso de la Aplicación

1. Accede al formulario principal para filtrar gastos por rango de fechas.
2. Visualiza el resumen de gastos por departamento.
3. Utiliza las secciones de CRUD para administrar departamentos, empleados y gastos desde la barra de navegación.

---

## Estructura del Proyecto

La estructura principal del proyecto es la siguiente:

```plaintext
expense_tracker/
├── expense_tracker/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── expenses/
│   ├── templates/
│   │   ├── index.html  # Página principal
│   │   ├── departamento_*.html  # CRUD de departamentos
│   │   ├── empleado_*.html  # CRUD de empleados
│   │   ├── gasto_*.html  # CRUD de gastos
│   ├── forms.py  # Formularios de Django
│   ├── models.py  # Modelos: Departamento, Empleado y Gasto
│   ├── views.py  # Vistas para CRUD y filtrado de datos
│   ├── urls.py   # Rutas de la aplicación
├── staticfiles/  # Archivos estáticos (CSS, JS, imágenes)
├── db.sqlite3  # Base de datos SQLite3
├── manage.py
├── Procfile  # Archivo para ejecución en producción
├── requirements.txt  # Dependencias del proyecto
```

---

## Enlace al Proyecto

Repositorio en GitHub: [Expense Tracker](https://github.com/andresguaman0621/minicore_gastos.git)

---

## Licencia

Este proyecto está bajo la licencia especificada en el archivo `LICENSE`.

---
