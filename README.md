Ejercicio de la clase Arquitectura de Computadoras
Creaccion de un aplicacion mediante Python Django para medir el rendimiento de su computador.

Integrantes:
Roberto Rafael Oyuela Midence 202420110313
Jorge Luis Diaz Espinal 202310110124
Angel Jafet Contreras Carranza 20220060275

# 🖥 Monitor del Sistema (Proyecto Django)

Este es un proyecto simple desarrollado en Django que muestra en tiempo real el uso de CPU, memoria RAM, disco y detalles del sistema operativo, utilizando la biblioteca `psutil`. La interfaz web se actualiza automáticamente cada 10 segundos y permite ver estadísticas básicas del estado del sistema.

---

## Descripción del Proyecto

El sistema cuenta con:

- Un panel web (`home`) donde se muestra:
  - Uso actual de CPU.
  - Memoria RAM total, usada y porcentaje de uso.
  - Información del disco (usado, libre, total).
  - Información del sistema (SO, versión, núcleos).
- Autoactualización de datos cada 10 segundos.
- Un botón para recargar manualmente.

---

Instrucciones para Ejecutar Localmente

##1. Clona el repositorio

git clone https://github.com/robertooyuela97/monitor_project_exam
cd monitor

2- Crea un entorno virtual
python -m venv env
env\Scripts\activate         # En Windows

3. Instala las dependencias
bash

pip install django psutil

4. Realiza las migraciones
bash

python manage.py migrate

5. Ejecuta el servidor de desarrollo
bash
python manage.py runserver
