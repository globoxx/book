inventaire = []
vie= 100

def début():
    global vie
    print("vous êtes seul dans un bar miteux, vous écoutez du Jazz. Tout d'un coupvous recevez  un coup derrière la tête et vous vous évanouissez.")
    print("lorsque vous vousréveillez vous êtes dans une pièce sans fenêtre, devant vous un homme se tient dans la pénombre. Il voustend une clef.votre vie est a 100%")
    reponse=input(" la prendre ou la refuser ?")
    while reponse not in ["la prendre", "la refuser"]:
        reponse=input("la prendre ou la refuser ?")
    if reponse=="la prendre":
        print("vous la mettez dans votre inventaire")
        inventaire.append("clef")
    print("l'homme vous explique les règles. Il vous dit que vous devez vous échapper de cet endroit mais il vous conseille d'être prudent, car il y'a entre ces murs une chose qui vous cherche et qui vous jouera des tours. Mais retenez bien ceci: soyez illogique!")
    print("Il vous montre une porte, vous la passez et rentrez dans un couloir. Vous arrivez devant deux portes, la première a des écritures en latin et la deuxième a un visage découpé pendu à la poignée")
    reponse=input("la porte numéro 1 ou la porte numéro 2?")
    while reponse not in ["la porte numéro 1", "la porte numéro 2"]:
        reponse=input("la porte numéro 1 ou la porte numéro 2 ?")
        
    if reponse=="la porte numéro 1":
        print("vous traversez la porte, mais ressentez une atmosphère étrange")
        print("vous rentrez dans une pièce lumineuse,une personne à l'allure humaine vous dit de la suivre vers la sortie. La suivez vous?")
        reponse = input("ressortir ou la suivre ?")
        while reponse not in ["ressortir", "la suivre"]:
            reponse = input("ressortir ou la suivre ?")
        if reponse=="la suivre":
            print("malheur!!!! elle vous a coupé en morceau pour nourrir le monstre, vous mourrez")
            début()
        elif reponse=="ressortir":
            print("vous sortez de la pièce et vagabondez dans l'espoir de trouver une sortie")
            mannequin()        
    elif reponse=="la porte numéro 2":
        print("vous vous trouvez dans un couloir ensanglanté. Le monstre vous à entendu. Courrez!!")
        print("vous tournez à gauche, puis à droite. Vous tombez sur une petite fille qui pleure")
        reponse=input("voulez vous la prendre ou la laisser?")
        while reponse not in  ["la prendre", "la laisser"]:
            reponse=input("voulez vous la prendre ou la laisser?")
        if reponse=="la prendre":
            print("la petite fille prend une forme exécrable et vous charcute le bras. Vous perdez 75% de vie, mais vous réussissez à vous enfuir")
            vie = vie-25
        elif reponse=="la laisser":
            print("vous la laissez, par chance il ne vous arrive rien et vous continuez tout droit")
            print("vous arrivez vers un balcon, dehors il fait nuit, vous voyez que vous êtes encore haut dans le bâtiment. Mais ne vous découragez pas vous y arriverez!")
            mannequin()

def mannequin():
    global vie
    print(" vous marchez et vous tombez né à né face à un mannequin dans une sorte de sale d'éxpérimentation, sur celui-ci se troue une feuille, derrière lui il y'a une machine avec 4 boutons, un jaune un bleu et un vert")
    print(" sur la feuille il y'a des instructions pour résoudre une énigme...le bouton rouge doit être appuyé après le bleu...le jaune est avant le bleu...le bouton vert doit être appuyé après le bleu, mais pas avant le jaune")
    reponse=input("laquelle de ses possibilités est la bonne?, possibilité une: jaune,bleu,vert,rouge - possibilité deux: bleu,vert,rouge,jaune - possibilité trois: bleu,rouge,vert,jaune")
    while reponse not in ["possibilité une", "possibilité deux" , "possibilité trois"]:
        reponse=input("laquelle de ses possibilités est la bonne?, possibilité une: jaune,bleu,vert,rouge - possibilité deux: bleu,vert,rouge,jaune - possibilité trois: bleu,rouge,vert,jaune")
    if reponse=="possibilité deux":
        print("vous ratez et vous prenez des dégats, 25% de vie en moins")
        vie= vie-25
        print("vous êtes mort")
        début()
    elif reponse=="possibilité trois" :
        print("vous ratez et vous prenez des dégats, 25% de vie en moins")
        vie= vie-25
        print("vous êtes mort")
        début()
    elif reponse=="possibilité une":
        print("vous réussissez avec brio et accedez à la suite. Bravo!")
        print("après cette épreuve quelques mètres plus loin se trouve une salle. Sur les murs se trouvent une matière chaude et visqueuse, au fond de cette salle se trouve une porte qui requiert une clef")
        print(" si vous avez la clef vous la passez, à contrario vous mourrez car le monstre vous attrape")
        if "clef" in inventaire:
            reponse=input("derrière cette salle se trouve une table avec un coeur et une pomme et cela fait 48h que vous n'avez pas mangé. Manger la pomme ou le coeur?")
            while reponse not in ["la pomme", "le coeur"]:
                reponse=input("Manger la pomme ou le coeur?")
            if reponse=="la pomme":
                print("la pomme était en fait un piège, elle est toxique, hélas vous êtes condamné à errer ici jusqu'a votre dernier souflle et qu'elle vous consume. Bonne chance.. agonisez!!!")
                début()
            elif reponse=="le coeur":
                print("SURPRISE, le coeur était en réalité un trompe l'oeil et vous reprenez donc des forces")
                print(" vous patientez quelques instants, et voyez devant vous une porte s'ouvrir, vous êtes libre et sentez enfin l'odeur de la liberté.")
        else:
            début()


début()

   