inventaire = []
argent = 50


def evanouit():
    global argent
    print ("Vous vous êtes évanoui au milieu des cailloux et à votre réveil un martien vous propose d’aller chez lui.")
    reponse = input("Vous allez chez lui ?")
    while reponse not in ["oui","non"]:
        reponse = input("Vous allez chez lui ?")
        
    if reponse == "non" :
        print ("GAME OVER")
        exit ()
        
    elif reponse == "oui" :
        print ("Il vous propose de boire une potion rouge qui coute 30 pièces, violette ou verte.")
        boisson = input("Quelle couleur de potion voulez-vous boire ?")
        while boisson not in ["verte","rouge", "violette"]:
            boisson = input("Quelle couleur de potion voulez-vous boire ?")
        
                
        if boisson == "rouge" :
            prix = input ("Voulez-vous donner 30 pièce ?")
            while prix not in ["oui","non"]:
                prix = input ("Voulez-vous donner 30 pièce ?")
                
            if prix == "non" :
                print ("GAME OVER")
                exit ()
                    
            elif prix == "oui" :
                print ("Vous êtes en pleine forme et partez de chez le martien.")
                argent -= 30
                print ("Il vous reste", argent, "pièces.")
            
        elif boisson == "violette" :
            print ("Vous êtes en pleine forme et partez de chez le martien")

        elif boisson == "verte" :
            print ("C’était du poison, vous vous sentez très mal.")
            evanouit()
            
            
            
def atterrissage():
    print ("Vous atterrissez en douceur sur Mars.")
    print ("Vous voyez une bouteille remplie d’eau par terre.")
    reponse = input("Vous ramassez la bouteille ?")
    while reponse not in ["oui","non"]:
        reponse = input("Vous ramassez la bouteille ?")
            
    if reponse == "oui" :
        print ("Une bouteille d’eau est ajoutée à votre inventaire.")
        inventaire.append("bouteille d'eau")
                
        print ("Vous continuez à marcher et vous croisez un martien")
    
    elif reponse == "non" :
        print ("Vous continuez à marcher et vous croisez un martien")
    

def fin() :
    global argent
    print ("Le martien vous emmène à son village.")
    reponse = input("Il vous propose de prendre une de leur fusée. accepter ou refuser ?")
    while reponse not in ["accepter","refuser"]:
        reponse = input("Il vous propose de prendre une de leur fusée. accepter ou refuser ?")
    
    if reponse == "refuser" :
        print ("Vous êtes resté bloqué sur cette planète et les martiens vous dévorent.")
        print ("GAME OVER")
        
    elif reponse == "accepter" :
        print ("Vous avez", argent, "pièces.")
        reponse = input("Avez-vous 50 pièces pour acheter une fusée ?")
        while reponse not in ["oui","non"]:
            reponse = input("Avez-vous 50 pièces pour acheter une fusée ?")
        
        if reponse == "oui" :
            if argent >= 50 :
                print ("VICTOIRE, vous parvenez à rentrer chez vous avec la fusée et vous racontez votre histoire à tout le monde !!")
            
            elif argent < 50 :
                print ("Vous avez menti, car vous avez moins de 50 pièces. Le martien n'a pas apprécié votre mensonge et vous mange.")
                print ("GAME OVER")
            
        elif reponse == "non" :
            print ("Vous êtes resté bloqué sur cette planète et les martiens vous dévorent.")
            print ("GAME OVER")
            

def cascade() :
    print ("Vous suivez le martien et il vous emmène vers une cascade.")
    print ("Avez-vous de la crème solaire dans votre inventaire ?")
    if "crème solaire" in inventaire:
        print ("Vous avez bel et bien de la crême solaire alors")
        reponse = input ("voulez-vous vous baigner ?")
        while reponse not in ["oui","non"]:
            reponse = input ("voulez-vous vous baigner ?")
        
        if reponse == "oui" :
            print ("Le martien ne vous avait pas prévenu qu’il y avait des piranhas, vous vous faite dévorer.")
            print ("GAME OVER")
            
        elif reponse == "non" :
            fin()
            
    elif "crème solaire" not in inventaire:
        print ("Comme vous n'avez pas de crème solaire,")
        fin()
        
        
