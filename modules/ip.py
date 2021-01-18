#coding: utf-8

# ∞∞∞∞∞ Autor: xaxxjs (https://github.com/sergioab7) ∞∞∞∞∞

import sys,os
from time import sleep
from colorama import Fore, Back, Style
import requests
import subprocess

def opciones():
    menu=Fore.RED+"""
    [1]"""+Fore.RESET+Fore.LIGHTRED_EX+""" GeoIP Lookup"""+Fore.RESET+Fore.RED+""" 
    [2]"""+Fore.LIGHTRED_EX+""" Reverse IP Lookup"""+Fore.RESET+Fore.RED+"""
    [3]"""+Fore.RESET+Fore.LIGHTRED_EX+""" TCP Port Scan"""+Fore.RED+"""
    [4]"""+Fore.LIGHTRED_EX+""" UDP Port Scan"""+Fore.RED+"""
    [5]"""+Fore.LIGHTRED_EX+""" Subnet Lookup"""+Fore.RED+"""
    [6]"""+Fore.LIGHTRED_EX+""" ASN Lookup"""+Fore.RED+"""
    [7]"""+Fore.LIGHTRED_EX+""" Banner Grabbing"""+Fore.RED+"""
    [8]"""+Fore.LIGHTRED_EX+""" Volver al menú
    """+Fore.RESET
    print(menu)

def ip():
    try:
        opciones()
        eleccion=int(input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP]~ "+Fore.RESET))
        if(eleccion==1):
            eleccion_ip=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP/GeoIP_Lookup]"+Fore.RESET+"Ingresa IP~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/geoip/?q=%s"%(eleccion_ip)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==2):
            eleccion_reverse_ip=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP/Reverse_IP_Lookup]"+Fore.RESET+"Ingresa IP~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/reverseiplookup/?q=%s"%(eleccion_reverse_ip)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==3):
            eleccion_tcp_portscan=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP/TCP_Portscan]"+Fore.RESET+"Ingresa IP~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/nmap/?q=%s"%(eleccion_tcp_portscan)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==4):
            eleccion_tcp_portscan=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP/UCP_Portscan]"+Fore.RESET+"Ingresa IP~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/nmap/?q=%s"%(eleccion_tcp_portscan)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==5):
            eleccion_subnet_lookup=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP/Subnet_Lookup]"+Fore.RESET+"Ingresa IP~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/subnetcalc/?q=%s/24"%(eleccion_subnet_lookup)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==6):
            eleccion_asn_lookup=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP/ASN_Lookup]"+Fore.RESET+"Ingresa IP~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/aslookup/?q=%s"%(eleccion_asn_lookup)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==7):
            eleccion_banner=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[IP/Banner_Grabbing]"+Fore.RESET+"Ingresa IP~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/bannerlookup/?q=%s/24"%(eleccion_banner)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==8):
            os.system("clear")
            pass
        else:
            print(Fore.YELLOW + "[!] Opción incorrecta" + Fore.RESET)
            ip()
    except:
        print("Error")