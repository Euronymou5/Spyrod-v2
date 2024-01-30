# Updated version by JetnBerries https://github.com/JetBerri

import requests
import time
import os

from colorama import Fore as color

logo = (f"{color.RED}"
        "             uu$:$:$:$:$:$uu\n"
        "          uu$$$$$$$$$$$$$$$$$uu\n"
        "         u$$$$$$$$$$$$$$$$$$$$$u\n"
        "         u$$$$$$$$$$$$$$$$$$$$$$$u\n"
        "       u$$$$$$$$$$$$$$$$$$$$$$$$$u\n"
        "       u$$$$$$$$$$$$$$$$$$$$$$$$$u\n"
        "       u$$$$$$*   *$$$*   *$$$$$$u\n"
        "       *$$$$*      u$u       $$$$*\n"
        "        $$$u       u$u       u$$$\n"
        "        $$$u      u$$$u      u$$$\n"
        "         *$$$$uu$$$   $$$uu$$$$*\n"
        "          *$$$$$$$*   *$$$$$$$*\n"
        "            u$$$$$$$u$$$$$$$u\n"
        "             u$*$*$*$*$*$*$u\n"
        "  uuu        $$u$ $ $ $ $u$$       uuu\n"
        " u$$$$        $$u$u$u$u$u$$       u$$$$\n"
        "  $$$$$uu      *$$$$$$$$$*     uu$$$$$$\n"
        "u$$$$$$$$$$$      *****    uuuu$$$$$$$$$\n"
        "$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$\n"
        "***      **$$$$$$$$$$$uu **$***\n"
        "          uuuu **$$$$$$$$$$uuu\n"
        " u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$\n"
        "$$$$$$$$$$****           **$$$$$$$$$$$*\n"
        "   *$$$$$*                      **$$$$**\n"
        "     $$$*    ___________________  $$$$*\n"
        "            |Made by: Euronymou5|\n"
        "            |___________________|\n"
        "            | Spyrod Version: v4|\n"
        "            |___________________|\n"
        f"{color.RESET}")

os.system("clear")
print(logo)

def save_data_to_file(filename, data):
    with open(filename, "w") as file:
        for label, value in data.items():
            file.write(f"[~] [{label}]: {value}\n")

def own_ip():
    try:
        respuesta = requests.get('https://httpbin.org/ip')
        tu_ip = respuesta.json()['origin']
        
        return tu_ip
    
    except requests.RequestException as e:
        print(f"Error al obtener la dirección IP: {e}")

tu_ip = own_ip()    

def print_data(label, value):
    if value:
        print(f"[~] [{label}]: {value}")
    else:
        print(f"[~] [{label} no encontrado!]")

def display_location_data(data):
    labels = ["IP De la victima", "ISP", "Organizacion", "Ciudad", "Nombre del país",
              "Region", "Nombre del continente", "Región / estado", "Código de continente de dos letras",
              "Latitud", "Longitud", "Zona horaria", "Codigo zip", "AS número y organización",
              "Código de país de dos letras", "DNS inverso de la IP", "Conexión móvil (celular)",
              "Moneda nacional", "Distrito (subdivisión de la ciudad)", "Proxy, VPN o Tor"]

    for label in labels:
        print_data(label, data.get(label.lower(), False))

def locate(ipin):

    api = f"http://ip-api.com/json/{ipin}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

    try:
        data = requests.get(api).json()
        print_data("IP De la victima", data.get('query', False))
        print_data("ISP", data.get('isp', False))
        print_data("Organizacion", data.get('org', False))
        print_data("Ciudad", data.get('city', False))
        print_data("Nombre del país", data.get('country', False))
        print_data("Region", data.get('region', False))
        print_data("Nombre del continente", data.get('continent', False))
        print_data("Región / estado", data.get('regionName', False))
        print_data("Código de continente de dos letras", data.get('continentCode', False))
        print_data("Latitud", data.get('lat', False))
        print_data("Longitud", data.get('lon', False))
        print_data("Zona horaria", data.get('timezone', False))
        print_data("Codigo zip", data.get('zip', False))
        print_data("AS número y organización", data.get('as', False))
        print_data("Código de país de dos letras", data.get('countryCode', False))
        print_data("DNS inverso de la IP", data.get('reverse', False))
        print_data("Conexión móvil (celular)", data.get('mobile', False))
        print_data("Moneda nacional", data.get('currency', False))
        print_data("Distrito (subdivisión de la ciudad)", data.get('district', False))
        print_data("Proxy, VPN o Tor", data.get('proxy', False))
        
        save_data_to_file(f"{ipin}.txt", data)
    
    except Exception as e:
        print(f'\n[~] Error al intentar obtener datos de {ipin}')

def menu():
    
    print('[1] Localizar una IP')
    print('[99] Salir')
    
    try:
        var = int(input('\n>> '))
        if var == 1:

            time.sleep(1)
            print("\n")
            print(f"Tu direccion IP es : {tu_ip}")
            print('\n[~] Escribe la IP de la victima')
            ipin = input('[~] IP: ')
            print(f'[~] Buscando datos de: {ipin}')
            time.sleep(1)
            locate(ipin)
        elif var == 99:
            print('\n[~] Saliendo del programa...')
            time.sleep(1)
            exit()
        else:
            print('\n[~] Error opcion invalida.')
            time.sleep(2)
            menu()
    except ValueError:
        print('\n[~] Por favor, ingresa un número válido.')
        time.sleep(2)
        menu()

if __name__ == "__main__":

    menu()
