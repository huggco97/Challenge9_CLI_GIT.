# CLI de Consulta Climática

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python que permite consultar datos climáticos para una ubicación específica utilizando una API de clima. La aplicación ofrece varias opciones de salida, incluyendo JSON, CSV, y un informe en texto plano.

## Características Principales

- **Consulta de Clima por Ubicación:** La aplicación permite al usuario consultar datos climáticos como temperatura, humedad y descripción del clima para una ubicación específica ingresada como argumento.
- **Formato de Salida Personalizable:** Los usuarios pueden elegir el formato de salida de la información climática en JSON, CSV o texto plano.
- **Manejo de Errores:** Implementa manejo de errores para solicitudes fallidas o ubicaciones no encontradas, garantizando una experiencia de usuario robusta.
- **Soporte para Argumentos de Línea de Comandos:** La aplicación acepta argumentos de línea de comandos para la ubicación y el formato de salida, y muestra un mensaje de ayuda que explica cómo usar la aplicación.
- **Automatización con Bash:** Incluye un script `setup.sh` para automatizar la instalación de dependencias y la configuración del entorno de desarrollo.

## Instalación

### Requisitos Previos

- Python 3.10 o superior
- `pip` para la gestión de paquetes

### Configuración del Entorno

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/huggco97/Challenge9_CLI_GIT..git
    cd Challenge9_CLI_GIT. 
    ```

2. Ejecuta el script `setup.sh` para instalar las dependencias y configurar el entorno virtual:

    ```bash
    ./setup.sh
    ```

### Variables de Entorno

El proyecto utiliza un archivo `.env` para gestionar las claves API y otras configuraciones sensibles. Debes crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
API_KEY=tu_api_key_aqui
URL=http://api.openweathermap.org/data/2.5/weather



Ejemplo de uso

linux/Mac = python3 cli.py --ciudad "Asuncion" --formato "json"
windows = python3 cli.py --ciudad "Asuncion" --formato "json"

Ayuda

linux/Mac = python3 cli.py --help
windows = python cli.py --help 
