#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación con parámetros predeterminados
python cli.py  "Asuncion" --format "json"

# Ejecutar pruebas automatizadas
pytest tests/ #comando de prueba ./setup.sh