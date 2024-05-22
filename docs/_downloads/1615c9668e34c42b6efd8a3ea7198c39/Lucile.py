### définir l'inventaire d'objets
accessoires = []

### initialiser les variables "résistance" et "affinité"
résistance = 1
affinité = 60
fin = False

### recalculer les points de résistance
def calcul_résistance(changement_résistance):
    global résistance
    résistance = résistance + changement_résistance
    print("Vous avez maintenant", résistance, "point(s) de résistance.")
    
### recalculer le nombre d'affinité
def calcul_affinité(changement_affinité):
    global affinité
    affinité = affinité + changement_affinité
    print("Vous avez désormais", affinité, "points d'affinité")

   
### définir le script des questions
def poser_question(question, choix_possibles):
    reponse = input(question + str(choix_possibles))
    while reponse not in choix_possibles:
        reponse = input(question + str(choix_possibles))
    while reponse == "":
        reponse = input(question + str(choix_possibles))
    return reponse
    
### quand il y a beaucoup de texte, cette fonction permet à l'utilisateur d'afficher successivement les différentes parties à l'aide de la touche ENTER
def passage (texte1, texte2):
    reponse = input(texte1 + "(Enter pour continuer)")
    if reponse == "":
        print(texte2)

### Boucle d'exploration du corail  
def corail():
    print("Vous vous dirigez ensemble vers la barrière de corail, vous gagnez 15 points d'affinité !")
    calcul_affinité(+15)
    global fin
        
    print("Vous longez les coraux à la recherche de poissons clowns.")
    
    ### entrer ou pas dans la grotte
    global choix
    choix = poser_question("Vous appercevez une grotte et vous dirigez vers l'entrée. Votre ami vous dit de ne pas vous y aventurer, y entrez-vous ?", "(oui/non)")
               
    if choix == "oui":
        print("Vous perdez 15 points d'affinité.")
        calcul_affinité(-15)
                
        passage("L'entrée est un peu étroite mais vous vous y faufilez seul.e. Des plantes lumineuses éclairent légèrement l'espace.","Soudain, vous sentez quelque chose foncer sur vous, et vous mordre brusquement le bras. Vous perdez 1 point de résistance.")
        
        ### morsure - mourir ou pas
        calcul_résistance(-1)
        if résistance == 0:
            print("Vous mourrez de votre blessure dans les secondes qui suivent.")
            print("GAME OVER !")
            fin = True
        
        elif résistance >0:
            choix = poser_question("Vous décidez de : sortir de la grotte pour retrouver votre ami ou continuer d'explorer la grotte ?", "(sortir/explorer)")
            
            if choix == "sortir":
                print("Vous quittez la grotte et rejoignez votre ami qui a trouvé un joli coin de corail à observer.")
                    
            elif choix == "explorer":
                print("Vous trouvez des restes humains accrochés à une paroi de la grotte par un harpon.")
                
                ### prendre le harpon ou pas
                choix = poser_question("Récupérez-vous le harpon ?oui, il pourrait bien m'être utile pour la suite de mon aventure!/non, dégoutant!Je le laisse à son propriétaire!!!", "(oui/non)")
                    
                if choix == "oui":
                    print("Vous récupérez le harpon.")
                    accessoires.append("harpon")
                    print("Contenu de votre équipement :", accessoires)
                    print("Vous tentez d'accrocher le harpon à votre équippement mais peu agile comme vous êtes, celui-ci transperce votre bombonne d'oxygène. Vous n'avez donc plus d'air et vous vous noyez.")
                    print("GAME OVER !")
                    fin = True
                        
                elif choix =="non":
                    print("Vous quittez la grotte sans le harpon et rejoignez votre ami qui, pendant votre absence, a trouvé un joli coin de corail à observer.")
           
    elif choix == "non":
        print("Vous suivez le conseil de votre ami et continuez de vous émerveiller devant le spectacle qui s'offre à vos yeux.")
    
    if fin==False:
        passage("","")
    else:
        print("")

