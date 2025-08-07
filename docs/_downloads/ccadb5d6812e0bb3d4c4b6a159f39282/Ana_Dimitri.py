
pv=50
inventaire= []

def robot():
    print("Un robot pirate vous kidnappe dans la rue")

    if "abonnement futuriste" in inventaire:
        print("Vous appelez votre cousin, super héro qui vient vous sauver")
        print("Victoire")
    else:
        print("Malheureusement vous ne l'avez pas et le robot pirate vous tue")
        print("Game over")

def vaisseau():
    global pv
    print("vous êtes le gardien du temps et vous vous amusez à voyager a travers les époques!")
    choix = input("Voulez vous allez dans le futur ou le passé?")
    if choix == "passé":
        print("Vous arrivez lors de la chute de Constentinople et le peuple se fait attaquer")
        choix = input("Voulez vous empêcher l'attaque?")
        if choix == "oui":
            print("le peuple vous offre une clé temporelle très rare")
            inventaire.append("clé temporelle")

        print("Une bande ennemie vous attaque")
        choix = input("Acceptez-vous le combat?")
        if choix == "oui":
            print("Game Over")
        elif choix == "non":
            print("Vous trouvez une cachette mais vous avez très peu de temps pour trouver une solution")
            print("Possédez-vous la clé temporelle?")
            if "clé temporelle" in inventaire:
                print("Vous arrivez à vous téléportez chez vous")
                print("Victoire")
            else:
                print("Malheuresement vous ne l'avez pas")
                print("Vous arrivez à retrouver votre vaisseau en ayant perdu 30pv")
                pv = pv - 30
                vaisseau()

    elif choix == "futur":
        print("Vous atterissez sur Mars, dans une ville futuriste ou l'IA a pris le dessus")
        choix = input("Voulez-vous installer ChatGPT sur votre montre connecté?")
        if choix == "oui":
            print("La police vous arrête car ils sont les seuls à pouvoir utilisez ChatGpt et vous enlève 20pv")
            pv = pv - 20
            if pv == 0:
                print("Game over")
            else:
                robot()
        elif choix == "non":
            print("Les robots vous offrent un abonnement futuriste")
            inventaire.append("abonnement futuriste")
            robot()




vaisseau()







