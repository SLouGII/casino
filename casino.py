import random
import time
nombre = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]


print("Bien venu dans le casino vous avez une chance sur 10 de gagner!")

while True:
    choise = random.choice(nombre)
 

    reponse = input("Quelle nombre veut tu choisirs ? :")


    if int(reponse) == int(choise):
        print("Bien jouer tu gagnes rien!")
        time.sleep(1)
    else:
        print("tu as perdu!")
        time.sleep(1)
        
    reponse2 = input("Voulez-vous continuer? (oui/non)")
    if (reponse2) == "non":
        print("au revoir!")
        break 

    
    
    


