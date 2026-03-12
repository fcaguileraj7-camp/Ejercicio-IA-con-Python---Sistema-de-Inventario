# Enlace intrucciones al modelo IA.
https://chatgpt.com/share/69b2c371-cbe0-800b-af5e-9b675be16714

# Sistema de Gestión de Inventario (Python + Tkinter + SQLite)

Aplicación de escritorio desarrollada en Python que permite gestionar productos de inventario mediante una interfaz gráfica construida con Tkinter y almacenamiento persistente usando SQLite.

El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre productos, además de generar alertas automáticas cuando el stock se encuentra por debajo del mínimo definido.

Está diseñado para ejecutarse en Windows y puede ejecutarse fácilmente desde Visual Studio Code.

## Características

Interfaz gráfica clara y fácil de usar

Gestión completa de inventario (CRUD)

Base de datos local SQLite

Formato de precios en Pesos Colombianos (COP)

Visualización de productos en tabla

Alertas de stock mínimo

Aplicación ligera sin dependencias externas

## Tecnologías utilizadas

Python 3

Tkinter (interfaz gráfica)

SQLite3 (base de datos local)

Visual Studio Code (entorno recomendado)

## Estructura del proyecto
inventario-app
│
├── inventario_app.py
├── inventario.db
└── README.md
## Archivos

### inventario_app.py

Archivo principal que contiene:

Interfaz gráfica

Conexión con base de datos

Funciones CRUD

Sistema de alertas

### inventario.db

Base de datos SQLite creada automáticamente al ejecutar el programa.

## Requisitos

Antes de ejecutar la aplicación asegúrese de tener instalado:

Python 3.8 o superior

Para verificar:

python --version

Tkinter y SQLite ya vienen incluidos con Python en Windows.

## Instalación

Clonar el repositorio

git clone https://github.com/tu-usuario/inventario-app.git

Entrar al proyecto

cd inventario-app

Abrir el proyecto en Visual Studio Code

Ejecutar el programa

python inventario_app.py

Al ejecutarse por primera vez se creará automáticamente el archivo:

inventario.db

## Uso de la aplicación

Al iniciar la aplicación se abrirá la ventana principal del sistema de inventario.

La interfaz contiene:

Campos para registrar productos

Botones para gestionar el inventario

Tabla de visualización de productos

## Campos del producto

Cada producto contiene la siguiente información:

Nombre

Nombre del producto.

Precio

Precio del producto en pesos colombianos (COP).

Cantidad

Número de unidades disponibles en inventario.

Stock mínimo

Cantidad mínima permitida antes de generar una alerta.

# Funciones del sistema
## Agregar producto

Ingresar la información en los campos:

Nombre

Precio

Cantidad

Stock mínimo

Presionar el botón:

Agregar

El producto será almacenado en la base de datos y aparecerá en la tabla.

## Mostrar productos

Presionar el botón:

Mostrar todo

Se cargará la lista completa de productos registrados.

## Seleccionar producto

Para editar o eliminar un producto:

Hacer clic sobre el producto en la tabla.

Los datos se cargarán automáticamente en el formulario.

## Actualizar producto

Seleccionar un producto en la tabla.

Modificar los campos deseados.

Presionar el botón:

Actualizar

Los cambios se guardarán en la base de datos.

## Eliminar producto

Seleccionar un producto en la tabla.

Presionar el botón:

Eliminar

El sistema pedirá confirmación antes de borrar el registro.

## Alerta de stock

El botón:

Alerta stock

Muestra únicamente los productos cuya cantidad actual es menor que el stock mínimo.

Consulta utilizada:

cantidad < stock_minimo

Esto permite identificar productos que necesitan reposición.

## Base de datos

La aplicación utiliza SQLite, una base de datos ligera almacenada en un archivo local.

Tabla utilizada:

productos

Campos:

Campo	Tipo
id	INTEGER
nombre	TEXT
precio	REAL
cantidad	INTEGER
stock_minimo	INTEGER

## Posibles mejoras futuras

Búsqueda de productos

Exportación a Excel

Dashboard de inventario

Control de usuarios

Interfaz moderna con CustomTkinter

Empaquetado como aplicación ejecutable (.exe)


