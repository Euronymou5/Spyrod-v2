# -*- coding: utf-8 -*-

import os
import requests
import argparse
import time
from colorama import Fore

logo = f"""{Fore.RED}
             uu$:$:$:$:$:$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
         u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$*   *$$$*   *$$$$$$u
       *$$$$*      u$u       $$$$*
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         *$$$$uu$$$   $$$uu$$$$*
          *$$$$$$$*   *$$$$$$$*
            u$$$$$$$u$$$$$$$u
             u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$u$u$u$u$u$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$      *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$**
     $$$*    ___________________  $$$$*
            |Made by: Euronymou5|
            |___________________|
            | Spyrod Version: v5|
            |___________________|
"""

parser = argparse.ArgumentParser()
parser.add_argument("-track", "-t", type=str, help="Introduce alguna IP para obtener informacion.")
parser.add_argument("-trackme", "-tm", action='store_true', help="Obten informacion de tu propia IP.")
args = parser.parse_args()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def locate(ip):
  print(f'[~] Buscando datos de: {ip}')
  time.sleep(1)
  api = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  data = requests.get(api).json()
  ##-----------Query---------##
  print("\n[~] [IP]:", data['query'])
  ##--------------ISP-----------
  try:
    print("[~] [ISP] :", data['isp'])
    if data['isp'] == False:
      print('[~] [ISP no encontrado!]')
  ##------------Org-----------##
    print("[~] [Organizacion]:", data['org'])
    if data['org'] == False:
     print('[~] [Organizacion no encontrado!]')
  ##-----------City---------##
    print("[~] [Ciudad]:", data['city'])
    if data['city'] == False:
     print('[~] [Ciudad no encontrada!]')
  ##-----------Country---------##
    print("[~] [Nombre del país]:", data['country'])
    if data['country'] == False:
     print('[~] [Nombre del pais no encontrado!]')
  ##----------Region-------##
    print("[~] [Region]:", data['region'])
    if data['region'] == False:
     print('[~] [Region no encontrada!]')
  ##---------Nombre del continente---
    print("[~] [Nombre del continente]:", data['continent'])
    if data['country'] == False:
     print('[~] [Nombre del continente no encontrado!]')
  #-----------Región / estado-------##
    print("[~] [Región / estado]:", data['regionName'])
    if data['regionName'] == False:
      print('[~] [Region / Estado no encontrado!]')
  ##----------2 letras continente##---
    print("[~] [Código de continente de dos letras]:", data['continentCode'])
    if data['country'] == False:
     print('[~] [Código de continente de dos letras no encontrado!]')
  #---Latitud----##
    print("[~] [Latitud]:", data['lat'])
    if data['lat'] == False:
     print('[~] [Latitud no encontrada!]')
  ##----------Longitud------##
    print("[~] [Longitud]:", data['lon'])
    if data['lon'] == False:
      print('[~] [Longitud no encontrada!]')
  ##--------------Timezone---------##
    print("[~] [Zona horaria]:", data['timezone'])
    if data['timezone'] == False:
      print('[~] [Zona horaria no encontrada!]')
  ##-------------- ZIP--------------##
    print("[~] [Codigo zip]:", data['zip'])
    if data['zip'] == False:
      print('[~] [Codigo zip no encontrado!]')
  ##------------ AS -------------------##
    print("[~] [AS número y organización]:", data['as'])
    if data['as'] == False:
      print('[~] [AS número y organización no encontrado!]')
  ##-----------Countrycode-----##
    print("[~] [Código de país de dos letras]:", data['countryCode'])
    if data['countryCode'] == False:
     print('[~] [Código de país de dos letras no encontrado!]')
  ##-----------Reverse IP---------##
    print("[~] [DNS inverso de la IP]: ", data['reverse'])
    if data['reverse'] == False:
      print('[~] [DNS inverso de la IP!]')
  ##--------------Mobile------##
    print("[~] [Conexión móvil (celular)]:", data['mobile'])
    if data['mobile'] == False:
      print('[~] [Conexión móvil no encontrado!]')
  #----currency----##
    print('[~] [Moneda nacional]:', data['currency'])
    if data['currency'] == False:
      print('[~] [Moneda nacional no encontrada!]')
  #-----district----#
    print('[~] [Distrito (subdivisión de la ciudad)]:', data['district'])
    if data['district'] == False:
      print('[~] [Distrito no encontrado!]')
  #-------Proxy-----#
    print('[~] [Proxy, VPN o Tor]:', data['proxy'])
    if data['proxy'] == False:
      print('[~] [VPN No detectado.]')
  except KeyError:
    print(f'\n[~] Error al intentar obtener datos de {ip}')

