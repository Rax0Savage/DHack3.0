import requests
import datetime
import sys
import time
import argparse
import os
import colorama
import csv
import json
import vk
import random
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import itertools
import threading
import time
import base64
import urllib.request
from bs4 import BeautifulSoup
import socket
os.system('clear')
print(Fore.GREEN +
"""
░▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄░
████░░░░░░░░░░░░░░░░░░░░░░░░░░░░████
▀███▄░░░░░░░░░░▄▄▄▄▄▄░░░░░░░░░░▄███▀
░░░▀██▄██▀░▄██▀▀▀▀▀▀▀▀██▄░▀██▄██▀░░░
░░░░███████▀▄▄▄▄▄██▄▄▄▄▄▀███████░░░░
░░░░█▀████████████████████████▀█░░░░
░░░░░░░▀████████████████████▀░░░░░░░
░░░░░░░░██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀███░░░░░░░
░░░░░░░░▀█░░▄▄██▄░░▄██▄▄░░███░░░░░░░
░░░░░░░░▀█░░█████░░█████░░████░░░░░░
░░░░░░░░░█▄░░▀▀▀░▄▄░▀▀▀░░▄████░░░░░░
░░░░░░░░░░██▄▄░░████░░▄▄██████░░░░░░
░░░░░░░░░▄████░░████░░████████░░░░░░
░░░░░░░▄████▀█░░░░░░░░█▀█████░░░░░░░
░░░░▄█████▀█▄▀▀▀█▀▀█▀▀▀▄███████▄░░░░
░░▀▀▀▀▀░░░░░█▄░░▀░░▀░░▄█▀███░▀▀▀▀▀░░
░░░░░░░░░░░░░▀████████▀░░░▀▀░░░░░░░░""")
print(Fore.GREEN +
"""
░▐█▀█▄░▐█░▐█─░▄█▀▄─░▐█▀█▒▐█▒▐▀░▐█▀▀▒▐█▀▀▄
░▐█▌▐█░▐████░▐█▄▄▐█░▐█──▒▐██▌░░▐█▀▀▒▐█▒▐█
░▐█▄█▀░▐█░▐█░▐█─░▐█░▐█▄█▒▐█▒▐▄░▐█▄▄▒▐█▀▄▄ """)
print("                                        Coded by: Rax0")
print("                                        VK: @rax0savage")
print("----FISHING-----")
print("[1]kingfish2 - Фишинг VK и Instagram")
print("[2]Recreator-Phishing - много вариантов фишинга")
print("-----DEANON-----")
print("[3]sherlock - Можно много всего (Например пробить номер телефона)")
print("-----VK-----")
print("[4]VkToPass - Брутофорс ВК")
print("[5]VkRaidBot - Убивает бееседы в ВК спамом")
print("[6]VKTOOL - Утилита спамит посты и комментарии")
print("-----SMS SPAM-----")
print("[7]smsham - Утилита для спама смс на номер телефона")
print("-----DDOS ATTACK-----")
print("[8]Doser - утилита для DoS Аттак")
print("-----Others-----")
print("[9]Bot Bilder - Утилита поможет сделать ботов для ВК")
print(" ")
print("ВНИМАНИЕ: Автор не несет ответственности за ваши действия с этими утилитами")
print(" ")
print("    ")
print("Введите Номер: ")
while True:
    num =int(input("\033[35m\033[5m[*]"))
    if num == (1) :
        print("Запуск kingfish2...")
        os.system('clear')
        os.chdir('kingfish2')
        os.system('python3 fsh.py')
    elif num == (2):
        print (Fore.GREEN + 'Запуск Recreator-Phishing...')
        os.system('clear')
        os.chdir('DH')
        os.chdir('Recreator-Phishing')
        os.system('python3 ServerInstall.py')
        print("Запуск...")
        os.system('python3 recreator-phishing.py')
    elif num == (3):
        print (Fore.GREEN + 'Запуск Sherlock')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 sherl.py')
    elif num == (4):
        print (Fore.GREEN + 'Запуск VkToPass')
        os.system('clear')
        os.chdir('DH')
        print("Загрузка...")
        time.sleep(4)
        os.system('python3 vtp_db.py')
    elif num == (5):
        print (Fore.GREEN + 'Запуск VkRaidBot..')
        os.system('clear') 
        os.chdir('DH')
        print("После того как вам напишет Bot started зайдите в это сообщество в ВК club195563900 и нажми на кнопку Добавить в беседу выбераете беседу и бот начнет спамить в выбранную беседу")
        os.system('python3 vkraid.py')
    elif num == (6):
        print (Fore.GREEN + 'Запуск VKTOOL...')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 vktool.py')
    elif num == (7):
        print (Fore.GREEN + 'Запуск SmsHam...')
        os.system('clear')
        os.chdir('smsham')
        os.system('python3 smsham.py')
    elif num == (8):
        print (Fore.GREEN + 'Запуск VKTOOL...')
        os.system('clear')
        os.chdir('DH')
        os.chdir('Doser')
        os.system('python3 doser.py')
    elif num == (9):
        print (Fore.GREEN + 'Запуск BotBilder...')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 botbilder.py')
