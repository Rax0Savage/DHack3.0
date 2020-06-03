import os
import colorama
from colorama import Fore , Back , Style
from colorama import init
init()
os.system('clear')
print(Fore.GREEN +
"""
░▐█▀█▄░▐█░▐█─░▄█▀▄─░▐█▀█▒▐█▒▐▀░▐█▀▀▒▐█▀▀▄
░▐█▌▐█░▐████░▐█▄▄▐█░▐█──▒▐██▌░░▐█▀▀▒▐█▒▐█
░▐█▄█▀░▐█░▐█░▐█─░▐█░▐█▄█▒▐█▒▐▄░▐█▄▄▒▐█▀▄▄ """)
print(Fore.GREEN+'Введите язык/Enter language:')
print("\033[31m[\033[33m1\033[31m] - Русский")
print("\033[31m[\033[33m2\033[31m] - English")
os.chdir('DH')
os.chdir('language')
while True:
    lag = input("\033[35m\033[5m[*]")
    if lag == ('1'):
        os.system('clear')
        os.system('python3 russian.py')
    elif lag == ('2'):
        os.system('clear')
        os.system('python3 english.py')
    else :
        print("\33[31mRETURN")
