print("Vous marchez dans une foret mais tout d'un coup un ours veut vous deguster.")
vie = 10
inventaire = []

reponse = input("Voulez-vous donner un nom à votre héro ? ")

if reponse == "oui":
    print("Pas le choix, elle s appellera Pupuce.")

elif reponse == "non":
    print("pas le choix, elle s appellera Pupuce.")
    
else:
    print("pas le choix, elle s appellera Pupuce.")

print("Durant votre fuite, vous apercevez au loin deux cabanes. Une en bois, l autre en pierre.")

reponse = input("ou allez-vous?")

if reponse == "cabane en bois":
    print("Vous trouvez une clé sur une table.")

    reponse = input("Ramasser la clé ?")
    while reponse != "oui":
        reponse = input("Ramasser la clé ?")
        inventaire.append("clé")
    
    print("En sortant de la cabane, vous apercevez un animal sortir de la cabane en pierre.")

elif reponse == "cabane en pierre":
    print("Vous trouvez une épée dans un coffre.")

    reponse = input("Ramasser l'épée ?")
    if reponse == "oui":
        inventaire.append("épée")
        print("En sortant de la cabane, vous apercevez un animal sortir de la cabane en bois.")

print("en continuant votre chemin, vous tombez sur Chipeur le renard Malicieux, et il veut vous attaquer!")
if "épée" in inventaire:
    print("Vous affrontez Chipeur et finissez par le tuer. Vous trouvez une clé sur son cadavre et la ramassez.")
    inventaire.append("clé")
    

elif "clé" in inventaire:
    print("Oh mince ! Chipeur vous a blessé avec son épée! Votre vie diminue de 5.") 
    vie = vie - 5

print("Vous continuez votre chemin, jusqu'à arriver à une grotte.")

reponse = input("Entrer dans la grotte ? ")

while reponse != "oui":
    reponse = input("Entrer dans la grotte ?")

print("Vous pénétrez dans la grotte, et apercevez une grande porte verouillée.")
print("Vous déverouillez la porte et arrivez dans la suite de la grotte.")
print("Soudain, un monstre surgit de lobscurité. C'est le démon Ratata, Il est très agressif, et veut vous attaquer!")

reponse = input("Que choisissez-vous ? La fuite, ou l'affrontement pacifique ?")
    
if reponse == "la fuite":
        print("Vous décidez de partir le plus vite possible! Vous sortez de la grotte, et essayez de retrouver votre chemin.")
        if vie < 10:
            print("Malheureusement, vous n'avez plus de force suite à votre combat contre Chipeur. Vous mourrez à cause de vos blessures. Game Over ! ")
        if vie >= 10:
            print("Malheureusement, vous avez oublié qu'un ours vous poursuivait. Il vous trempe dans du miel et vous mange. Dommage! Game Over...")

elif reponse == "l'affrontement pacifique":
    print("Vous tendez votre bras droit, la paume vers Ratata, et déclarez solenellement: 'Parle à ma main !' Ratata prit la fuite, apeuré.")
    print("Vous continuez d'explorer, et finissez par trouver un coffre avec beaucoup d'argent. Avec ce bénéfice, vous appelez un taxi pour rentrer chez vous. Bravo! Vous voilà saine et sauve, avec des traumas. Vous avez gagné (un suivi psychologique)!")
        











