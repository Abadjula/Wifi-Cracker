import os
from colorama import Fore
import subprocess as sp

if os.name != "nt":
    input("You are not a Windows User. Press Enter to Exit...")
    exit()

os.system("cls")
os.system("title Wifi Cracker")

Network = input(f"{Fore.MAGENTA}[{Fore.RESET}{Fore.LIGHTCYAN_EX}+{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.GREEN}Enter the Name of the Network you are Trying to Crack:{Fore.RESET} {Fore.LIGHTBLACK_EX}")
os.system("cls")

output = sp.getoutput(f'netsh wlan show profile {Network} key=clear')

if output == f"Profile \"{Network}\" is not found on the system.":
    print(f"{Fore.RESET}[{Fore.RED}ERROR{Fore.RESET}] {Fore.RED}Profile \"{Network}\" is not found on the system.{Fore.RESET}")
    input("\nPress any key to Exit...")
else:
    Value = output.find("Key Content")
    Hidden = output.find("Cost settings")

    Under = output.replace(output[Hidden:], "")
    Password = Under.replace(output[:Value], "")

    print(f"{Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.LIGHTCYAN_EX}+{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.GREEN}{Password}{Fore.RESET}")
    input("Press any key to Exit...")
