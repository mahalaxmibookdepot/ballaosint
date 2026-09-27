import requests
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def clear_screen():
    os.system('clear')

def show_banner():
    # Updated ASCII Art to clearly show "YASH CODE"
    banner = rf"""
{Fore.GREEN}##########################################################
{Fore.CYAN}             SUBSCRIBE YT: YASH CODE WITH AI
{Fore.GREEN}##########################################################
{Fore.WHITE}
  __   __         _        ____           _      
  \ \ / /_ _  ___| |__    / ___|___   __| | ___ 
   \ V / _` |/ __| '_ \  | |   / _ \ / _` |/ _ \
    | | (_| \__ \ | | |  | |__| (_) | (_| |  __/
    |_|\__,_|___/_| |_|   \____\___/ \__,_|\___|
    
{Fore.CYAN}                 --- WITH AI ---
{Fore.YELLOW}           [+] Telegram ID Lookup Tool [+]
{Fore.GREEN}##########################################################
    """
    print(banner)

def fetch_details():
    clear_screen()
    show_banner()
    
    # User Input
    tg_id = input(f"{Fore.YELLOW}Enter Telegram ID: {Fore.WHITE}")
    
    if not tg_id:
        print(f"{Fore.RED}Error: Telegram ID cannot be empty!")
        return

    # API Configuration
    api_url = f""

    print(f"\n{Fore.BLUE}[*] Fetching data from database...")

    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()

        if data.get("success"):
            print(f"\n{Fore.GREEN}[+] DETAILS FOUND:")
            print(f"{Fore.CYAN}------------------------------------")
            print(f"{Fore.WHITE}TG ID        : {Fore.YELLOW}{data.get('tg_id')}")
            print(f"{Fore.WHITE}Name         : {Fore.YELLOW}{data.get('name')}")
            print(f"{Fore.WHITE}Username     : {Fore.YELLOW}@{data.get('username')}")
            print(f"{Fore.WHITE}Country      : {Fore.YELLOW}{data.get('country')}")
            print(f"{Fore.WHITE}Country Code : {Fore.YELLOW}{data.get('country_code')}")
            
            num = data.get('number')
            print(f"{Fore.WHITE}Phone Number : {Fore.YELLOW}{num if num else 'Not Found'}")
            print(f"{Fore.CYAN}------------------------------------")
        else:
            print(f"\n{Fore.RED}[-] Error: {data.get('msg', 'No data found for this ID')}")

    except Exception as e:
        print(f"\n{Fore.RED}[!] Connection Error: Please check your internet!")

    print(f"\n{Fore.MAGENTA}Subscribe to Yash code with AI for more tools!")
    input(f"\n{Fore.WHITE}Press Enter to search again...")
    fetch_details() # Loops back to the start

if __name__ == "__main__":
    fetch_details()