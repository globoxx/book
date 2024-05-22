import random

inventaire = []
vie = 2

#il y a parfois plusieurs ligne de "print" à la suite. C'est pour structurer l'histoire lorsque'elle est écrite dans le terminal, pour faire en sorte qu'il y ait des retours à la ligne et que ce soit plus lisible

def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    return reponse

def fin_rocher() :
    global vie
    print("Vous vous relevez et courrez de toutes vos forces alors que les golems vous jette d'énorme pierre dessus, une des pierre vous touche la nuque et vous pousse un cris de douleur. Votre vie baisse de 1.")
    vie = vie-1
    if vie == 0 :
        print("Vous avez sucombé au rocher")
        print("GAME OVER")
        exit()
    elif vie>0 :
        print("Vous réussissez à fuir, et après plusieurs minutes de course intense, vous retrouvez le ruisseau bleu.")
        histoire()

def grotte_carte() :
    choix = poser_question("Voulez-vous y entrer?", ["oui", "non"])
    if choix == "oui" :
        print("C'était un piège tendu par un farrouche farfadet. Vous vous êtes malheureusement perdu à l'intérieur de celle-ci.")
        print("GAME OVER")
        exit()
    elif choix == "non" :
        print("Vous suivez soigneusement l'itinéraire de cette carte. Un triton s'oppose soudainement à vous.")
        rand = random.choice([True, False])
        if rand == True :
            print("Vous vous êtes baigné, il y a encore de l'eau sur vos cheveux")
            print("Le triton puise l'eau de vos cheveux afin de renforcer ses pouvoirs. Il vous foudroie avec son trident.")
            print("GAME OVER")
            exit()
        elif rand == False :
            print("Quelques mètres plus tard, des objets sont posées par terre. Il y a un arc et une baguette magique.")
            print("VOUS AVEZ GAGNER")
            exit()

