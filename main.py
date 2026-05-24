import time
import random
import requests
import json
import os
from colorama import Style, Fore


weather = "Погода", "погода", "Что за окном?", "Погода стокгольм", "Погода?", "погода?"

with open("database.json", "r")as f:
    data = json.load(f)

import requests

def get_stockholm_weather():
    # Эта ссылка возвращает погоду в Стокгольме в виде короткой строки
    url = "https://wttr.in/Stockholm?format=3"
    
    # Делаем запрос к сайту
    response = requests.get(url)
    
    # Если сайт ответил без ошибок, выводим текст
    if response.status_code == 200:
        print(f"Результат с сайта: {response.text}")
    else:
        print("Не удалось подключится к серверу :( разроботчик уже знает о проблеме и исправляет ее!")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_data():
    with open("database.json", "w")as f:
        json.dump(data, f, indent=4)

print("Loading system..")
time.sleep(2)

print(Fore.GREEN + "Success" + Style.RESET_ALL)

clear_console()

while True:
    print("Welcome to Lime Bot!")
    print("===================")
    print(f"Subscribe : {data['subscribe']}")
    print("===================")
    print("Вы можете узнать погоду.")

    choice = input("-->> ")

    if choice in weather:
        get_stockholm_weather()
        time.sleep(3)
        continue

