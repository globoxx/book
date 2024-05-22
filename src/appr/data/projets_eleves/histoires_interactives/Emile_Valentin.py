argent=0
inventaire=[]
vie=85

def debut():
    global argent
    print("vous faites un randonée dans une foret")
    print("vous avez une torche et une pièce d'or")
    inventaire.append("torche")
    argent=argent+5
    tournant()

def tournant():
    print("vous arrivez à un croisement")
    print(" 2 choix s'offrent à vous gauche ou droite")
    reponse=input("quelle direction prenez vous")
    if reponse=="gauche":
        chemingauche()
    if reponse=="droite":
        chemindroite()
def chemindroite():
    print("Au bout de 69 minutes de marche vous arrivez devant un manoir")
    reponse==input("souhaitez vous entrer dans ce manoir ou continuer votre chemin ?")
    if reponse=="entrer dans ce manoir":
        print("Vous vous approchez de la porte et essayer de l'ouvrir. Elle est fermée")
        reponse==input("souhaitez ouvrir la porte grâce à un coup de pied ou souhaitez vous abandonner ?")
        if reponse=="ouvrir la porte grâce à un coup de pied":
            print("Vous donnez un coup de pied de toute votre force dans la porte et vous réussissez à l'ouvir. Malheureusement vous vous faites mal à la jambe et vous perdez 10 de vie")
            vie=vie-10
            print(vie)
            print("Vous arrivez dans la salle principale")
            manoir()
        if reponse=="abandonner":
            print("En repartant vous appercevez une petite porte sur le côté et vous y entrez")
            print("Vous arrivez dans la salle principale")
            manoir()
    if reponse=="continuer votre chemin":
        print("vous marchez pendant encore un trentaine de minutes")
        print("la fatigue vous gagne vous vous reposez un instant sur une souche")
        print("malheureusement une épine se plante dans votre pied")
        print("vous reprenez votre route pendant plusieurs heure sans rencontrer de difficultés")
        print("puis lentement une fièvre vous gagne. Vous essayez de prendre du repos mais durant votre sommeil vous étes terrassés par l'infection")
        debut()
        
        
    
            
def manoir():
     print("la pièce est immense. Vous arrivez au milieu lorsque une des dalles en marbre sur laquelle vous marchez s'afaisse")
     print("toutes les issues de la pièce se trouvent soudainement bloquée par des grilles")
     print("une trappe s'ouvre au dessus de votre tete.")
     print("un hamster enragé vous tombe sur le crane")
     print("il essaye de vous mordre au cou. mais vous le dégagez du plat de votre main")
     print("Avant que vous n'ayez le temps de reprendre votre souffle c'est maintenant un boa qui s'enroule autour de votre tronc")
     x=randint(1,10)
     if x==10:
         print("vous arrivez à vous défaire de son étreinte mortelle et le déchirer en 2 avec votre force impressionante")
         reponse=input("les grilles se relèvent après ce combat harassant. essayez vous de sortir ou restez vous dans la pièce pour attendre une potentielle 3ème surprise?")
         if reponse=="sortir de la salle":
             print("vous passez la porte,losque une main sort du coin sombre derrière la porte.")
             print("cette main tient un machette. Vous n'avez pas le temps de vous enfuir que la main vous hache et vous découpe méticuleusemnt")
             debut()
         elif reponse=="rester dans la salle":
             print("vous entendez un cri rauque au loin")
             print("vous voyez une patte monstrueuse dépasser de la trappe")
             print("c'est un dragon titanesque qui s'écrase devant vous")
             reponse=input("de quelle couleur est donc ce dragon?")
             if reponse=="ocre":
                 print("vous le terrassez d'un seul regard. il s'écroule raide mort")
                 print("vous avez gagné. Bien joué")
             else:
                 print("il vous jette un regard meurtrier puis vous carbonise d'un jet de flammes bleues")
                 debut()
     else:
          print("le boa vous étouffe de son étreinte,vous succombez rapidement")
          début()
             

def chemingauche():
    print("vous marchez pendant 20 minutes. Vous vous frayez un chemin parmi les ronces")
    print("malheureusement il commence à pleuvoir")
    reponse=input("souhaitez vous continuer à marcher ou vous abriter ?")
    if reponse=="continuer à marcher":
        print("vous voyez une grotte au loin")
        continuer_a_marcher()
    if reponse=="s'abriter sous un arbre":
        print(" vous vous réfugiez sous l'arbre le plus proche. Vous attendez que la pluie passe. Une fois qu'il arrête de pleuvoir vous continuez à marcher")
        debut()
        
