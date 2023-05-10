#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, json
import os
import time

class colores:
    red="\033[31;1m"


os.system("clear")
logo = colores.red + '''
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
            | Spyrod Version: v4|
            |___________________|
     
'''

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
    print('[~] [Proxy, VPN o Tor no encontrado!]')

def locate():
  print('\n[~] Escribe la IP de la victima')
  ipin = input('[~] IP: ')
  print(f'[~] Buscando datos de: {ipin}')
  time.sleep(1)
  api = f"http://ip-api.com/json/{ipin}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  data = requests.get(api).json()
  ##-----------Query---------##
  print("\n[~] [IP De la victima]:", data['query'])
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
      print('[~] [Proxy, VPN o Tor no encontrado!]')
  except KeyError:
    print(f'\n[~] Error al intentar obtener datos de {ipin}')

def menu():
  print(logo)
  print('[1] Localizar una IP')
  print('[2] Localizar tu propia IP')
  print('[99] Salir')
  var = int(input('\n>> '))
  if var == 1:
    locate()
  elif var == 2:
    per()
  elif var == 99:
    print('\n[~] Saliendo del programa...')
    time.sleep(1)
    exit()
  else:
    print('\n[~] Error opcion invalida.')
    time.sleep(2)
    menu()

menu()
