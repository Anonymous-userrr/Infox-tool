import os
import time
import instaloader
import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, Style

# Banner function
def banner():
    os.system('clear')
    print(Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════╗
║         InfoX | Tool Created by       ║
║            Mr Anonymous               ║
║                                        ║
║  Follow Instagram : @mr__anonymous_11  ║
║  Follow Telegram  : @Mr_Anonymous_11   ║
╚══════════════════════════════════════╝
""" + Style.RESET_ALL)

# Instagram info function
def instagram_info():
    username = input(Fore.YELLOW + "\nEnter Instagram Username: " + Fore.RESET)
    print(Fore.CYAN + f"\nFetching info for @{username}...\n" + Fore.RESET)
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
        
        print(Fore.GREEN + f"Username    : {profile.username}")
        print(f"Full Name   : {profile.full_name}")
        print(f"Followers   : {profile.followers}")
        print(f"Following   : {profile.followees}")
        print(f"Bio         : {profile.biography}")
        print(f"Profile Pic : {profile.profile_pic_url}" + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"\nError: {e}")
        print("Maybe the username is incorrect or private profile!" + Fore.RESET)
    input("\nPress Enter to continue...")

# Phone number info function
def phone_info():
    number = input(Fore.YELLOW + "\nEnter Phone Number with country code (e.g., +911234567890): " + Fore.RESET)
    try:
        parsed_number = phonenumbers.parse(number)
        location = geocoder.description_for_number(parsed_number, 'en')
        service_provider = carrier.name_for_number(parsed_number, 'en')

        print(Fore.GREEN + f"\nLocation        : {location}")
        print(f"Service Provider : {service_provider}" + Fore.RESET)
    except:
        print(Fore.RED + "\nInvalid phone number!" + Fore.RESET)
    input("\nPress Enter to continue...")

# Main Program
while True:
    banner()
    print(Fore.CYAN + """
[1] Instagram User Info
[2] Phone Number Info
[3] Exit
""" + Fore.RESET)

    choice = input(Fore.YELLOW + "Select Option: " + Fore.RESET)

    if choice == '1':
        instagram_info()
    elif choice == '2':
        phone_info()
    elif choice == '3':
        print(Fore.GREEN + "\nThanks for using InfoX! Goodbye!\n" + Fore.RESET)
        break
    else:
        print(Fore.RED + "\nInvalid Option! Try again..." + Fore.RESET)
        time.sleep(1)
