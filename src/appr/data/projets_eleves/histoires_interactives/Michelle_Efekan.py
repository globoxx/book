print ("vous êtes perdu et affamé dans une grotte, votre vie est à 20")
vie = 20
print ("vous avez deux chemins différents")

def start():
    reponse = input ("gauche ou droite?")
    while reponse not in ["gauche","droite"]:
        reponse = input (" gauche ou droite?")
    if reponse == "gauche" :
        gauche()
    elif reponse == "droite" :
        droite()







def gauche():
    global vie
    print ("vous tombez sur un lapin, vous le manger. Votre vie augmente de 30")
    vie = vie + 30
    print ("vous trouvez une pièce particulière,vous réveillez un ours")
    
    reponse = input ("avez vous une épée? (oui/non)")
    while reponse not in ["oui","non"]:
        reponse = input ("avez vous une épée? (oui/non)")
    
    if reponse == "non" :
        print ("l'ours vous dévore")
        print ("Game over!")
    elif reponse == "oui" :
        print (" vous arrivez à la fin et voyez de la lumière par un trou")
        
        reponse = input ("faire demi-tour ou explorer?")
        while reponse not in ["faire demi-tour","explorer"]: 
            reponse = input ("faire demi-tour ou explorer?")
        
        if reponse == "faire demi-tour":
            start()
        elif reponse == "explorer" :
            print (" à travers le trou vous voyez plein de pièces d'or et bijoux")
            reponse = input (" avez vous une pioche dans l'inventaire?")
            while reponse not in ["oui","non"]:
                reponse = input (" avez vous une pioche dans l'inventaire?") 
        
        if reponse == "non" :
            start()
        elif reponse == "oui" :
            print (" vous atteignez l'or. Vous perdez de vie par fatigue")
            print("Victoire!")

def droite():
    global vie
    print ("vous vous dirigez vers la pièce la plus sombre, vous tombez sur un canibal")
    
    reponse = input (" avez vous un couteau dans votre sac? (oui/non)")
    while reponse not in ["oui","non"]:
        reponse = input (" avez vous un couteau dans votre sac? (oui/non)")
    
    if reponse == "non" :
        print ("malgré le combat, il fini par vous manger")
        print ("Game over")
    
    elif reponse == "oui" :
        print (" vous arrivez à vous en débarrasser et continuez avec moins 10 de vie par coup recus")
        vie = vie - 10
        print ("vous tombez sur une petite statue magique en forme de hibou")
        print (" vous voulez le prendre, mais vous devez le remplacer par un autre objet du même poids")
        
        reponse = input ("avez vous un objet du même poids? (oui/non)")
        while reponse not in ["oui","non"]:
            reponse = input ("avez vous un objet du même poids? (oui/non)")

        
        if reponse == "non" :
            print ("vous repartez sans l'objet qui vaut une fortune")
            start()
        elif reponse == "oui" :
            print ("vous faites l'échange, mais vous n'avez pas bien estimer le poids, vous mourrez par des flèches sorties du mur")
            print ("Game over!")

start()