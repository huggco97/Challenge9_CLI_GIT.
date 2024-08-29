import subprocess
import sys

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(f"Salida:\n{resultado.stdout}")
        if resultado.returncode != 0:
            print(f"Error:\n{resultado.stderr}")
        return resultado.returncode == 0
    except Exception as e:
        print(f"Error al ejecutar el comando {comando}: {e}")
        return False

def probar_cli():
    # Prueba: Mostrar ayuda
    print("Prueba: Mostrar ayuda")
    if not ejecutar_comando("python cli.py --help"):
        sys.exit(1)

    # Prueba: Obtener clima para una ciudad válida
    print("Prueba: Obtener clima para 'Asuncion'")
    if not ejecutar_comando("python cli.py --ciudad Asuncion"):
        sys.exit(1)

    # Prueba: Obtener clima para una ciudad no válida
    print("Prueba: Obtener clima para una ciudad no válida 'Ciudad_Inexistente'")
    if not ejecutar_comando("python cli.py --ciudad Namekusein"):
        sys.exit(1)

    # Prueba: Obtener clima con formato JSON
    print("Prueba: Obtener clima para 'Asuncion' en formato JSON")
    if not ejecutar_comando("python cli.py --ciudad Asuncion --formato json"):
        sys.exit(1)

    # Prueba: Obtener clima con formato CSV
    print("Prueba: Obtener clima para 'Asuncion' en formato CSV")
    if not ejecutar_comando("python cli.py --ciudad Asuncion --formato csv"):
        sys.exit(1)

    print("Todas las pruebas han pasado correctamente.")

if __name__ == "__main__":
    probar_cli()