def continuer_a_marcher():
    print("vous voyez une grotte au loin. En vous approchant, vous appercevez un marchant")
    print("Le marchant : Regardez ce que je vend : Epée ; Prime ; Arc + Flêches ; Grosse potion ; Livre de math ; Rien")
    reponse=input("Que souhaitez-vous acheter ?")
    if reponse=="Epée":
        argent=argent-5
        inventaire.append("Epée")
        print("Vous acheter l'épée en échange de toutes vos pièces d'or")
    if reponse=="Prime":
        argent=argent-5
        inventaire.append("Prime")
        print("Vous acheter la boisson Prime en échange de toutes vos pièces d'or. Vous êtes un vrai supporter d'arsenal!")
    if reponse=="Arc + Flêches":
        argent=argent-5
        inventaire.append("Arc + Flêches")
        print("Vous acheter l'arc et les flêches en échange de toutes vos pièces d'or")
    if reponse=="Grosse potion":
        argent=argent-5
        inventaire.append("Grosse potion")
        print("Vous acheter la Grosse potion en échange de toutes vos pièces d'or")
    if reponse=="Livre de math":
        argent=argent-5
        inventaire.append("Livre de math")
        print("Vous acheter le livre de math en échange de toutes vos pièces d'or. La connaissance coûte chère=)")
    reponse==input("souhaitez vous ressortir prendre l'air ou vous enfoncez dans la grotte")
    if réponse=="sortir prendre l'air":
        ours()
    if réponse=="s'enfoncer dans la grotte":
        grotte()
def ours():
    print("vous sortez de la caverne, le soleil brille intensèment dans le ciel")
    print("vous entendez un craquement derrière vous")
    print(" un énorme ours se dresse devant vous, il s'élance vers vous")
    print("vous n'arrivez malheureusement pas à vous échapper il vous attrape et vous démenbre joyeusement. Vous passez un bon moment")
    début()
def grotte():
    print("la lumière s'éloigne alors que vous vous enfoncez dans la grotte")
    print("vous entendez une voix qui vous apelle sur votre droite")
    reponse=input("votre instint vous dit de la suivre mais une crainte s'installe en vous. Suivre la voix ou rebrousser chemin ?")
    if reponse=="suivre la voix":
        print("vous apercevez un petit diablotin en pierre au fond du couloir de pierre")
        print("il s'approche de vous en courant et sort une pique de fer rouillée.")
        print("vous comprenez l'erreur de votre décision")
        if "Arc+flèches" in inventaire:
            x=randint(1,50)
            if x==50:
                print("vous arrivez à lui décocher une flèche entre les 2 yeux avant qu'il vous atteigne.Il s'écroule mort sur le coup")
                i=randint(1,100)
                if i==100:
                    print("vous arrivez à lui arrachez un médaillon qu'il avait au cou et vous le mettez dans votre poche")
                    inventaire.append("médaillon du diablotin")
                    suite_grotte()
            else:
                print("il vous attrape alors que vous vous retournez et vous transperce le crane de sa barre de fer")
                debut()
    elif reponse=="rebrousser chemin":
        suite_grotte()

def suite_grotte():
    print("vous voyez une lumière au loin")
    print("vous vous approchez et vous apercevez la sortie devant vous")
    print("la sortie est surélevée par apport à vous. Un petit gouffre s'étend entre vous et la liberté")
    reponse=input("tentez vous le saut ?")
    if reponse== "je tente le saut":
        print("vous vous élancez au dessus du vide")
        if "prime" in inventaire:
            k=randint(0,10000)
            if k==10000:
                print("vous traversez le gouffre d'un saut magistral")
                print("vous sortez enfin de l'antre obscur. la lumière vous caresse le visage")
                print("vous avez gagné bravo")
            else:
                print(" le rebord vous échappe et vous chutez dans les ténèbres. vos os se disloquent")
                debut()
        elif "médaillon_de_diablotin" in inventaire:
            print("vous vous racrochez au bord du rebord. Vous passez par la sortie. La lumière caresse votre visage")
            print("vous avez gagné. bien joué")
        else:
            print("vous etes épuisé par votre journée. votre saut est trop mou. vous n'atteignez pas le rebord")
            début()
    if reponse=="je ne tente pas le saut":
        print("vous glissez malencontreusement sur une minuscule pierre. le vide vous emporte")
        debut()
        
        

debut()














