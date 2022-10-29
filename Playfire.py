from termcolor import colored
import pyfiglet
crp_alg="playfire"
app_name=colored(pyfiglet.figlet_format("CrypZ3nun - "+crp_alg),'green')



def doplaintext (plainText):
# append X if Two letters are being repeated
    for s in range(0,len(plainText)+1,2):
        if s<len(plainText)-1:
           if plainText[s]==plainText[s+1]:
             plainText=plainText[:s+1]+'x'+plainText[s+1:]
    if len(plainText)%2 != 0:
        plainText = plainText[:]+'x'
    return plainText

##################################################
def key_gen ():
    key_5x5 = [['l','g','d','b','a'],
    ['q','m','h','e','c'],
    ['u','r','n','i','f'],
    ['x','v','s','o','k'],
    ['z','y','w','t','p']]
    return key_5x5
##################################################
def encrypt(text):
    message = doplaintext(text)
    k = key_gen()
    message.replace("j","i")
    cipher=''
    for m in range(0, len(message)- 1, 2):
        for i in range(5):
            for j in range(5):
                if message[m] == k[i][j]:
                   i1=i
                   j1=j
                   if message[m+1] == k[i][j]:
                      i2=i
                      j2=j
                      if i1==i2:
                        if j1 != 4:
                            cipher=cipher+k[i1][j1+1]
                        else:
                            cipher=cipher+k[i1][0]
                        if j2!=4:
                          cipher=cipher+k[i2][j2+1]
                        else:
                          cipher=cipher+k[i2][0]
                      if j1==j2:
                        if i1 != 4:
                           cipher=cipher+k[i1+1][j1]
                        else:
                           cipher=cipher+k[0][j1]
                        if i2!=4:
                           cipher=cipher+k[i2+1][j2]
                        else:
                           cipher=cipher+k[0][j2]
                        if i1 != i2 and j1 != j2:
                          cipher=cipher+k[i1][j2]
                          cipher=cipher+k[i2][j1]
                          return cipher    







def display_Playfire():
   print(app_name)
   print("please choose :")
   print("1-encrypt...")
   print("2-decrypt...")
   choosed = input()
   match choosed:
       case "1": print("please enter your message ") ; message=input();  cipher=encrypt(message); print("CIPHER is :" +cipher)
       case "2": print("please enter your encrypted message :"); message=input(); plain=decrypt(message); print(plain)
 

