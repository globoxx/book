import time


argent = 100
vie = 100
possibilite_refus = 1
inventaire = []




#________________________________________________________________________________


def perte():
    print("GAME OVER!")
    exit()



def poser_question(question, choix):
    reponse = input(question + str(choix))
    while reponse not in choix:
        reponse = input(question + str(choix))
    return reponse


    
#_______________________________________________________________________    




def intro(inventaire):
    print("Vous êtes un(e) archéologue débutante. Cela fait quelques mois que vous n'avez rien découvert et votre chef de recherche vous menace de vous virer si vous ne trouvez rien dans la semaine. ")
    print("Avant de partir, vous remarquez une barre protéinée et une lampe torche.")
    reponse = poser_question("Que voulez-vous prendre?", ["la lampe torche", "la barre protéinée", "les deux","rien"])
    if reponse == "la barre protéinée":
        inventaire.append("barre protéinée")
    elif reponse == "la lampe torche":
        inventaire.append("lampe torche")
    elif reponse == "les deux":
        inventaire.append("barre protéinée")
        inventaire.append("lampe torche")
    print("Vous vous mettez en recherche de ruines à explorer lorsque vous tombez sur une grotte.")
    return inventaire








def debut_exploration(possibilite_refus):
    reponse = poser_question("Voulez-vous entrer dans la grotte?", ["oui","non"])
    if reponse == "oui" or possibilite_refus == 0:
        if possibilite_refus == 0 and reponse == "non":
            print("Vous vous sentez forcé à entrer.")
        print("Vous entrez dans la grotte et débutez votre exploration. La grotte semble remplie de gravures ni naturelles ni animales. Curieux, vous continuez d'avancer et, après une demi-heure d'exploration vous tombez sur un piédestal antique avec une relique ancienne dessus. Elle vous permettra sûrement à satisfaire votre patron.")
        reponse = poser_question("Voulez-vous prendre la relique?",["oui","non"])
        if reponse == "oui" or possibilite_refus == 0:
            if possibilite_refus == 0 and reponse == "non":
                print("Vous vous sentez obligé à la prendre")
            print("Vous prenez la relique")
            inventaire.append("relique")
        
    
            



def deuxieme_chance(possibilite_refus):
    if possibilite_refus > 0:
        print("Votre chef de recherche vous licensie à cause de votre inutilité dans l'équipe.")
        reponse = poser_question("Est-ce que vous le suppliez pour qu'il vous donne une dernère chance?",["oui","non"])
        if reponse == "non":
            print("Vous n'avez plus assez d'argent pour payer votre loyer et devenez un sans-abri. Vous serez retrouvé mort(e) deux mois plus tard, sous un pont, à cause d'un coma éthylique")
            perte()
        else:
            possibilite_refus -= 1
            debut_exploration(possibilite_refus)
    elif possibilite_refus == 0:
        print("Vous n'avez plus assez d'argent pour payer votre loyer et devenez un sans-abri. Vous serez retrouvé mort(e) deux mois plus tard, sous un pont, à cause d'un coma éthylique")
        perte()
    return possibilite_refus
            







def milieu_exploration(vie,inventaire):
    print("Dès que vous prenez la relique, le plafond se met à trembler dangereusement et des gros morceaux de pierre commencent à boucher l'entrée de la grotte. Vous remarquez qu'il y a un chemin qu paraît sûr, mais il faut agir vite.")
    start = time.time()
    reponse = poser_question("Qu'allez-vous faire?", ["reposer la relique","aller au fond de la grotte","tenter de libérer l'entrée et s'échapper"])
    temps = time.time()-start
    if int(temps) > 20:
        print("Vous avez pris trop de temps et vous êtes fait ensevelis par les cailloux.")
        perte()
    
    elif reponse == "reposer la relique":
        print("Le plafond arrête de trembler. Après 45 minutes de dur labeur, vous réussissez à sortir.Votre chef de recherche vous licensie à cause de votre inutilité dans l'équipe. Et vous n'avez plus aucune idée sur ce que vous pouvez explorer. Peut-être qu'il vous manquait ce goût du risque?")
        perte()
    
    elif reponse == "aller au fond de la grotte":
        print("Vous vous hâtez d'aller au fond de la grotte. Vous esquivez de peu les dernières pierres et vous jetez contre la paroi. En faisant cela, vous vous blessez légèrement les côtes. L'entrée est maintenant totalement obstruée et il serait trop long de la libérer. Vous sortez votre téléphone pour appeler les secours mais il s'est cassé dans votre chute. Vous n'avez que ce que vous avez pris ce matin et plus beaucoup d'espoir. Mais vous devez continuer, malgré votre blessure.")
        reponse = poser_question("Voulez-vous vous reposer?",["oui","non"])
        if reponse == "oui":
            print("Vous vous posez contre le mur le temps que votre blessure ne vous lance plus.")
            vie = vie+30
            if "barre protéinée" in inventaire:
                reponse = poser_question("Voulez-vous manger votre barre protéinée?",["oui","non"])
                if reponse == "oui":
                    print("Vous vous sentez encore mieux après avoir manger.")
                    vie = vie+20
                    inventaire.remove("barre protéinée")
    
    elif reponse == "tenter de libérer l'entrée et s'échapper":
        print("En essayant de libérer l'entrée vous vous faites ensevelir et écrabouiller par 50 tonnes de roche.")
        perte()
    print("Vous remarquez un chemin étroit dans une fissure. Vous l'empruntez car vous ne pouvez rien faire de mieux, à part ne pas perdre votre lampe torche. Après 5 minutes, vous débarquez devant une crevasse d'environ 3 mètres de long. Vous êtes obligé de sauter au-dessus pour survivre.")
    if vie == 100:
        print("Vous vous élancez mais, au moment de sauter, votre douleur aux côtes vous retient et vous tombez dans la crevasse.")
        perte()
    elif "lampe torche" not in inventaire:
        print("Vous ne voyez pas le rebord et faites un pas dans le vide. Vous mourez à la fin de la chute.")
        perte()
    elif vie == 130:
        print("Vous vous élancez mais ratterrissez mal. Vous avez maintenant très mal à la cheville.")
    else:
        print("Vous vous élancez et ratterrissez parfaitement. Vous pouvez continuer l'exploration.")
    return vie
    return inventaire
    







def fin_exploration():
    print("En marchant, vous apercevez un éclat doré. Vous vous précipitez vers cette lumière.")
    print("Vous vous approchez rapidement. Et une cinquantaine de mètres plus tard.... une salle remplie d'or!!! Vous êtes émerveillé, et vous le devenez encore plus lorsque vous voyez le soleil à travers une fissure. En fouillant la salle, vous tombez sur une corde et des piolets. Vous n'êtes pas le premier à passer par là. Vous remarquez des fissures dans la roche et commencez à monter.")
    if vie == 130:
        print("Après une grimpe de 10m votre cheville décide de ne pas coopérer et vous perdez appui. Vous tombez sur votre tête et mourez sans douleur")
        perte()
    print("Vous êtes dehors! Vous voyez un sentier un peu en contrebas et vous le rejoignez. Vous allez enfin pouvoir rentrer. Vous mémorisez l'endroit afin de le présenter à votre chef. Deux semaines plus tard, vous êtes promu au poste de chef-assistant. Vous avez réussi.")
    print("BIEN JOUÉÉÉÉ!!!!!!!!!")
    


#___________________________________________________________________________________________________________________-

intro(inventaire)
debut_exploration(possibilite_refus)
if "relique" not in inventaire:
    deuxieme_chance(possibilite_refus)
milieu_exploration(vie,inventaire)
fin_exploration()
























