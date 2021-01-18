#coding: utf-8

# ∞∞∞∞∞ Autor: xaxxjs (https://github.com/sergioab7) ∞∞∞∞∞

import sys,os
from colorama import Fore, Back, Style
import warnings
import signal
from time import sleep
from beautifultable import BeautifulTable
import platform
from modules import network,dns,ip,web

warnings.filterwarnings("ignore")

##Linux/Mac
if(platform.system()=="Linux" or platform.system()=="Darwin"):
    pass
else:
    print(Fore.RED + "Necesitas correrlo en Linux o Mac" + Fore.RESET)
    sys.exit(1)

if(os.geteuid() != 0):
    print(Fore.RED + "Necesitas ser root!" + Fore.RESET)
    sys.exit(1)
else:
    pass

### Inicio módulos
os.system("clear")
print(Fore.BLUE+"Realizando comprobaciones.."+Fore.RESET)
sleep(1)
try:
    if("colorama" in sys.modules):
        print(Fore.GREEN+"✅ Modulos instalados correctamente "+Fore.RESET)
        sleep(1.5)
        os.system("clear")
except:
    print(Fore.RED+"Moulo colorama no instalado"+Fore.RESET)
    sys.exit(1)

### Ctrl+c
def signal_handler(key,frame):
    print(Fore.YELLOW + "\n[*]" + Fore.RESET + "[!] Saliendo... \n")
    print(Style.RESET_ALL)
    sys.exit(1)

signal=signal.signal(signal.SIGINT,signal_handler)


###Inicio funciones

def menu():
    menu=Fore.RED+"""
    [1]"""+Fore.RESET+Fore.LIGHTRED_EX+""" Network"""+Fore.RESET+Fore.RED+""" 
    [2]"""+Fore.LIGHTRED_EX+""" DNS"""+Fore.RESET+Fore.RED+"""
    [3]"""+Fore.RESET+Fore.LIGHTRED_EX+""" IP Address"""+Fore.RED+"""
    [4]"""+Fore.LIGHTRED_EX+""" Web Tools"""+Fore.RED+"""
    [5]"""+Fore.LIGHTRED_EX+""" Salir
    
    """+Fore.RESET
    print(menu)

def banner():
    text=Fore.LIGHTBLUE_EX+"""    ,--.  ,--.              ,--.    ,--.   ,--.       ,--.    
    |  '--'  | ,--,--. ,---.|  |,-. |  |   |  | ,---. |  |-.  
    |  .--.  |' ,-.  || .--'|     / |  |.'.|  || .-. :| .-. ' 
    |  |  |  |\ '-'  |\ `--.|  \  \ |   ,'.   |\   --.| `-' | 
    `--'  `--' `--`--' `---'`--'`--''--'   '--' `----' `---'  """+Fore.RESET+""" v.1
//////////////////////////////////////////////////////////////////////
//                  Github :"""+Fore.GREEN+"""sergioab7"""+Fore.RESET+"""                               //
//                  Web:"""+Fore.GREEN+"""sergioab7.github.io"""+Fore.RESET+"""                         //
//////////////////////////////////////////////////////////////////////
                """
    
                
    print(text) 


start=True
while(start):
    banner()
    menu()
    eleccion=int(input(Fore.YELLOW+"⚡"+Fore.RESET+"~ "))
    if(eleccion==1):
        network.menu()
    elif(eleccion==2):
        dns.dns()
    elif(eleccion==3):
        ip.ip()
    elif(eleccion==4):
        web.web()
    elif(eleccion==5):
        sys.exit(1)
    else:
        print("nada")




