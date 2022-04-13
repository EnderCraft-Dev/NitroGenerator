from tkinter import messagebox

from utils.generator import generate_code

from colorama import *

from time import sleep

init(convert=True)


title = """
███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝"""

print(Fore.YELLOW+title+Fore.WHITE)
print("\n")
print("""
█▄▄ █▄█   █▀▀ █▄░█ █▀▄ █▀▀ █▀█ █▀▄ █▀▀ █░█
█▄█ ░█░   ██▄ █░▀█ █▄▀ ██▄ █▀▄ █▄▀ ██▄ ▀▄▀""")
print("\n")
print(Fore.LIGHTBLUE_EX+"[+] GitHub: https://github.com/EnderCraft-Dev"+Fore.WHITE)

print("")
url_amount = int(input("[+] Enter how many codes do you want to generate: "))

codes = generate_code(url_amount)
print(Fore.LIGHTYELLOW_EX+"\n[+]generating codes..."+Fore.WHITE)

file = open("CODES.txt", 'w')

for code in codes:
    sleep(1)
    print(Fore.LIGHTCYAN_EX+code+Fore.WHITE)
    file.write(code+"\n")
file.close()


sleep(0.5)
print("")
input("press enter to close the window...")