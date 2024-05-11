def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

def entrer_deuxMaison():
    global vie
    print ("Vous voyez deux maisons")
    
    choix = poser_question("Aller dans la maison bleu ou dans la maison en ruine ?", ["la maison bleu", "la maison en ruine"])
    if choix == "la maison bleu":
        print ("Vous trouvez un pompe chasseur")           
        choix = poser_question("Voulez vous le prendre", ["oui", "non"])
        if choix == "oui":
            inventaire.append("pompe chasseur")
    elif choix == "la maison en ruine":     
        print ("Vous trouvez un champignon qui vous donne +5 de vie ")
        vie = vie + 5
        
    choix = poser_question("Vous vous cacher pour le reste de la partie ou vous partez à la recherche d'ennemis ?", ["se cacher", "partir a la recherche d'ennemis"])  
    if choix == "se cacher":
        print ("Vous vous cachez dans une cabane")
        
    

inventaire = []
vie = 100

print("Vous êtes dans un bus d'un battle royal.")
choix = poser_question("Oû voulez vous spawn ?", ["Oulens sous échallens", "Salty springs"])
if choix == "Oulens sous échallens":
    print("Vous arrivez chez Arda !")
        
    print("Vous trouvez un coffre.")
    choix = poser_question("Vous voulez ?", ["Ouvrir le coffre !", "Ne pas l'ouvrir !"])
    if choix == "Ouvrir le coffre !":
        print("Le père de Arda vous étouffe avec un kebab legandaire. GAME OVER !!!!!!")
        exit ()
        
    elif choix == "Ne pas l'ouvrir !":
        print("Le père de Arda vous acceuil et vous donne un kebab (votre vie augmente de +10).")
        vie = vie + 10
        print("Puis une squad arrive sur vous alors vous fuyez.")
        print("Vous voyez deux maisons.")
        entrer_deuxMaison()

elif choix == "Salty springs":
    entrer_deuxMaison()
    
print ("Vous partez vous balader et trouvez Yassine El Tunzi prime qui se cache dans un buisson")





print("Avez vous un fusil a pompes?.")
choix = poser_question("oui ou non ?", ["oui", "non"])
if choix == "non":
    print("Yassine vous met une balle de cal.50 et vous mourrez !")
    exit()


elif choix == "oui":
    print("vous  survivez et tuer le Yassine sauvage.")
    print("Vous vous cachez dans une cabane.")
    
    print("Alexandra Prime arrive et vous inflige 100 de vie.")
    vie = vie -100
    print("vie")
    
print("Il vous reste de la vie?")
choix = poser_question("Oui ou Non ?", ["Oui", "Non"])
if choix == "Oui":
    print("Vous lui mettez - 200 de vie grâce à votre pompe !")
    print("Top #1 VICTOIRE ROYAL")

    
