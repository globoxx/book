import time as tm
hache = 0
vie = 100
def sleep(x):
    tm.sleep(x)

print("Tu es tout seul dans un champ avec aucune arme, tu te leves et regardes autour de toi, il n'y a rien. Juste la foret d'un cote et la plage de l'autre.")
sleep(2)
#foret ou plage
reponse3 = input("foret ou plage ? 1 = foret, 2 = plage")
if reponse3 == "1":
    print("tu t'aventures dans cette fôret obscur dont tu ne connais le nom")
    #marécage ou arbre
    while True:
        reponse1 = input("veux tu te diriger vers les grand arbres ou le marécage ? 1 = grands arbres, 2 = marécage")
        if reponse1 == "1":
            print("tu passe un bon moment à coté de ces majestueux arbres jusqu à voir une hache bizarement plantée contre l'un des arbres.")
            #hache
            reponse = input("Prendre la hache ? 1 = oui, 2 = non")
            if reponse == "1":
                print("vous fuyez facilement une attaque surprise d'un gobelin sauvage que vous repoussez avec votre hache ")
                hache = 1
            if reponse == "2":
                print("vous fuyez difficilement l'attaque surprise d'un gobelin sauvage sans hache")
                hache = 0
        if reponse1 == "2":
            print("tu vois un sarchosuchus qui n'hésite pas à t'attaquer ")
            #si hache
            if hache == 1:
                print("tu réussis de peu à défoncer la gueule de ce sarcho qui se tire au loin. vie-50")
                print("tu continues à t'avancer dans ces bois qui deviennent de plus en plus obscur lorsque tu croises un petit homme des bois qui souhaite t'offrir un champignon joli car tu as une jolie petite gueule d'après lui.")
                reponse = input("prendre le champignon ?1 = oui, 2 = non")
                if reponse == "1":
                    print("tu gagnes 50 de vie(évidemment que les petits sont gentils)")
                    sleep(2)
                    print("un troll te bloque le passage qui te permettrai de gravir une grande montagne.Il te lance une boule de bowling du boulissssteeeeeeeee hihihu tu perds donc 50 de vie. ")
                    print("Comme tu as accepté le présent du petit homme, tu défonces le troll à coup de ta superbe hache et gravi cettemontagne avec dificulté jusqu'à y voir en son sommet un joli petit village dans lequel tu vas rester pour vivre heureux jusqu'à ta mort en l'année 2679.")
                    break
                if reponse == "2":
                    print("tu continues ta route tranquilement")
                    sleep(2)
                    print("un troll te bloque le passage qui te permettrai de gravir une grande montagne.Il te lance une boule de bowling du boulissssteeeeeeeee hihihu tu perds donc 50 de vie. ")
                    sleep(1)
                    print("...")
                    sleep(2)
                    print("KOOOOOOO PAR BOULISTTEEEE HIHIHIAAAAA")
                    print("game over !")
                    break

            if hache == 0:
                print("Le sarchosuchus te déchicte comme un animal,tu te vides de tes entrailles")
                print("GameOver ! (noob)")
                break