def histoire() :
    global vie
    print("Vous vous réveillez dans une mystérieuse forêt, sans savoir où celle-ci se situe ni comment vous y êtes parvenu. En regardant autour de vous, vous apercevez un ruisseau d'un bleu étincelant. Puis en tournant la tête, vous découvrez un chemin qui s'enfonce dans cette forêt qui vous intrigue tant.")
    choix = poser_question("Souhaitez-vous suivre le ruisseau, ou préférez-vous emprunter le petit chemin ?", ["le chemin", "le ruisseau"])
    if choix == "le chemin":
        print("Après avoir marché pendant de nombreuses heures, vous rencontrez un petit animal étrangement mignon à 6 têtes. Il vous propose un caillou qui vous semble quelque peu douteux.")
        choix = poser_question("L'acceptez-vous ?", ["oui", "non"])
        if choix == "oui":
            inventaire.append("la pière")
            print("Vous récupérez le caillou, en le remerciant.")
        print("Vous le saluez et continuez votre route. Le soleil commence à se coucher. Il vous faut trouvez un abri où passer la nuit. ")
        choix = poser_question("Voulez-vous continuer à marcher, ou bien souhaitez-vous vous construire un abri de fortune sur place?", ["continuer à marcher", "rester sur place"])
        if choix == "continuer à marcher" :
            print("Vous voyez une grotte au loin. Vous y entrez et trouvez de quoi allumer un feu. Vous faites un feu et vous vous endormez.")
            rand = random.choice([True, False])
            if rand == True :
                print("Alors que vous dormiez, un ours vous réveille et vous dévore avant que vous n'ayez eu le temps de réagir.")
                print("GAME OVER")
                exit() 
            elif rand == False :
                print("Vous vous réveiller, en pleine forme. Vous sorter de la grotte et reprenez votre route dans la forêt.")
        elif choix == ("rester sur place") :
            print("Vous trouvez quelques branches et vous vous faites un petit abri pour passez la nuit.")
            print("Vous vous réveillez, épuisé. Votre vie diminue de 1. Vous reprenez votre route dans la forêt.")
            vie = vie-1
        print("Après quelque temps, vous arrivez dans une clairière dans laquelle sont disposées plusieurs stèles de pierre positionnées en rond.")
        choix = poser_question("Préférez-vous les inspecter ou ne pas y faire attention?", ["passez outre", "les inspecter"])
        if choix == "les inspecter" :
            print("Vous les regardez de plus près et distinguer comme une forme humanoïde. Vous touchez ces rochers quand ceux-ci se mirent à bouger quand soudain d'impressionnants golems sortent de ces derniers.")
            if "la pière" in inventaire:
                print("Il vous fixe tous en vous point en répétant d'une voie grave 'la pière!'")
                print("Vous vous rapeller de la pière que vous a donner le petit animal tout à l'heure et vous la tender genriment aux golème. Il la prène, vous remercie. En ce mettant tous en rond, il vous ouvre un portail, vous y aller sans trop savoir ce qui vous attend.")
                print("VOUS AVEZ GAGNER")
                exit()
            else :
                print("Vous les voyez se mettre en colère car vous les avez réveillé et ceux-ci commencent à vouloir vous jeter des pierre dessus.")
        elif choix == "passez outre" :
            print("Vous les regardez sans plus et chouter un calliou sans trop réfléchir. Celui-ci heurte une des stèle quand tout a coup, celle-ci ce mis a bouger en vous repousse d'un coup de pied soudai. Votre vis baisse de 1. En vous relevant, sonnez, vous vous rendez compte que que ce sont des golème de pière et qu'il sont tous autour de vous.")
        choix = poser_question("Préférez-vous fuir ou leurs jeter désespérément ce que vous avez dans les poche?", ["fuir", "jeter"])
        if choix == "fuir" :
            fin_rocher()
        elif choix == "jeter" :
            if "la pière" in inventaire:
                choix = poser_question("Que jetez-vous? Une branche, un caillou, la pière du petit animal", ["caillou", "branche", "la pière"])
                if choix == "la pière":
                    print("Vous la jeter de toute vos force et contre toute attente, les golème s'arrête net, fixant tous ce que vous venez de leur lansez")
                    print("Vous réussissez à fuir.")
                    histoire()
            else :
                choix = poser_question("Que jetez-vous? Une branche, un caillou", ["caillou", "branche"])
                rand = random.choice([True, False])
                if rand == True :
                    print("Vous la/le jeter de toute vos force et contre toute attente, les golème s'arrête net, fixant tous ce que vous venez de leur lansez")
                    print("Vous réussissez à fuir.")
                    histoire()
                elif rand == False :
                    print("Ils ne réagissent pas et s'énèrvent encore plus.")
                    fin_rocher()
    elif choix == "le ruisseau" :
        print("Vous suivez le ruisseau pendant plusieurs dizaines de minutes avant de trouver un petit lac.")
        choix = poser_question("Souhaitez-vous vous y baigner ou vous reposer sur le coté ?", ["se baigner", "se reposer"])
        if choix == "se reposer" :
            vie = vie+1
            print("Votre vi augmente de 1")
            print("Vous vous endormez et, alors que vous constater que vous êtes en train de rêver...")
            histoire()
        elif choix == "se baigner" :
            print("Vous vous déshabiller et allez profiter de la fraicheur de l'eau.Vous sentez toutefois quelque chose au fond de l'eau qui frotte vos pieds")
            choix = poser_question("Souhaitez-vous sortir de l'eau ou préférez-vous plonger sous l'eau pour voir ce que c'est ?", ["sortir", "plonger"])
            if choix == "plonger" :
                print("C'est une sirène ! Elle vous tend une carte qui semble mener à un trésor. Vous prenez la carte, la remerciez, et sortez de l'eau.")
                inventaire.append("carte")
                print("Une fois sorti de l'eau, sec et rhabillé, vous suivez la carte. Sur votre chemin se trouve une grotte.")
                grotte_carte()
            elif choix == "sortir" :
                print("Vous sortez de l'eau puis vous vous séchez avec l'air du vent. Une fois rhabillé,vous apercevez un ogre.")
                choix = poser_question("Le saluez-vous ou continuez-vous votre route?", ["saluer", "continuer"])
                if choix == "saluer" :
                    print("L'ogre se sent heureux et vous offre en cadeau, pour votre gentillesse, une carte menant à un trésor.")
                    inventaire.append("carte")
                    choix = poser_question("Voulez-vous suivre cette carte?", ["oui", "non"])
                    if choix == "oui" :
                        print("Vous commencez à suivre le chemin que cette carte vous indique. Vos tombez nez-à-nez face à une grotte.")
                        grotte_carte()
                    elif choix == "non" :
                        print("Vous vous perdez dans la forêt.")
                        print("GAME OVER")
                        exit()
                elif choix == "continuer" :
                    print("Quelques mètres plus tard, des objets sont posées par terre. Il y a un arc et une baguette magique.")
                    choix = poser_question("Souhaitez-vous prendre l'arc ou la baguette?", ["arc", "baguette"])
                    print("Vous marchez paisiblement en observant le paysage quand soudain, une sorcière apparaît. Elle vous confronte en duel.")
                    if choix == "arc" :
                        print("Vous lui tirer ridiculement une flèche qu'elle atrape en vol et brise en deux, elle vous transforme en crapaud. ")
                        print("GAME OVER")
                        exit()
                    elif choix == "baguette" :
                        print("Vous lui lancer un sort et elle se transforme et crapaud.")
                        print("VOUS AVEZ GAGNER")
                        exit()

histoire()