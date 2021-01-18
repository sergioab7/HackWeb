#coding: utf-8

# ∞∞∞∞∞ Autor: xaxxjs (https://github.com/sergioab7) ∞∞∞∞∞

import sys,os
from colorama import Fore, Back, Style
import requests
from time import sleep

def opciones():
    text=Fore.RED+"""
    [1]"""+Fore.RESET+Fore.LIGHTRED_EX+""" Traceroute"""+Fore.RESET+Fore.RED+""" 
    [2]"""+Fore.LIGHTRED_EX+""" Test Ping"""+Fore.RESET+Fore.RED+"""
    [3]"""+Fore.LIGHTRED_EX+""" Volver al menú
    
    """+Fore.RESET
    print(text)
    
def menu():
    try:
        opciones()
        eleccion=int(input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[NETWORK]~ "+Fore.RESET))
        if(eleccion==1):
            eleccion_traceroute=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[NETWORK/TRACEROUTE]"+Fore.RESET+"Ingresa IP o Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/mtr/?q=%s"%(eleccion_traceroute)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print("")
                sys.exit()
        elif(eleccion==2):
            eleccion_ip=input(Fore.YELLOW+"\t↪"+Fore.RESET+Fore.LIGHTCYAN_EX+"[NETWORK/Test_Ping]"+Fore.RESET+"Ingresa IP o Dominio~ ")
            print("")
            r=requests.get("https://api.hackertarget.com/nping/?q=%s"%(eleccion_ip)).text
            print(Fore.LIGHTGREEN_EX + r + Fore.RESET)
            try:
                sleep(0.5)
                input(Fore.GREEN+" [*] Vuelve al menú (Presiona Enter..) "+Fore.RESET)
                os.system("clear")
            except:
                print("")
                sys.exit()
        elif(eleccion==3):
            os.system("clear")
            pass
        else:
            print(Fore.YELLOW + "[!] Opción incorrecta" + Fore.RESET)
            menu()
    except:
        print("\n Salida.")
        sys.exit()