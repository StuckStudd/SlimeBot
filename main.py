import time
import requests
import json
import os
from colorama import Style, Fore


weather = ("weather", "what is the weather?", "weather in stockholm", "weather in stockholm?")
crypto = ("current google stocks", "google stocks", "google stock", "google shares", "stock", "stocks")
commands = ("help",)


with open("database.json", "r") as f:
    data = json.load(f)

def get_stockholm_weather():
    url = "https://wttr.in/Stockholm?format=3"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Weather : {response.text.strip()}")
    else:
        print("Failed to connect to the server!")

def google_crypto():
    url = "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL"
    
   
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    
    if response.status_code == 200:
        
        stock_data = response.json()
        price = stock_data['chart']['result'][0]['meta']['regularMarketPrice']
        print(f"Google Stock Price: ${price}")
    else:
        print(f"Failed to connect to the server! Code: {response.status_code}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_data():
    with open("database.json", "w") as f:
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
    print("Write 'help' if you want to know the commands")

    choice = input("-->> ").lower().strip()

    if choice in weather:
        get_stockholm_weather()
        time.sleep(3)
        clear_console() #
        continue
        

    elif choice in crypto:
        google_crypto()
        time.sleep(3)
        clear_console()
        continue

    elif choice in commands:
        clear_console()
        print("Commands : ")
        print("- You can find out the weather in Stockholm")
        print("- You can find out current Google stocks")
        print("")
        time.sleep(4)
        clear_console()
        
    elif choice == "exit":
        print("Shutting down...")
        break
        
    else:
        print("Command not found!")
        time.sleep(1)
        clear_console()