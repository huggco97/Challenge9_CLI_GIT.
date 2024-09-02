#!/bin/bash

#Activar entorno virtual (si existe)
if [-d ".venv"]; then
    source .venv/bin/activate
else
    #crear entorno virtual
    python3 -m venv venv
    source .venv/bin/activate
fi

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación con parámetros predeterminados
python cli.py  --ciudad "Asuncion" --format "json"

# Ejecutar pruebas automatizadas
pytest tests/ #comando de prueba ./setup.sh