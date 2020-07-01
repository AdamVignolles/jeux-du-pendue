import random
import os
import time

choix_mot = [
    "chien",
    "chat",
    "souris",
    "cheval",
    "mulo",
    "chevre",
    "mouton",
    "dindon"
]

print("Bienvenue dans le jeux du Pendue")
print("1: 2 joueur\n2:IA")
choix = input()

if choix == "1":
    print("choisie le mot a deviner:")
    mot = input("")
    
elif choix =="2":
    print("un mot a ete choisi deviner le")
    print("le mot est sur le theme des animaux")
    
    mot = random.choice(choix_mot)
    
os.system("clear")
all_letre = []
letre_cacher = []
for letres in mot:
    letre_s = letres.replace(letres, "_")
    letre_cacher.append(letre_s)
    all_letre.append(letres)
time.sleep(1)


print("votre mot a bien ete enregistrer")
print("\n")

conteur = 0

run = True
while run:
    for i in letre_cacher:
        print(i, end=" ")
    print("\n")
    letre = input("donner une letre:")
    print("\n")
    for i in range(len(all_letre)):
        
        if letre not in all_letre:
            
            conteur = conteur +1
            
            if conteur == 10:
                print("_______")
                print("|      |")
                print("|      ⚫")
                print("|     >|<")
                print("|      ^")
                print("|____\n")
                print("Game over")
                print(f"Le mot etais:{mot}")
                run = False
                
            elif conteur == 1:
                print("___")
                
                print("Perdue essai encore")
                break
                
            elif conteur == 2:
                print("|")
                print("|")
                print("|____")
                
                print("Perdue essai encore")
                break
                
             
            elif conteur == 3:
                print("|")
                print("|")
                print("|")
                print("|")
                print("|___")
                
                print("Perdue essai encore")
                break
                
            elif conteur == 4:
                print("_______")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|___")
                
                print("Perdue essai encore")
                break
                
            elif conteur == 5:
                print("_______")
                print("|      |")
                print("|")
                print("|")
                print("|")
                print("|___")
                
                print("Perdue essai encore")
                break
                 
            elif conteur == 6:
                print("_______")
                print("|      |")
                print("|      ⚫")
                print("|")
                print("|")
                print("|___")
                
                print("Perdue essai encore")
                break
                
            elif conteur == 7:
                print("_______")
                print("|      |")
                print("|      ⚫")
                print("|      |")
                print("|")
                print("|___")
                
                print("Perdue essai encore")
                break
                
            elif conteur == 8:
                print("_______")
                print("|      |")
                print("|      ⚫")
                print("|      |")
                print("|      ^")
                print("|___")
                
                print("Perdue essai encore")
                break
                
            elif conteur == 9:
                print("_______")
                print("|      |")
                print("|      ⚫")
                print("|      |<")
                print("|      ^")
                print("|___")
                
                print("Perdue essai encore")
                break
                 
            
        
        elif letre in all_letre[i]:
            letre_cacher[i] = letre
            for i in letre_cacher:
                print(i, end=" ")
            print("\n")
            
            if letre in all_letre:
                if all_letre == letre_cacher:
                    print("Gangné")
                    run = False
                else:  
                    print("\nbien jouer\n")
                    os.system("clear")