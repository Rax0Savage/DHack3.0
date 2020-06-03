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
print("[1]kingfish2 - Phishing VK and Instagram")
print("[2]Recreator-Phishing -  Many phishing options")
print("-----DEANON-----")
print("[3]sherlock - You can do a lot of things(for example, break a phone number)")
print("-----VK-----")
print("[4]VkToPass - BruteForce VK")
print("[5]VkRaidBot - Kill conversations in VK by spam")
print("[6]VKTOOL - Spam comments and posts in VK")
print("-----SMS SPAM-----")
print("[7]smsham - Spam sms on phone number")
print("-----DDOS ATTACK-----")
print("[8]Doser - DDoS Attack")
print("-----Others-----")
print("[9]Bot Bilder - Create bot for VK")
print(" ")
print("ATTENTION: The author is not responsible for the actions of users with these utilities")
print(" ")
print("    ")
print("Enter number: ")
while True:
    num =int(input("\033[35m\033[5m[*]"))
    if num == (1) :
        print("Loading kingfish2...")
        os.system('clear')
        os.chdir('kingfish2')
        os.system('python3 fsh.py')
    elif num == (2):
        print (Fore.GREEN + 'Loading Recreator-Phishing...')
        os.system('clear')
        os.chdir('DH')
        os.chdir('Recreator-Phishing')
        os.system('python3 ServerInstall.py')
        print("Запуск...")
        os.system('python3 recreator-phishing.py')
    elif num == (3):
        print (Fore.GREEN + 'Loading Sherlock')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 sherl.py')
    elif num == (4):
        print (Fore.GREEN + 'Loading VkToPass')
        os.system('clear')
        os.chdir('DH')
        print("Загрузка...")
        time.sleep(4)
        os.system('python3 vtp_db.py')
    elif num == (5):
        print (Fore.GREEN + 'Loading VkRaidBot..')
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
        print (Fore.GREEN + 'Loading SmsHam...')
        os.system('clear')
        os.chdir('smsham')
        os.system('python3 smsham.py')
    elif num == (8):
        print (Fore.GREEN + 'Loading VKTOOL...')
        os.system('clear')
        os.chdir('DH')
        os.chdir('Doser')
        os.system('python3 doser.py')
    elif num == (9):
        print (Fore.GREEN + 'Loading BotBilder...')
        os.system('clear')
        os.chdir('DH')
        os.system('python3 botbild.py')