def per():
  api2 = f"http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  time.sleep(1)

  data = requests.get(api2).json()
  ##-----------Query---------##
  print("\n[~] [IP]:", data['query'])
  ##--------------ISP-----------
  print("[~] [ISP] :", data['isp'])
  if data['isp'] == False:
    print('[~] [ISP no encontrado!]')
  ##------------Org-----------##
  print("[~] [Organizacion]:", data['org'])
  if data['org'] == False:
    print('[~] [Organizacion no encontrado!]')
  ##-----------City---------##
  print("[~] [Ciudad]:", data['city'])
  if data['city'] == False:
    print('[~] [Ciudad no encontrada!]')
  ##-----------Country---------##
  print("[~] [Nombre del país]:", data['country'])
  if data['country'] == False:
    print('[~] [Nombre del pais no encontrado!]')
  ##----------Region-------##
  print("[~] [Region]:", data['region'])
  if data['region'] == False:
    print('[~] [Region no encontrada!]')
  ##---------Nombre del continente---
  print("[~] [Nombre del continente]:", data['continent'])
  if data['country'] == False:
    print('[~] [Nombre del continente no encontrado!]')
  #-----------Región / estado-------##
  print("[~] [Región / estado]:", data['regionName'])
  if data['regionName'] == False:
    print('[~] [Region / Estado no encontrado!]')
  ##----------2 letras continente##---
  print("[~] [Código de continente de dos letras]:", data['continentCode'])
  if data['country'] == False:
    print('[~] [Código de continente de dos letras no encontrado!]')
  #---Latitud----##
  print("[~] [Latitud]:", data['lat'])
  if data['lat'] == False:
    print('[~] [Latitud no encontrada!]')
  ##----------Longitud------##
  print("[~] [Longitud]:", data['lon'])
  if data['lon'] == False:
    print('[~] [Longitud no encontrada!]')
  ##--------------Timezone---------##
  print("[~] [Zona horaria]:", data['timezone'])
  if data['timezone'] == False:
    print('[~] [Zona horaria no encontrada!]')
  ##-------------- ZIP--------------##
  print("[~] [Codigo zip]:", data['zip'])
  if data['zip'] == False:
    print('[~] [Codigo zip no encontrado!]')
  ##------------ AS -------------------##
  print("[~] [AS número y organización]:", data['as'])
  if data['as'] == False:
    print('[~] [AS número y organización no encontrado!]')
  ##-----------Countrycode-----##
  print("[~] [Código de país de dos letras]:", data['countryCode'])
  if data['countryCode'] == False:
    print('[~] [Código de país de dos letras no encontrado!]')
  ##-----------Reverse IP---------##
  print("[~] [DNS inverso de la IP]: ", data['reverse'])
  if data['reverse'] == False:
    print('[~] [DNS inverso de la IP!]')
  ##--------------Mobile------##
  print("[~] [Conexión móvil (celular)]:", data['mobile'])
  if data['mobile'] == False:
    print('[~] [Conexión móvil no encontrado!]')
  #----currency----##
  print('[~] [Moneda nacional]:', data['currency'])
  if data['currency'] == False:
    print('[~] [Moneda nacional no encontrada!]')
  #-----district----#
  print('[~] [Distrito (subdivisión de la ciudad)]:', data['district'])
  if data['district'] == False:
    print('[~] [Distrito no encontrado!]')
  #-------Proxy-----#
  print('[~] [Proxy, VPN o Tor]:', data['proxy'])
  if data['proxy'] == False:
    print('[~] [VPN No detectado.]')

clear()
print(logo)

if args.track:
    locate(args.track)

if args.trackme:
    per()

if not any(vars(args).values()):
    print("""
    [!] Error necesitas ingresar algun argumento.
          
    -track, -t, Introduce alguna IP para obtener informacion.
          
    -trackme, -tm, Obten informacion de tu propia IP.
    """)
