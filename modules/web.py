#coding: utf-8

# ∞∞∞∞∞ Autor: xaxxjs (https://github.com/sergioab7) ∞∞∞∞∞

import sys,os
from colorama import Fore, Back, Style
import requests
from time import sleep

def opciones():
    text=Fore.RED+"""
    [1]"""+Fore.RESET+Fore.LIGHTRED_EX+""" HTTP Headers"""+Fore.RESET+Fore.RED+""" 
    [2]"""+Fore.LIGHTRED_EX+""" Extract Page Links"""+Fore.RESET+Fore.RED+"""
    [3]"""+Fore.LIGHTRED_EX+""" Reverse Analytics Search"""+Fore.RESET+Fore.RED+"""
    [4]"""+Fore.LIGHTRED_EX+""" Volver al menú
    
    """+Fore.RESET
    print(text)
    
def web():
    try:
        opciones()
        eleccion=int(input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[WEB]~ "+Fore.RESET))
        if(eleccion==1):
            eleccion_http_headers=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[WEB/HTTP_Headers]"+Fore.RESET+"Ingresa Dominio ~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/httpheaders/?q=%s"%(eleccion_http_headers)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print("")
                sys.exit()
        elif(eleccion==2):
            eleccion_extract_page_links=input(Fore.YELLOW+"\t↪"+Fore.RESET++Fore.LIGHTCYAN_EX+"[WEB/Extract_Page_Links]"+Fore.RESET+" Ingresa Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/pagelinks/?q=%s"%(eleccion_extract_page_links)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print("")
                sys.exit()
        elif(eleccion==3):
            eleccion_reverse_anal=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[WEB/Reverse_Analytics_Search]"+Fore.RESET+" Ingresa Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/analyticslookup/?q=%s"%(eleccion_reverse_anal)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print("")
                sys.exit()
        elif(eleccion==4):
            os.system("clear")
            pass
        else:
            print(Fore.YELLOW + "[!] Opción incorrecta" + Fore.RESET)
            menu()
    except:
        print("\n Salida.")
        sys.exit()