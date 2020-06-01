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
░▐█▀█▄░▐█░▐█─░▄█▀▄─░▐█▀█▒▐█▒▐▀░▐█▀▀▒▐█▀▀▄
░▐█▌▐█░▐████░▐█▄▄▐█░▐█──▒▐██▌░░▐█▀▀▒▐█▒▐█
░▐█▄█▀░▐█░▐█░▐█─░▐█░▐█▄█▒▐█▒▐▄░▐█▄▄▒▐█▀▄▄
                                                                                                                                                                     """)
print("Автор: Rax0")
print("VK: @rax0savage")
print("----FISHING-----")
print("[1]kingfish3 - Король Фишинга очень много вариантов для Фишинга(Фишинг ВК и прочее)")
print("-----DEANON-----")
print("[2]sherlock - Можно много всего (Например пробить номер телефона)")
print("[3]seeker - Вычисляет данные телефона")
print("-----VK-----")
print("[4]VkRaidBot - Убивает бееседы в ВК спамом")
print("[5]VKTOOL - Утилита спамит посты и комментарии")
print("-----SMS SPAM-----")
print("[6]smsham - Утилита для спама смс на номер телефона")
print("Others")
print("[7]Bot Bilder - Утилита поможет сделать ботов для ВК")
print("Авторы утилит: Sudoreboot2020, Shotfly-tlab, Rax0")
print("    ")
print("Введите Номер: ")
while True:
    num =int(input("\033[35m\033[5m[*]"))
    if num == (1) :
        print("Запуск kingfish3...")
        os.system('clear')
        os.chdir('DH')
        os.system('python3 fsh.py')
    elif num == (2):
        print (Fore.GREEN + 'Запуск Sherlock')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 sherlock.py')
    elif num == (3):
        print (Fore.GREEN + 'Запуск Seeker')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 seeker.py -t manual')
    elif num == (4):
        print (Fore.GREEN + 'Запуск VkRaidBot')
        os.system('clear')
        os.chdir('DH')
        print("После запуска вам должно написать Bot Started после этого зайди в это сообщество в ВК club195563900 и нажмите Добавить в беседу и бот начнёт спамить в выбраную беседу")
        print("Загрузка...")
        time.sleep(4)
        os.system('python3 vkraid.py')
    elif num == (5):
        print (Fore.GREEN + 'Запуск VKTOOL...')
        os.system('clear') 
        os.chdir('DH')
        os.system('python3 vktool.py')
    elif num == (6):
        print (Fore.GREEN + 'Запуск vktool ...')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 smsham.py')
    elif num == (7):
        print (Fore.GREEN + 'Запуск BotBilder...')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 botvk.py')
