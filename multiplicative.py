from pydoc import plain
from re import I
from termcolor import colored
import pyfiglet
crp_alg="Multiplicative"
app_name=colored(pyfiglet.figlet_format("CrypZ3nun - "+crp_alg),'green')

alphabet= "abcdefghijklmnopqrstuvwxyz"
index = dict(zip(alphabet,range(len(alphabet))))
letter = dict(zip(range(len(alphabet)),alphabet))

def encrypt(message,key):
   plain=message
   cipher=''
   for char in plain:
       if char=='':
          cipher=cipher+char
       elif char.isupper():
            cipher=cipher + chr((ord(char) * int(key) -65)%26 + 65)
       else:
            cipher=cipher + chr((ord(char) * int(key) -97)%26 + 97)
   return cipher


def decrypt(message):
   
    for i in range(26):
        key=i
        plain=''
        for char in message:
            if char=='':
                plain=plain+char
            else:
                plain=plain + chr((ord(char)* key )%26)
        print ("{}{}" .format( key , plain))
        


def display_multi():  
   print(app_name)
   print("please choose :")
   print("1-encrypt...")
   print("2-decrypt...")
   choosed = input()
   match choosed:
       case "1": print("please enter your message ") ; message=input(); print("please enter the key") ; key=input(); cipher=encrypt(message,key); print("CIPHER is :" +cipher)
       case "2": print("please enter your encrypted message :"); message=input(); plain=decrypt(message); print(plain)
