from pystyle import *
import os
import subprocess
import requests
from colorama import Fore, init
import time
import webbrowser


os.system('clear' if os.name == 'posix' else 'cls')

intro = """

   ____            ___     __      _          _____         __          
  / __/__  ___    / _ |___/ /_ _  (_)__  ____/ __(_)__  ___/ /__ ____   By Soo Web
 _\ \/ _ \/ _ \  / __ / _  /  ' \/ / _ \/___/ _// / _ \/ _  / -_) __/   
/___/\___/\___/ /_/ |_\_,_/_/_/_/_/_//_/   /_/ /_/_//_/\_,_/\__/_/      
                                                                        
                     > Appuyez sur Entrée                      

"""

Anime.Fade(Center.Center(intro), Colors. black_to_red, Colorate.Vertical, interval=0.200, enter=True)

print(f"""{Fore.WHITE}

   ____            ___     __      _          _____         __          
  / __/__  ___    / _ |___/ /_ _  (_)__  ____/ __(_)__  ___/ /__ ____   By Soo Web
 _\ \/ _ \/ _ \  / __ / _  /  ' \/ / _ \/___/ _// / _ \/ _  / -_) __/   
/___/\___/\___/ /_/ |_\_,_/_/_/_/_/_//_/   /_/ /_/_//_/\_,_/\__/_/      
                        
                        

Bienvenue !

""")

init(autoreset=True)  

def find_admin_page(url):
    if not (url.startswith('https://') or url.startswith('http://')) or not url.endswith('/'):
        print(f"{Fore.RED}Saisie incorrecte : l'URL doit commencer par 'https://' ou 'http://' et se terminer par '/'{Fore.RESET}")
        return

    with open('admin_pages.txt', 'r') as file:
        common_admin_pages = file.read().splitlines()

    for page in common_admin_pages:
        admin_url = url + page
        response = requests.get(admin_url)

        if response.status_code == 200:
            print(f"{admin_url} - {Fore.GREEN}TRUE{Fore.RESET}")
            
        else:
            print(f"{admin_url} - {Fore.RED}FALSE{Fore.RESET}")
        time.sleep(0.001)  


while True:
    url = input(f"{Fore.WHITE}Entrez l'URL du site web :{Fore.RESET} ")

    if not (url.startswith('https://') or url.startswith('http://')) or not url.endswith('/'):
        print(f"{Fore.RED}Saisie incorrecte : l'URL doit commencer par 'https://' ou 'http://' et se terminer par '/'{Fore.RESET}")
    else:
        find_admin_page(url)

    choix = input(f"{Fore.WHITE}Voulez-vous refaire un scan ? (O/N) :{Fore.RESET} ")
    if choix.lower() != "o":
        break
