# Usa una imagen base de Python
FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copia el archivo requirements.txt y los archivos de tu proyecto a la imagen
COPY requeriments.txt .


# Instala las dependencias de tu proyecto
RUN pip install -r requeriments.txt

## Conecta a la base de datos 
#ENV POSTGRES_USER <tienda>
#ENV POSTGRES_PASSWORD <password>
#ENV POSTGRES_DB <tienda>

# Expone el puerto que utiliza tu aplicación (por ejemplo, el puerto 8000 para Django)

# Ejecuta el comando de inicio de tu aplicación (ajusta según tus necesidades)


COPY . .

