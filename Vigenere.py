from ast import keyword
from termcolor import colored
import pyfiglet
crp_alg="Vigenere"
app_name=colored(pyfiglet.figlet_format("CrypZ3nun - "+crp_alg),'green')

def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 
def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None 
  else: 
    return x % m 
 
def encrypt(text, key): 
  return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 
def decrypt(cipher, key): 
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 



def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryptionVigenere(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = ((ord(string[i]) +ord(key[i])) % 26)
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 
def decryptionVigenere(encrypt_text, key): 
  orig_text = [] 
  for i in range(0,len(encrypt_text)): 
    x = ((ord(encrypt_text[i]) -ord(key[i])) % 26)
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 


def display_vigenere():  
   print(app_name)
   print("please choose :")
   print("1-encrypt...")
   print("2-decrypt...")
   choosed = input()
   match choosed:
       case "1": print("please enter your message ") ; message=input(); print("please enter the key") ; key=input(); keyword=generateKey(message,key);cipher=encryptionVigenere(message,keyword); print("CIPHER is :" +cipher)
       case "2": print("please enter your encrypted message :"); message=input(); print("please enter the key") ; key=input(); keyword=generateKey(message,key);plain=decryptionVigenere(message,key); print(plain)
