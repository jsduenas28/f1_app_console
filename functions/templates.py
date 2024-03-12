from pyfiglet import Figlet
from termcolor import colored
import time
import os

def info_app():
    os.system('cls')
    custom = Figlet(font='standard')
    print(colored(custom.renderText("F1 App - F1 API"), 'red'))
    
    print('App de informacion sobre la F1 usando una api publica')
    print('API: Ergast Developer API')
    print('https://ergast.com/mrd/')
    print('------------------------------------------------------')
    print('Desarrollador de la app: Josué Dueñas')
    print('https://github.com/jsduenas28')

def despedida():
    os.system('cls')
    custom = Figlet(font='standard')
    print(colored(custom.renderText("Adios"), 'red'))
    time.sleep(2)
    os.system('cls')