#coding: utf-8

# ∞∞∞∞∞ Autor: xaxxjs (https://github.com/sergioab7) ∞∞∞∞∞

import sys,os
from time import sleep
from colorama import Fore, Back, Style
import requests

def opciones():
    menu=Fore.RED+"""
    [1]"""+Fore.RESET+Fore.LIGHTRED_EX+""" DNS lookup"""+Fore.RESET+Fore.RED+""" 
    [2]"""+Fore.LIGHTRED_EX+""" Reverse DNS"""+Fore.RESET+Fore.RED+"""
    [3]"""+Fore.RESET+Fore.LIGHTRED_EX+""" Find Subdomains"""+Fore.RED+"""
    [4]"""+Fore.LIGHTRED_EX+""" Find Shared DNS Servers ➛[ns1.dnsserver.com]"""+Fore.RED+"""
    [5]"""+Fore.LIGHTRED_EX+""" Zone transfer"""+Fore.RED+"""
    [6]"""+Fore.LIGHTRED_EX+""" Whois Lookup"""+Fore.RED+"""
    [7]"""+Fore.LIGHTRED_EX+""" Volver al menú
    
    """+Fore.RESET
    print(menu)

def dns():
    try:
        opciones()
        eleccion=int(input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[DNS]~ "+Fore.RESET))
        if(eleccion==1):
            eleccion_traceroute=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[DNS/LOOKUP]"+Fore.RESET+"Ingresa Hostname de DNS~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/dnslookup/?q=%s"%(eleccion_traceroute)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==2):
            eleccion_dns_reverse=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[DNS/Reverse_DNS]"+Fore.RESET+"Ingresa IP o Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/reversedns/?q=%s"%(eleccion_dns_reverse)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==3):
            eleccion_subdominios=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[DNS/Find_Subdomains]"+Fore.RESET+"Ingresa Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/hostsearch/?q=%s"%(eleccion_subdominios)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==4):
            eleccion_dns_subdominios=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[DNS/Find_Shares_DNS_Servers]"+Fore.RESET+" Ingresa Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/findshareddns/?q=%s"%(eleccion_dns_subdominios)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==5):
            eleccion_zone_transfer=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[DNS/Zone_Transfer]"+Fore.RESET+"Ingresa Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/zonetransfer/?q=%s"%(eleccion_zone_transfer)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==6):
            eleccion_whois=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[DNS/Whois_Lookup]"+Fore.RESET+" Ingresa IP o Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/whois/?q=%s"%(eleccion_whois)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print(Fore.RED+"[!] Error"+Fore.RESET)
                sys.exit()
        elif(eleccion==7):
            os.system("clear")
            pass
        else:
            print(Fore.YELLOW + "[!] Opción incorrecta" + Fore.RESET)
            dns()
    except:
        print("\n Salida.")
        sys.exit()