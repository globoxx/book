import time


#situation initiale de l'histoire et contexte
def sit_initiale():
    print("Nous sommes dans un monde malheureux où des esprits malveillants ont envahi la Planète.(enter pour continuer)\n")
    input()
    print("N’ayant aucun talent spécial en arts martiaux et combat à mains nues, toi,", x, ", le pizzaiolo le plus renommé de ton petit village en région napolitaine, va combattre l’ennemi avec tes délicieuses pizzas afin de faire régner à nouveau la paix dans ce monde chamboulé.\n")
    input()
    print("Il y a un portail magique qui laisse s’échapper ces esprits maléfiques dans le gigantesque creux du Vésuve. Trouve un moyen de le réduire en morceaux, et la victoire sera à toi !\n")
    input()
    print("Tu as hérité d’une boîte magique qui s’est transmise de génération en génération dans ta famille.\n")
    input()
    print("Tu n’as qu’à y balancer tes ingrédients, et PAF, tu as une pizza toute chaude et prête à se faire manger (ou à être balancée dans la tronche de quelqu’un, c’est toi qui vois).\n")
    input()
    print("Bonne chance !\n")

def debut_histoire():
    answer = input("Es-tu prêt à commencer ton aventure?")
    if answer not in ["oui"]:
        print("Désolé! Tu est là pour sauver le monde, pas pour flemmarder!")
    if answer == "oui":
        print("Très bien, alors commençons!\n")
        time.sleep(1)
        
        