if reponse3 == "2":
    print("Tu te promènes sur la plage mais ne croises personne, tu t'ennuies donc bien ferme. Tu vois un caillou au sol. ")
    reponse = input("Faire des ricochets ou ne pas faire de ricochets ? 1 = oui 2 = non")
    if reponse == "2":
        print("Tu meurs d'ennui. Game over. ")
    if reponse == "1":
        print("Tu fais ton meilleur ricochet, qui finit avec un 12ème rebond droit dans la gueule d'un enfant que t'avais pas vu. L'enfant crie. Un vieil homme apparait derriere toi et te demande si tu aimes frapper les enfants.")
        reponse = input("Lui répondre ou fuir ? 1 = répondre, 2 = fuir")
        if reponse == "2":
            print("Tu fuis mais tu as tellement honte d'avoir fui ET d'avoir blessé un enfant que tu exploses littéralement (parce que pourquoi pas, c'est vraiment puissant la culpabilité). Game over.")
        if reponse == "1":
            reponse = input("Répondre oui ou non ? 1 = oui, 2 = non")
            if reponse == "2":
                print("Tu réponds que non, que tu n'avais pas fait exprès de jeter ce caillou dans les molaires de cet enfant, et le vieil homme, visiblement déçu, part dans un portail qu'il ouvre grace à un magnifique baton. Tu essaies de le suivre dans le portail mais ce dernier se referme en te coupant en deux. Game over.")
            if reponse == "1":
                print("Pris de court par cette subite apparition et confus par la pression de la situation, tu réponds que oui, tu as fait exprès. Le vieil homme te regarde un moment avant de sourire largement. Il te dit : C'est bien. Moi aussi j""'""""aime frapper les enfants.Tu m""'""as l""'"air confus mon jeune ami. Tu n'es pas d'ici ?""")
                reponse = input("Répondre je suis d""""'"ici" ou "je ne suis pas d'ici" ? 1 = d'ici, 2 = pas d'ici""")
                if reponse == "1":
                    print("Tu réponds que tu es d'ici. Le vieil homme te réponds alors qu'il aime pas les gens qui viennent du coin, et fait apparaitre des disques d'Aya Nakamura, il te les jette dessus et tu te couvres de boutons violets à leur contact avant de mourir. Game over.  ")
                if reponse == "2":
                    print("Tu réponds que tu n'es pas d'ici, et le vieillard te sourit une fois de plus, en disant que lui non plus. Il te propose alors une fiole de potion rose. ")
                    reponse = input("Prendre la potion ou ne pas la prendre ?1 = oui, 2 = non")
                    if reponse == "1":
                        print("Le vieil homme te donne sa fiole de potion rose. Tu bois goulument ce breuvage frais sa mère. Ta vie est à 150 maintenant. Le vieil homme dit que vous vous recroiserez peut-être un autre jour, dans une autre vie, et te souhaite bonne route. ")
                        vie = 150
                    elif reponse == "2":
                        print("Tu refuses en expliquant que tu n'aimes pas le rose. Il te dit alors qu'il est déçu que tu sois sexiste, mais que si tu voulais savoir ta vie est à 100, et tu lui dis merci même si t'as rien compris. Il te souhaite bonne chance dans ta quête et disparait en claquant des doigts. ")
                    if reponse == "1" or reponse == "2":
                        print("Tu poursuis ton chemin, rencontrant moult pandas sur la plage qui chantent au ukulélé, et tombes enfin sur un hameau, d'où émanent des nuages de fumée. Les habitants viennent vers toi, paniqués. Ils t'expliquent qu'un dragon incendie leurs habitations. N'hésitant pas, ni une, ni deux, tu te précipites vers la belle bête en courant.  ")
                    if vie < 150:
                        print("Le dragon te crache du feu dessus et tu meurs. Le village est détruit mais au moins, à la fin, les habitants peuvent se consoler en mangeant du kébab (toi). Game over. ")
                    else:
                        print("Le dragon te crache du feu dessus, mais tu tiens bon (par contre tu n'as plus que 50pv). Toujours est-il que tu assènes une assourdissante patate de forain sur le gros crane du dragon, et en viens à bout. Le village entier te célébre en héros inespéré, et le forgeron t'offre son épée. ")
                        reponse = input("Accepter ou refuser l'épée ? 1 = oui, 2 = non")
                        if reponse == "1":
                            print("Tu accèptes l'épée et remercies chaleureusement le forgeron. ")
                            épée = 1
                        if reponse =="2":
                            print("Tu refuses l'épée.")
                            épée = 0
                        reponse = input("Rester au village ou continuer l'aventure ? 1 = rester, 2 = continuer")
                        if reponse == "1":
                            print("Tu restes au village. Tu adoptes un chien, apprends à connaitre les habitants, et finis par filer le parfait amour avec une des serveuses, que tu as remarqué pendant ta bataille épique, qui forgera d'ailleurs la légende du village, ainsi que la tienne. Tu meurs paisiblement à l'age vénérable de 38 ans en regardant le coucher de soleil. Bien joué guerrier. Tu auras vécu une belle vie. ")
                        if reponse == "2":
                            print("Un sorcier maléfique apparait dans un nuage de fumée verte foncée. Il t'explique que tu es le fruit de sa création, que maintenant que tu as prouvé que tu es le plus puissant des Hommes, il te démultipliera pour conquérir le monde et qu'il devrait y'avoir plein de scénario mais que vraiment il faudrait être dans un triple A pour se le permettre, donc qu'il va juste te capturer tout de suite. ")
                            if épée==1:
                                print("Tu sprintes tel Usain Bolt en esquivant les sorts et jette ton épée, qui finit dans le ventre du sorcier affaibli. Le vieil homme de la plage apparait et met un coup de baton dans les fesses du sorcier, ce qui le fait exploser en nuage de fumée rouge. Le village te célébre, tu deviens le plus grand sorcier du pays et tu vis une vie heureuse en bromance avec le vieil homme. Fin.  ")
                            else:
                                print("Tu meurs, foudroyé par un sort qu'il te jette et qui te fait exploser. Game over. ")




