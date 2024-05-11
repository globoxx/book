def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

inventaire = []
argent = 0 

def entrer_plage():
    print("Vous êtes à la plage.")
    print("Vous trouvez une canne à pêche")
    choix = poser_question("Rammasser la canne à pêche ?",["Oui","Non"])
    if choix == "Oui":
        print("La canne à pêche est ajoutée a votre inventaire")
        inventaire.append("canne à pêche")
        print(inventaire)
        print("Vous montez dans un bateau")

    elif choix == "Non":
        print("Vous montez dans un bateau")
        
entrer_plage()

def entrer_bateau():
    global argent
    print("Vous trouvez 50CHF")
    choix = poser_question("Rammasser les 50CHF?", ["Oui","Non"])
    if choix == "Oui":
        print("Les 50CHF sont ajouter a votre portefeuille.")
        argent += 50
        print("argent =", argent)
        
    elif choix == "Non":
        print("Vous ne pouvez pas acheter de la nourriture, vous mourrez de faim.")
        
entrer_bateau()

if "canne à pêche" in inventaire:
    choix = poser_question("Achetez un hameçon?",["Oui","Non"])
    if choix == "Oui":
        print("L'hameçon est ajouté a votre inventaire")
        inventaire.append("Hameçon")
        print(inventaire)
        
    elif choix == "Non":
        print("Vous ne pouvez pas pêcher, vous mourrez de faim")
        
else:
    print("Vous n'avez pas de canne à pêche, je vous redonne une chance d'en avoir une")
    entrer_plage()
    entrer_bateau()
    
choix = poser_question("Voulez vous pêcher?" ,["Oui","Non"])
if choix == "Oui":
    print("Vous attrapez un poisson")
    print("Le poisson est ajouté a votre inventaire")
    inventaire.append("poisson")
    print(inventaire)
    print("Vous mangez et ne mourrez pas de faim")
    print("Vous trouver une epée")
    choix = poser_question("Voulez vous rammassez l'epée?",["Oui","Non"])
    if choix == "Oui":
        print("Vous croisez un requin et gagnez")
    elif choix == "Non":
        print("Vous mourrez sans defense face a un requin")

elif choix == "Non":
    print("Vous êtes mort de faim")
    

