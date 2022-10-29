
from termcolor import colored
from operator import imod
import os
import caeser
import Vigenere
import Hill
import Autokey
import Playfire
import AES
import pyfiglet
app_name=colored(pyfiglet.figlet_format("CrypZ3nun"),'green')
print(app_name)

print("please choose the algorithm that you want :")
print("1- Auto-Key")
print("2- Casear")
print("3- Playfire")
ch=input()
match ch :
    case "1":os.system('cls' if os.name == 'nt' else 'clear') ; Autokey.display_Auto()
    case "2":os.system('cls' if os.name == 'nt' else 'clear') ; caeser.display_caeser()
    case "3":os.system('cls' if os.name == 'nt' else 'clear') ; Playfire.display_Playfire()
    case "4":os.system('cls' if os.name == 'nt' else 'clear') ; Vigenere.display_vigenere()
    case "5":os.system('cls' if os.name == 'nt' else 'clear') ; Hill.display_hill()
    case "6":os.system('cls' if os.name == 'nt' else 'clear') ; AES.display_AES()


