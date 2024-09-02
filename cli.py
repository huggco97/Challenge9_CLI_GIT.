import argparse
from clima import obtener_clima


def crear_parser():
    parser = argparse.ArgumentParser(
        description="Aplicación CLI para obtener datos climáticos de una ciudad específica."
    )
    parser.add_argument(
        "--ciudad",
        type=str,
        help="Nombre de la ciudad para la cual deseas obtener los datos climáticos.",
    )
    parser.add_argument(
        "--formato",
        choices=["json", "csv", "txt"],
        default="txt",
        help="Formato de salida de los datos climáticos. Opciones: json, csv, txt (predeterminado: txt).",
    )
    return parser


def mostrar_clima(clima, formato):
    if formato == "json":
        import json

        print(json.dumps(clima, indent=4))
    elif formato == "csv":
        import csv
        import sys

        writer = csv.writer(sys.stdout)
        writer.writerow(clima.keys())
        writer.writerow(clima.values())
    else:  # Formato txt
        print(f"Ciudad: {clima['ciudad']}")
        print(f"Temperatura: {clima['temperatura']}°C")
        print(f"Descripción: {clima['descripcion']}")
        print(f"Humedad: {clima['humedad']}%")


def main():
    parser = crear_parser()
    args = parser.parse_args()

    clima = obtener_clima(args.ciudad)

    if clima:
        mostrar_clima(clima, args.formato)


if __name__ == "__main__":
    main()
