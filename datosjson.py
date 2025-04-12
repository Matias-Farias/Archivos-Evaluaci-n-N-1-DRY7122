#!/usr/bin/env python3
import json
import time
from datetime import datetime

try:
    with open("myfile.json", "r") as f:
        ourjson = json.load(f)

    token = ourjson.get("token", "Sin token")
    expires_at = ourjson.get("expires_at", None)

    print("Token:", token)

    if expires_at:
        current_time = time.time()
        seconds_left = int(expires_at - current_time)

        horas = seconds_left // 3600
        minutos = (seconds_left % 3600) // 60
        segundos = seconds_left % 60

        print("Tiempo restante antes de caducar el token:")
        print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
    else:
        print("No se encontró información de expiración en el JSON.")
except FileNotFoundError:
    print("El archivo 'myfile.json' no se encontró.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")