def debut():
    global argent
    print("La fusée a des problèmes")
        
    reponse = input("Inspecter la fusée?")
    while reponse not in["oui","non"]:
        reponse = input("Inspecter la fusée?")
            
    if reponse == "non":
        print("La fusée explose sans que vous puissiez vous en sortir")
        print("GAME OVER")
            
    if reponse == "oui":
        print("Vous decouvrez que un des moteurs ne fonctionne plus")
            
        reponse = input("Est-ce que vous vous fiez à vos 'talents de pilote', voulez vous chercher une boite a outils ou chercher a avoir du reseau?")
        while reponse not in ["talents de pilote","boite a outils","reseau"]:
            reponse = input("veuiller choisir une option ci dessous: talents de pilote ou boite a outils ou reseau")
            
        if reponse == "talents de pilote":
            print("Grace a votre parfaite maitrise de la fusée, vous parvenez a atterir sur Mars et marchez dans le desert")
                
        if reponse == "boite a outils":
            reponse = input("Vous trouvez une boite a outils, la prenez vous?")
            if reponse == "oui":
                print("Une boite a outils a ete ajoutee a votre inventaire")
                inventaire.append("boite a outils")
                print("Vous avez trouve 100 pieces")
                argent += 100
                print("Il vous reste",argent,"pieces")
            reponse = input("Voulez vous reparer le moteur?")
            if reponse =="non":
                print("Vous vous réveillez en sursaut d'un cauchermard et vous vous rendez compte que tout va bien")
                debut()
            if reponse =="oui":
                reponse = input("Avez vous une boite a outils?")
                if reponse =="oui":
                    print("Vous parvenez a reparer le moteur et atterrisez vite sur Mars et marchez seul.")
                if reponse =="non":
                    print("Vous vous reveillez en sursaut d'un cauchemard et vous vous rendez compte que tout va bien.")
                    debut()
                        
        while reponse == "reseau":
            print("Vous n'arrivez pas a avoir du reseau et votre telephone tombe en panne")
            print("Vous decouvrez que un des moteurs ne fonctionne plus. Recommencez. ")
            reponse = input("Est-ce que vous vous fiez à vos 'talents de pilote', voulez vous chercher une boite a outils ou chercher a avoir du reseau?")
            while reponse not in ["talents de pilote","boite a outils","reseau"]:
                reponse = input("veuiller choisir une option ci dessous: talents de pilote ou boite a outils ou reseau")
            
            if reponse == "talents de pilote":
                print("Grace a votre parfaite maitrise de la fusée, vous parvenez a atterir sur Mars et marchez dans le desert")
                
            if reponse == "boite a outils":
                reponse = input("Vous trouvez une boite a outils, la prenez vous?")
                if reponse == "oui":
                    print("Une boite a outils a ete ajputee a votre inventaire")
                    inventaire.append("boite a outils")
                    print("Vous avez trouve 100 pieces")
                    argent += 100
                    print("Il vous reste alors", argent, "pièces.")
                reponse = input("Voulez vous reparer le moteur?")
                if reponse == "non":
                    print("Vous vous réveillez en sursaut d'un cauchermard et vous vous rendez compte que tout va bien")
                    debut()
                if reponse =="oui":
                    reponse = input("Avez vous une boite a outils?")
                    if reponse=="oui":
                        print("Vous parvenez a reparer le moteur et atterrisez vite sur Mars et marchez seul.")
                    if reponse=="non":
                        print("Vous vous reveillez en sursaut d'un cauchemard et vous vous rendez compte que tout va bien.")
                        debut()
                    print("Vous parvenez a reparer le moteur et atterrisez vite sur Mars et marchez seul.")
            
        print("Vous avez continue a marcher et vous croisez un martien")
        cascade()



# Début de l'histoire
print("Vous êtes dans une fusée et vous avez 50 pièces sur vous.")

reponse = input("Voulez-vous prendre les commandes de la fusée?")
while reponse not in ["oui","non"]:
    reponse = input("Voulez-vous prendre les commandes de la fusée?")
    
if reponse == "oui":
    debut()
    

elif reponse == "non":
    print("Vous voyez Mars au loin")
    
    reponse = input("Activer le pilotage automatique pour atterir ?")
    while reponse not in ["oui","non"]:
        reponse = input("Activer le pilotage automatique pour atterir ?")
        
    if reponse == "non" :
        print("Vous êtes à court de carburant mais vous trouvez un parachute, une combinaison de cosmonaute et un drap.")
        reponse = input("Que choisissez vous de prendre ?")
        while reponse not in ["un parachute", "un drap", "une combinaison de cosmonaute"]:
            reponse = input("Que choisissez vous de prendre ?")
        
        if reponse == "une combinaison de cosmonaute" :
            print ("GAME OVER")
            
        elif reponse == "un drap" :
            print ("Vous avez bien atterri sur Mars, mais vous êtes gravement blessé.")
            evanouit()
            
            print ("Après 3 longues heures de marche, vous voyez un tube de crème solaire sur le sol.")
            reponse = input("Voulez-vous le prendre ?")
            while reponse not in ["oui","non"]:
                reponse = input("Voulez-vous le prendre ?")
                
            if reponse == "oui" :
                print ("Le tube de crème solaire est ajouté à votre inventaire.")
                inventaire.append("crème solaire")
                
                print ("Vous continuez à marcher et vous croisez un martien")
                cascade()
                
            elif reponse == "non" :
                print ("Vous continuez à marcher et vous croisez un martien")
                cascade()
                
        elif reponse == "un parachute" :
            atterrissage()
            cascade()
                
            
    elif reponse == "oui" :
        atterrissage()
        cascade()