### Boucle d'exploration de l'épave
def épave():
    print("Vous vous dirigez seul.e vers la mythique épave ayant été victime d'un naufrage, et perdez 15 points d'affinité.")
    calcul_affinité(-15)
    print("Vous trouvez une brêche dans la coque du bateau et commencez à l'explorer.")
    
    ### prendre le trésor ou pas
    global choix
    choix = poser_question("Vous vous retrouvez dans la salle aux trésors. Vous hésitez à emporter un petit souvenir.", "(prendre/laisser)")
    
    if choix == "laisser":
        print("Vous laissez tout en place et, vous sentant observé.e, vous vous dirigez vers la sortie.")
    
    elif choix == "prendre":
        print("Vous vous emparez d'un petit objet, le glissez dans votre équipement et, vous sentant observé.e, vous vous dirigez vers la sortie.")
        accessoires.append("trésor")
        print("Contenu de votre équipement :", accessoires)
    
    ### informer ou pas de la trouvaille    
    choix = poser_question("De nouveau hors du bateau, vous retrouvez votre ami et hésitez à l'informer de votre trouvaille. L'en informez-vous ?", "(oui/non)")
    
    if choix == "oui":
        print("Vous informez votre ami et gagnez 15 points d'affinité.")
        calcul_affinité(+15)
        print("Enthousiastes, vous retournez ensemble à l'intérieur afin d'avoir une meilleure idée de l'ampleur de votre découverte.")
        passage("Une fois dans la salle aux trésors, ce sentiment d'être observé.es augmente. Soudain, la porte se referme et vous entendez le verrou se fermer.", "Ne pouvant avertir personne de votre situation, vous n'aurez bientôt plus d'oxygène dans vos réservoirs et risquerez de vous noyer.")
        
        ### utiliser bombonne 1 ou 2 pour s'échapper
        choix = poser_question("Pour vous en sortir, vous devez utiliser un de vos réservoirs d'oxygène pour enfoncer la porte. Un de vos réservoir est vide, l'autre est plein mais vous ne savez pas lequel est vide, lequel allez-vous débrancher ?", "(1/2)")
        
        if choix == "1":
            print("Pas de chance ! Vous avez débranché votre dernière réserve d'oxygène. Vous aviez une chance sur 2 de survivre ! Vous vous noyez avec comme dernière pensée que personne ne saura où vous trouver.")
            print ("GAME OVER !")
            global fin
            fin=True
            
        elif choix == "2":
            print("Ouf ! Vous ne vous êtes pas trompé.es de bombonne, vous arrivez à enfoncer la porte avec la bombonne vide, vous vous dépêchez de sortir de l'épave.")
            
    elif choix == "non":
        print("vous gardez votre petit secret pour vous.")
        
    if fin==False:
        passage("vous continuez à explorer les fonds marins en quête de petits poissons indigènes","")
    else:
        print("")

### Fin de l'histoire sur le bateau
def bateau():
    print("Arrivé.es sur le bateau, vous vous débarrassez de vos équipements.")
    
    ### fin de l'histoire selon si on a pris le trésor ou pas    
    if "trésor" in accessoires:
        print("Le trésor s'échappe de votre équipement et tombe sur le sol du bateau.")
        passage("L'équipage du bateau voit ce petit objet brillant et vous demande avec insistance où vous l'avez trouvé.", "Vous comprenez vite que l'équipage du bateau fait partie de la mafia et recherchait justement le trésor dont vous avez emporté une partie.")
        
        if affinité >= 60:
            print("Vous avez actuellement", affinité, "points d'affinité : votre ami, solidaire, vous défend et arrive à vous sortir de la situation. Vous quitterez bientôt le bateau et boirez un mojito sur la plage en vous réjouissant déjà de votre prochaine aventure ensemble.")
            print("VICTOIRE !")
            
        elif affinité < 60:
            print("Vous avez actuellement", affinité, "points d'affinité : votre ami ne vous défend pas ; n'étant pas non plus habile de vos mots, vous n'arrivez pas à expliquer la situation aux mafieux. Ceux-ci étant peu patients, ils décident de vous tuer.")
            print("GAME OVER !")
    
    else:
        print("Votre ami et vous êtes fatigué.es, vous méritez bien une petite sieste et vous vous réjouissez déjà de votre prochaine aventure ensemble !")
        print("VICTOIRE !")
        
    
### début de l'histoire
prénom = input("Bienvenue dans l'histoire interactive! Choisissez votre pseudo...")
print("Bienvenue à bord,",prénom,"!", "Vous êtes sur un bateau en pleine mer pour faire de la plongée sous-marine avec un ami. Vous avez 1 point de résistance et 60 points d'affinité avec votre ami.")

### manger ou pas
choix = poser_question("On vous propose de manger avant de plonger, acceptez-vous ?", "(oui/non)")
  
if choix == "oui":
    print("Vous acceptez et mangez un petit plat de fruits, vous gagnez 1 point de résistance !")
    calcul_résistance(1)    
    print("Après avoir bien mangé, vous vous préparez à plonger.")
    
elif choix == "non":
    print("Vous refusez et vous préparez à plonger.")
    
passage("Vous et votre ami plongez, regardez les alentours et allez observer un requin baleine.","Après quelques instants de bonheur, l'animal part comme s'il fuyait quelque chose...")

### sélection des 3 options
while fin == False :
    print("Vous avez le choix d'aller explorer une épave de bateau, une barrière de corail, ou de remonter sur le bateau.")
    choix = poser_question("Votre ami souhaite observer la barrière de corail, que choisissez-vous ?", "(épave/corail/bateau)")

    if choix == "corail":
        corail()
    
    elif choix == "épave":
        épave()
        
    elif choix == "bateau":
        fin=True
        bateau()

