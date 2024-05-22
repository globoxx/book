preuves = []
vie = 2

def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

def debut_histoire():
    choix = poser_question("Voulez-vous découvrir le cadavre ou visiter la maison ?", ["découvrir le cadavre", "visiter la maison"])
    if choix == "visiter la maison":
        visiter_la_maison()
    elif choix == "découvrir le cadavre":
        decouvrir_le_cadavre()


def visiter_la_maison():
    choix = poser_question("Voulez-vous monter au premier étage ou rester au rez-de-chaussée ?", ["monter au premier étage", "rester au rez-de-chaussée"])
    if choix == "monter au premier étage":
        premier_etage()
    elif choix == "rester au rez-de-chaussée":
        rez_de_chaussee()
      
def premier_etage():      
    print("Vous suivez des traces de sang et vous trouvez des ciseaux dans la salle de bain. Vous les récupérez et les ajoutez aux preuves")
    preuves.append("les ciseaux")
    choix_3portes()
        
def rez_de_chaussee():
    choix = poser_question("Voulez-vous entrer dans la cuisine ou dans le salon ?", ["cuisine", "salon"])
    if choix == "cuisine":
        print("Vous entrez dans la cuisine.")
        decouvrir_le_cadavre()
    elif choix == "salon":
        print("Vous entrez dans le salon. Vous regardez une photo de famille. Le père coupe les cheveux du fils. Vous comprenez que le mari est l'assassin. Pour dénoncer le mari, vous avez besoin de preuves. Possédez-vous les ciseaux ?")
        if "les ciseaux" in preuves :
            print("Oui")
            end()
        else :
            print("Non. Vous allez au premier étage.")
            premier_etage()
            
def end():
    print("Vous appelez la police et il est arrêté. Il avoue, vous avez réussi votre mission. THE END")
    
def choix_3portes():  
    choix = poser_question("Vous êtes dans un couloir, face à 3 portes. Voulez-vous prendre celle de droite, de gauche, ou du milieu ?", ["droite", "gauche", "milieu"])
    if choix == "gauche":
        print("Vous arrivez dans la chambre du fils de la famille. Tout est normal. Vous ressortez.")
        choix_3portes()
    elif choix == "droite":
        print("Vous trouvez une chambre en désordre avec une fenêtre ouverte donnant sur un balcon. Vous trouvez un bout de tissu ensanglanté. Vous le récupérez et l'ajoutez aux preuves")
        preuves.append("le bout de tissu ensanglanté") 
        print("Vous décidez de visiter le rez-de-chaussée")
        rez_de_chaussee()
    elif choix == "milieu":
        global vie
        print("Vous arrivez dans le bureau où se trouve une pendule et une armoire.")
        choix = poser_question("Voulez-vous inspecter la pendule ou inspecter l'armoire ?", ["pendule", "armoire"])
        if choix == "pendule":
            print("En touchant la pendule, les aiguilles se mettent à tourner très rapidement. Le temps avance et la nuit tombe. Vous avez échoué, vous perdez une vie.")
            vie = vie - 1
            print(" Il vous reste", vie , "vie")
            if vie == 0:
                print("GAME OVER")
            else:
                print("Vous recommencez au début.")
                debut_histoire() 
        elif choix == "armoire":
            print("Vous tirez la porte et un couteau qui vous tombe dessus vous fend le crâne en deux. Vous perdez une vie.")
            vie = vie - 1
            print(" Il vous reste", vie , "vie")
            if vie == 0:
                print("GAME OVER")
            else:
                print("Vous recommencez au début.")
                debut_histoire()

def decouvrir_le_cadavre():
    global vie
    print("Vous trouvez le cadavre. Il s'agit d'une femme, elle a été poignardée dans la jambe, puis étranglée. Vous trouvez une écharpe rouge à côté d'elle. Puis, vous entendez son téléphone vibrer. Vous le sortez de sa poche. Vous découvrez son mari avec une écharpe rouge en fond d'écran. Vous comprenez que le mari est l'assassin. Pour le dénoncer, vous avez besoin de preuves. Possédez-vous le bout de tissu ensanglanté ?")
    if "le bout de tissu ensanglanté" in preuves :
            print("Oui")
            end()
    else :
        print("Non, vous perdez une vie.")
        vie = vie - 1 
        print(" Il vous reste", vie , "vie")
        if vie == 0:
            print("GAME OVER")
        elif vie == 1 :
            print("Vous recommencez au début.")
            debut_histoire()
            
   

print("Vous êtes un détective. Vous avez été appelé par la police pour résoudre un crime commis dans une maison. Trouvez l'assassin avant la tombée de la nuit. Vous avez 2 vies.")
debut_histoire()