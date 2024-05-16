def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse
inventaire = []


def alien_ciel():
    choix = poser_question("vous etes dans le ciel. Droite ou gauche ?" , ["droite" , "gauche"])
    if choix == "droite":
        aller_droite()
    elif choix == "gauche":
        aller_gauche()

def aller_droite():
    print ("tu commences le voyage en somalie.")
    print ("tu tombes sur des dizaines de kg d'or")
    choix = poser_question("voler ce trésor ?" , ["oui" , "non"])
    if choix == "oui":
        print ("le trésor contenait des explosifs!! tu es mort.")
        exit()
    
    elif choix == "non":
        print ("tu prend lavion direction les USA")
        print ("arrivé là bas, tu vois un homme tirer sur une tornade")
        print ("désespéré du niveau d'intelligence, tu repars dans le ciel.")
        alien_ciel()
def aller_gauche():
    print ("tu commences le voyage en Tunisie")
    choix = poser_question("Sortir du pays ou y rester ?" , ["sortir" , "rester"])
    if choix == "rester":
        print ("tu te fais attraper par des terroristes qui te tortureront jusqu'à la mort")
        exit()
        
    elif choix == "sortir":
        print("tu sautes dans le premier bateau et tu te retrouves au Japon")
        print("tu tombes nez à nez avec un yakuza")
        choix = poser_question("Essayer de faire amis amis ou fuir ?" , ["amis" , "fuir"])
        if choix == "amis":
            print("il etait très gentil et tu decides de le mettre dans ton sac comme compagnon")
            inventaire.append("yakuza sauvage")
                 
        elif choix == "fuir":
            print ("Durant ta fuite tu tombes sur la réserve des trésors nationaux mondiaux")
            choix = poser_question("tu prends quoi ?" , ["rien" , "katana de Nobunaga" , "le corps du Pharaon" , "une ps1" , "le cheval de troie" , "un tajine kefta"])
            if choix == "rien":
                print("après quelques années, tu finis le tour du monde et tu es l'alien le plus heureux du monde. victory!!")
            elif choix == "le katana de Nobunaga":
                print("le katana te donnes un pouvoir spécial. Il est mit dans l'inventaire.")
                inventaire.append("le katana de Nobunaga")
                print ("vous sortez de la réserve des tresors nationaux.")
                
            elif choix =="le corps du Pharaon":
                print("l'odeur est trop forte pour tes narines surdéveloppées. tu meurs !!")
                exit()
            
            elif choix =="une ps1":
                print("l'objet est scintillant. l'objet te fait sentir nostalgique alors que tu le vois pour la first time")
                inventaire.append("une ps1")
                print ("vous sortez de la réserve des tresors nationaux.")
                
            elif choix =="le cheval de troie":
                print("l'objet est trop gros pour rentrer dans l'inventaire.")
                choix = poser_question("prendre le risque de le mettre dans l'inventaire ?" , ["oui" , "non"])
                if choix == "oui":
                    print("l'objet est trop gros et casse l'inventaire. tu as tout perdu, tu meurs de tristesse.")
                    exit()
                elif choix == "non":
                    print ("vous sortez de la réserve des tresors nationaux.")
                    
              
         
            elif choix =="un tajine kefta":
                choix = reponse_question("tu veux le manger ?" , ["oui" , "non"])
                if choix =="oui":
                    print("suite à l'explosion de saveurs dans votre bouche, vous mourrez.")
                    exit()
                elif choix =="non":
                   choix = reponse_question("tajine dans l'inventaire ?" , ["oui" , "non"])
                   if choix =="oui":
                       print("grace à l'odeur qui émane de votre inventaire, vous attirez maintenant tous les marocains.")
                       print ("vous sortez de la réserve des tresors nationaux.")
                   elif choix =="non":
                       print ("vous sortez de la réserve des tresors nationaux.")
        
    
    

print("vous êtes un alien et vous decidez de visiter la terre")
alien_ciel()