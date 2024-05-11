def fruit_fluorescent():
    global energie 
    print("Vous trouvez un fruit fluorescent")
    reponse = input("Prendre le fruit ?")
    if reponse == "oui":
        inventaire.append("fruit fluorescent")
        print("Vous continuez votre chemin et après 3 heures de marche vous avez faim")
    elif reponse == "non":
        print("Vous continuez votre chemin et après 3 heures de marche vous avez faim")
    if "fruit fluorescent" in inventaire:
        print("Vous mangez le fruit, il était empoisonné, et mourrez tout les deux")
        print("Game Over !")
    if "fruit fluorescent" not in inventaire:
        print("Votre état de santé se dégrade car vous n'avez rien mangé")
        print("Vous perdez 50 d'énergie")
        energie = energie - 50  
        if energie == 0:
            print("Votre énergie est de 0, car vous vous êtes battus contre le gorille avant, donc vous mourrez")
            print("Game Over !")
        elif energie == 50:
            print("Votre energie est de 50, car vous ne vous êtes pas battus contre le gorille") 

def bois():
    print("Vous continuez de marcher et vous trouvez du bois")
    reponse = input("Prendre le bois ?")        
    if reponse == "oui":
        inventaire.append("bois")
        print("Vous voyez un bateau au loin et décidez de faire un feu")
    elif reponse == "non":
        print("Vous voyez un bateau au loin et décidez de faire un feu")
    if "bois" in inventaire: 
        print("Vous réussissez à faire un feu, le bateau vous remarque et vient vous secourir")
        print("Victoire !")
    if "bois" not in inventaire:
        print("Vous ne pouvez donc pas faire de feu et mourrez sur l'île")
        print("Game Over !") 
          
energie = 100
inventaire = []
print ("Votre avion s'est crashé sur une ile déserte, vous avez 100 d'énergie et un briquet dans l'inventaire")
inventaire.append("briquet")
print ("Vous cherchez des survivants et trouvez un homme blessé")    
reponse = input("Vous l'aidez ou vous le laissez mourir ?")
if reponse == "l'aider":
    print("Vous le soignez et partez à deux explorer la forêt")      
    fruit_fluorescent()    
if energie == 50:    
    bois()
       
elif reponse == "le laisser mourir":
    print("Vous partez explorer la forêt seul")
    print("Vous trouvez une machette")
    reponse = input("Prendre la machette ?") 
    if reponse == "oui":
        inventaire.append("machette")
        print("Vous tombez face à face avec un gorille")
    elif reponse == "non":
        print("Vous tombez face à face avec un gorille")
    if "machette" in inventaire:
        print("Vous réussissez à battre le gorille grâce à la machette")
        bois()
    if "machette" not in inventaire:
        print("Le gorille vous assomme avec son coup de poing et perdez 50 d'énergie")
        energie = energie - 50 
        fruit_fluorescent()
