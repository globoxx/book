inventaire = []
oxygene = 100

def navette():
    global oxygene
    print("vous vous réveillez dans une navette spatiale seul.e, personne ne commande")

    reponse = input("prendre les commandes? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("prendre les commandes? (o/n)")
        
    if reponse == "o" :
        print("vous échappez la catastrophe, mais crachez dans une coline")
    elif reponse == "n" :
        print("vous venez de crasher dans une étendue de liquide non identifié")

    reponse = input("sortir et explorer où vous avez atteri ? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("sortir et explorer où vous avez atteri ? (o/n)")
    if reponse == "o" :
        print("vous perdez tout votre oxygène")
        oxygene = oxygene-100
        print(oxygene)
        print("vous mourrez")
        navette()
    elif reponse == "n" :
        print("vous trouvez un kit de survie,")
        

    reponse = input("rammaser? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("rammaser? (o/n)")
    if reponse == "o" :
        inventaire.append("kit de survie")
        print(inventaire)
        sortie()  
    elif reponse == "n" :
        dans_le_vaisseau()
        
def dans_le_vaisseau():
    print("vous continuez à chercher à l'intérieur de votre vaisseau spatial")
    print("vous trouvez une notice d'information concernant le vaisseau")
    
    reponse = input("rammaser? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("rammaser? (o/n)")
    if reponse == "o" :
        reponse = input("lire? (o/n)")
        while reponse not in ["o", "n"]:
            print("pas de reopnse valable")
            reponse = input("lire? (o/n)")
        if reponse == "o" :
            print("vous pouvez réparer le vaisseau et rentrer!")  
        elif reponse == "n" :
            print("vous avez une notice d'information du vaisseau")
            inventaire.append("notice d'information")
            print(inventaire)
            encore_le_vaisseau() 
    elif reponse == "n" :
        encore_le_vaisseau()
    
def encore_le_vaisseau():
    print("vous continuez à chercher à l'intérieur de votre vaisseau spatial")
    print("un débris vous tombe dessus, vous etes blessé")
    if "kit de survie" in inventaire:
        print("vous vous en remettez grâce aux soins procurés avec le kit de survie")
    else:
        print("vous mourrez de cette blessure mortelle")
    print("en continuant à chercher vous trouvez un numéro d'urgence")
    reponse = input("appeler? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("appeler? (o/n)")
    if reponse == "o" :
        print("des secours viennent de suite pour vous sauver")  
    elif reponse == "n" :
        print("vous avez plus assez de vivre et mourrez au bout de 2 jours")
def sortie():
    global oxygene
    print("vous avez + 50 d'oxygène et un kit de survie")
    oxygene = oxygene + 50
    print(oxygene)
    reponse = input("sortir et explorer maintenant équipé?? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("sortir et explorer maintenant équipé?? (o/n)")
    if reponse == "o" :
        print("vous voyez une hutte")
        reponse = input("aller vers elle et entrer? (o/n)")
        while reponse not in ["o", "n"]:
            print("pas de reopnse valable")
            reponse = input("aller vers elle et entrer? (o/n)")
        if reponse == "o" :
            dans_la_maison()  
        elif reponse == "n" :
            dehors()
    elif reponse == "n" :
        dans_le_vaisseau()

def dehors():
    print("vous errez dans la zone de crash, et voyez un point qui bouge")
    reponse = input("aller vers lui? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("aller vers lui? (o/n)")
    if reponse == "o" :
        print("cet extraterrestre vous troue votre combinaison")
        print("vous perdez 200 oxygène peu à peu")
        print("vous mourrez")
    elif reponse == "n" :
        print("vous continuez à errez et trouvez une corde")
        reponse = input("rammaser? (o/n)")
        while reponse not in ["o", "n"]:
            print("pas de reopnse valable")
            reponse = input("rammaser? (o/n)")
        if reponse == "o" :
            print("vous avez une corde")
            inventaire.append("corde")
            print(inventaire)
            trou()
        elif reponse == "n" :
            trou()
            
def trou():
    print("vous continuez à errer et tombez dans un trou, avez vous une corde?")
    if "corde" in inventaire:
        print("vous pouvez remonter du trou ")
        print("une main est tendue vers vous")
        reponse = input("prendre la main? (o/n)")
        while reponse not in ["o", "n"]:
            print("pas de reopnse valable")
            reponse = input("prendre la main? (o/n)")
        if reponse == "o" :
            print("ce sont les secours, vous pouvez rentrer!")  
        elif reponse == "n" :
            print("vous retombez dans le trou et mourrez sur l'impact")
    else:
        print("vous mourrez dans ce trou trop profond pour remonter")

def dans_la_maison():
    global oxygene
    print("vous trouvez des réserves d'oxygène")
    reponse = input("rammaser? (o/n)")
    while reponse not in ["o", "n"]:
        print("pas de reopnse valable")
        reponse = input("rammaser? (o/n)")
    if reponse == "o" :
        print("vous avez gagner +50 d'oxygene")
        oxygene = oxygene + 50
        print(oxygene)
        print("une radio inter-stéllaire est posée sur le comptoir")
        reponse = input("appeler les secours? (o/n)")
        while reponse not in ["o", "n"]:
            print("pas de reopnse valable")
            reponse = input("appeler les secours? (o/n)")
        if reponse == "o" :
            print("la station spatiale la plus proche vous propose de venir vous rejoindre pour vous sauver")
        elif reponse == "n" :
            print("vous montez et voyez une jeune femme ligotée")
            reponse = input("l'aider? (o/n)")
            while reponse not in ["o", "n"]:
                print("pas de reopnse valable")
                reponse = input("l'aider? (o/n)")
            if reponse == "o" :
                print("une fois libérée, elle vous dit qu'elle sait comment partir de cette planète")
            elif reponse == "n" :
                print("vous sortez de la maison, mais la nuit s'est levée")
                reponse = input("passer la nuit? (o/n)")
            while reponse not in ["o", "n"]:
                print("pas de reopnse valable")
                reponse = input("passer la nuit? (o/n)")
            if reponse == "o" :
                print("le lendemain est venue une équipe spéciale pour vous chercher et pouvez rentrer ")
            elif reponse == "n" :
                print("vous mourrez de froid dehors")

    elif reponse == "n" :
        print("vous perdez 200 d'oxygène")
        oxygene = oxygene - 200
        print(oxygene)
        print("vous mourrez")
    
navette()