def start():
    answer = input("Est-ce que tu prends 1 heure pour te préparer, ou est-ce que tu te dépêches pour sauver l'humanité? (se préparer / se dépêcher)")
    
    while answer not in ["se préparer", "se dépêcher"]:
        print("Désolé, j'ai mal compris. Réessaie.")
        answer = input("Est-ce que tu prends 1 heure pour te préparer, ou est-ce que tu te dépêches pour sauver l'humanité? (se préparer / se dépêcher)")
        
    #On se prépare!!
    if answer == "se préparer":
        print("Tu te prépares tranquillement dans ta cuisine, tu a regagné tous tes PV!")
        pv = 100
        time.sleep(1)
        answer = input("Tu sors de chez toi et te retrouves devant deux possibilités. Traverses-tu la forêt des cauchemards, ou le lac asséché? (FC ou LA)")
        
        # Chemin de la foret des cauchemars
        if answer == "FC":
            print("Tu arrives dans la forêt. Une atmosphère lugubre se forme autour de toi.")
            time.sleep(2)
            print("Tu inspecte des environs, et garde ta boîte a pizza magique près de toi. Tu vois au loin un petit plant de basilic. C'est suspect, mais ça pourrait te servir...")
            answer = input("Cueilles-tu quelques feuilles?")
            
            if answer == "oui":
                print("Super, tu gagnes trois feuilles de basilic! Sers toi en pour te soigner quand tu en as besoin.")
            
            if answer == "non":
                print("Dommage! Tu finis par entrer dans la forêt.")
                print("Tu gambades pendant quelques heures. Le brouillard se lève, et tu ne vois plus rien, et tu faillis t'encoubler sur quelques racines. Tu finis aplati(e) contre un arbre...")
                print("Fais un choix: tu peux essayer de dormir le temps que le brouillard s'en aille, ou tu peux foncer tête baissée dans le brouillard sous peine de te blesser encore une fois ou de te perdre.")
                answer = input("Est ce que tu dors, ou est ce que tu continues ton chemin? (dormir ou continuer)")
            
            while answer not in ["oui", "non"]:
                print("Ne reste pas planté la, tu cours un grand danger!")
                answer = input("Cueilles-tu quelques feuilles?")
        
            print("Tu entres dans la forêt et restes sur tes gardes...")
            print("Tu gambades pendant quelques heures. Le brouillard se lève, et tu ne vois plus rien, et tu faillis t'encoubler sur quelques racines. Tu finis aplati(e) contre un arbre... Tu perds 5 PVs.")
            pv -= 5
            print("Fais un choix: tu peux essayer de dormir le temps que le brouillard s'en aille, ou tu peux foncer tête baissée dans le brouillard sous peine de te blesser encore une fois ou de te perdre.")
            answer = input("Est ce que tu dors, ou est ce que tu continues ton chemin? (dormir ou continuer)")
            if answer == "dormir":
                print("Tu t'endors penché(e) sur un arbre et regagnes quelques PVs.")
                pv += 15
                print("Quand tu te réveilles, le brouillard s'en est allé, et tu peux poursuivre ta route dans la tranquillité.")
                
            if answer == "continuer":
                print("Tu erres aveuglement, tes mains devant toi pour te protéger d'éventuels obstacles devant toi. Tu parviens tout de même à trébucher sur quelques pierres et perds 5 PVs.")
                pv -= 5
                
            while answer not in ["continuer", "dormir"]:
                print("Pardon? J'ai pas bien entendu, peux tu répéter?")
                answer = input("Est ce que tu dors, ou est ce que tu continues ton chemin? (dormir ou continuer)")
        
        # Chemin du lac asséché
        if answer == "LA":
            print("Tu arrives vers le lac, qui n'a finalement pas grand chose d'un lac. C'est un énorme fossé sec et presque dépourvu de vie.")
            answer = input("Passes-tu tout droit, ou marches-tu vers la droite sous de vieux arbres? (tout droit / à droite)")
            
            if answer == "tout droit":
                print("Tu sens la chaleur du soleil brûler ta peau. Tu es sain et sauf, mais tu as quand même pris un méchant coup de soleil. Tu perds 5 PVs.")
                pv =- 5
                answer = input("Tu vois un amas de plantes au loin. Est ce que tu t'en approches?")
                if answer == "oui":
                    print("C'était des oignons! Tu en cueilles quelques uns.")
                    
                else:
                    print("Tu ne sauras jamais ce que c'était. Le mystère est intense...")
                    
            if answer == "à droite":
                print("Tu restes caché(e) sous les arbres secs et échappe aux rayons brûlants du soleil. Malheureusement, les moustiques semblent t'apprécier. Tu perds 10 PVs.")
                pv -= 10
                answer = input("Tu vois quelques feuilles vertes familières sous les racines d'un arbre. Est ce que tu les ramasse?")
                if answer == "oui":
                    print("Tu mets les feuilles de basilic dans ta sacoche. Tu en auras sûrement besoin.")
                    
                else:
                    print("Très bien, ne perdons pas de temps.")
                    
            while answer not in ["à droite", "tout droit"]:
                 print("Répète-moi ça?")
                 answer = input("Passes-tu tout droit, ou marches-tu vers la droite sous de vieux arbres? (tout droit / à droite)")
            print("Tu continues à marcher et arrives enfin sur l'autre rive du lac. Dis donc, c'était épuisant! Tu as perdu 5 PVs rien qu'en marchant...")
            pv -= 5
            time.sleep(2)
            print("Bravo! Tu as survécu à la première partie de ton voyage. Tu te fais une pizza bien méritée et la savoures en souriant.")
            print("Tu sais que le portail maléfique se trouve dans le volcan. Tu vois un panneau: Volcan du Vésuve, 2 semaines de marche, ou Villge de l'Arrabiata, 45 minutes de marche.")
            answer = input("Quel chemin choisis-tu? (volcan ou village)")
            if answer == "village":
                print("Alors en route!")
                
            
            if answer == "volcan":
                print("Tu erres sur un fin chemin de terre en espérant trouver ton chemin. Mais après une heure, un jour, une semaine... tu n'as à présent aucune idée d'où tu es.")
                answer = input("Est ce que tu continues, ou essaies tu de revenir sur tes pas? (continuer ou revenir)")
                if answer == "continuer":
                    print("Tu marches pendant des heures, mais tu n'en vois pas la fin. Tu souffres d'une mort lente et douloureuse, errant sans but pour finalement t'écrouler au sol.")
                    print("GAME OVER.")
                if answer == "revenir":
                    print("Tu as beau chercher, mais c'est peine perdue. Un ours sauvage abrège tes souffrances car tu étais dans son territoire.")
                    print("GAME OVER.")
                sit_initiale()
                
            else:
                print("Réessaie, j'ai du mal comprendre.")
                answer = input("Quel chemin choisis-tu? (volcan ou village)")
                
        #entrée au village!!
        print("Tu marches pendant une bonne quarantaine de minutes avant d'arriver à un charmant village. Il est écrit 'Bienveue à Arrabiata!!' en lettres colorées et joyeuses sur une banderole.")
        print("Tu te ballades un peu et regardes tes environs. A droite se trouve un café, et à gauche un marché.")
        answer = input("Vas-tu à droite ou à gauche? (droite ou gauche)")
        
        if answer == "droite":
            print("Tu entres dans le café. Il n'y a pas de clients, il semble bizarrement vide.\n")
            print("Tu parle avec le barista qui te dis que leur machine ne fonctionne pas et qu'il ne peuvent servir personne actuellement.\n")
            answer = input("Les aides tu a le réparer?\n")
            
            if answer == "oui":
                print("Tu sors une pâte de pizza dans laquelle t'incorpores quelques feuilles de basilic.\n")
                print("T'étales le tout que tu pose ensuite sur la machine.\n")
                print("Elle commence a marcher et produit un esspresso magnifique.\n")
                print("Tu le bois et le patron te remercie infiniment et t'offre un chorizo fait maison.\n")
            elif answer == "non":
                print("Tu quittes le café et continues sur ton chemin.\n")
                
            
        elif answer == "gauche":
            print("Tu entres dans le supermarché.\n")
            print("Tu cherches des ingrédients pour tes pizzas. Tu sors avec une quantité égale d'oignons, de jalapenos et de fromage bleu.\n")
            
        
        else:
            print("Réessaie, j'ai du mal comprendre.")
            answer = input("Vas-tu à droite ou à gauche? (droite ou gauche)")
        
        print("Tu continues à marcher et arrivé au bout du village, tu vois un bus qui part pour le Vésuve dans 10 minutes.\n")
        print("Tu montes dedans et il part.\n")
        print("Le bus fait un arrêt à Pompeii.\n")
        print("Tu sors prendre l'air et tu vois un ananas doré qui brille avec tout la lumière du soleil.\n")
        print("Tu le mets dans ton sac et tu retournes dans le bus.\n")
        time.sleep(3)
        print("Te voilà finalement arrivé au Volcan, le dernier chapitre de ton aventure!\n")
        print("Tu commences la montée quand tout à coup tu te retrouves face à un serpent géant!!\n")
        answer = input("Que fais tu? Veux tu courir ou faire une pizza armée pour le combattre? (courir ou pizza)\n")
        if answer == "courir":
            print("Non mais...mais non!\n")
            print("Nan, ok chut, c'est bon. \n")
            print("T'es mort, le serpent t'a attrapé on a compris. Oy vey.\n")
        elif answer == "pizza":
            answer = input("Tu mets quoi sur la pizza? Des onions? ou du basilic?\n")
            if answer == "basilic":
                print("Mais bravooo! Tu as GUERI le serpent!\n")
                print("Et maintenant tu es mort.\n")
                print("Dead.")
                print("Kaput.")
                pv= 0
            elif answer == "onions":
                print("Tu lances la pizza sur le monstre qui crit de douleur.\n")
                print("Une deuxième maintenant qu'il est affaibli!\n")

                answer = input("Des jalapenos ou du chorizo sur celle-ci?")
                if answer == "chorizo":
                    print("Le serpent semble dèstabilisé mais apprécie le petit snack.\n")
                    print("Il te frappe avec un coup de queue et te jette contre la paroi du volcan.\n")
                    pv= 0
                elif answer == "jalapenos":
                    print("Les piments brûlent l'énorme reptile devant toi. BRAVOOO!\n")
                    print("Tu arrives au sommet du volcan.\n")
                    print("Tu sais qu'il te reste une dernière étape à ta mission. Tu sors l'ananas de Pompeii.\n")
                    print("Qu'en fais tu?\n")
                
                    answer = input("Le manger? le jeter dans le volcan? en faire un chapeau? (manger, jeter ou chapeau)\n")
                    if answer == "manger":
                        print("Alors je ne sais pas dans quel monde un ananas lumineux te fais penser: 'Oh! Miam' mais d'accord.\n")
                        print("Nan en fait tu meurs quand même. Inattention ou un truc du genre et tu tombes dans le Vésuve voilà.\n")
                        pv= 0
                    elif answer == "chapeau":
                        print("Bon, au moins la fin du monde ne te fais pas perdre ta créativité, mais je crois qu'ils y'en ont qui auraient préféré un acte plus héroïque....\n")
                        answer = input("Le manger? le jeter dans le volcan? en faire un chapeau? (manger, jeter ou chapeau)\n")
                    elif answer == "jeter":
                        print("Finalement, finalement, le portail se ferme et tu sens le monde qui se remet doucement en place sans les monstres terrorisants.\n")
                        print("Merci infiniment brave héros!")
                        print("Fin de l'aventure")
                    else:
                        print("Je n'ai pas compris, réessaies...\n")
                        answer = input("Le manger? le jeter dans le volcan? en faire un chapeau? (manger, jeter ou chapeau)\n")
                else:
                    print("Je n'ai pas compris, réessaies...\n")
                    answer = input("Des jalapenos ou du chorizo sur celle-ci?")
        else:
             print("Je n'ai pas compris, réessaies...\n")
             answer = input("Tu mets quoi sur la pizza? Des onions? ou du basilic?\n")

                
        
    if answer == "se dépêcher":
        print("Tu prends tes affaires et pars en courant. Malheureusement, tu trébuches apres 3 mètres de course et t'écorche le genou. Tu perds 5 PVs.")
        print("Tu retournes donc te soigner.")
        start()
            
        

    
pv = 75
inventaire = []
if pv == 0:
    print("Game Over")
x = input("Comment t'appelles tu?")
print("bienvenue", x, "!")
sit_initiale()
debut_histoire()
start()