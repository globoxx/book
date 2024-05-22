inventaire =[]


metier = input("Voulez-vous devenir physicien ou un passioné d'aviation? (physicien/aviation)")


reponse = input("Vous partez en vacance pour rejoindre votre famille au Canada. Vous embarquez dans un avion et décollez. Vous êtes installé à l'arrière de l'avion. Une personne placée en first place à l'avant de l'avion fait un malaise. Souhaitez-vous lui prendre ça place?")

if reponse == "oui":
    reponse = input("Après votre déplacement imprévu, l'hôtesse vous demande si vous souhaitez prendre quelques choses?")
    if reponse == "oui":
        reponse = input("Que voulez vous prendre ?(eau,coca,poulet,fanta?)")
        if reponse == "eau":
            inventaire.append("eau")
        elif reponse == "coca":
            inventaire.append("coca")
        elif reponse == "poulet":
            inventaire.append("poulet")
        elif reponse == "fanta":
            inventaire.append("fanta")

    reponse = input("le voyage continu, l'hôtesse revient en vous proposant des souvenirs de votre futur voyage.Elle vous propose un grand porte bonheur, voulez vous le prendre ?")
    if reponse == "oui":
        inventaire.append("grand porte bohneur")

    print("Le temp passe et vous remarquez que les hôtesse commencent à s'agiter. Les alarmes retentissent dans tout l'avion et vous remarquez à travers l'ublo qu'il manque une aille.")
    if metier == "aviation":
        print("Malheureusement vous ne pouvez rien faire et mourrez lors du crash!!")
    elif "poulet" in inventaire:
        print("Vous allez aidé le pilot à diriger l'avion puisque vous arrivez à lui expliquer les différences forces exercées sur l'avion et atterrisez sur une piste de secours avec succès")
    else:
        print("Puisque vous n'avez rien mangé depuis un moment, vous n'étiez pas en forme et vous avez fait une erreur dans vos calcul et vous vous crachez dans l'océan.Apres un moment de coma, vous vous réveillez et remarquez que vous êtes le seul survivant. Vous avez survécu garce à un bout de chaise qui vous à fait flotter.")
        if "grand porte bohneur" in inventaire:
            print("Vous êtes malheureusement trop lourd a cause de votre porte bonheur et mourrez noyer")
        else:
            print ("Les secours arrivent et vous survivez!")
elif reponse == "non":
    print("Vous êtes en business classe depuis plus de 3h et le vole dure encore un long moment. A côté de vous se trouve un bébé qui pleure.")
    reponse = input("Vous allez demander aux parents s'ils ont besoin d'aide ? (oui/non)")
    if reponse == "oui":
        print("Vous demandez poliment aux parents s'ils veulent aller souffler au bar de l'avion pendant que vous vous occupez de leur bébé. Vous vous êtes occupé du bébé pendant plus d'une heure et les parents sont revenus s'occuper de leur bébé qui s'endort après 5 minutes.")
    print("C'est l'heure du repas et l'hôtesse vient vous proposer les deux formules de repas qui sont à choix.La formule 1 se compose d'une cuisse de poulet ainsi que de la purée de pomme de terre avec un sauté de légumes.La formule 2 se compose d'une entrecôte de boeuf et de pomme de terre sautée avec son nid de légumes du jour.")
    reponse = input("Quelle formule allez-vous choisir ?(1/2)")
    if reponse == "2":
        print("L'entrecôte était mal cuite et vous faites une intoxication alimentaire et mourrez!   Fin")
    elif reponse == "1":
        print("Vous vous régalez et vous appelez l'hôtesse pour lui demander une boisson sucrée.L'hôtesse vous amenez votre boisson et la renversez sans faire exprès sur votre jambe à cause d'une turbulence violente")
        reponse == input("Vous vous énervez ?(oui/non)")
        if reponse == "oui":
            print("Vous lui criez dessus et l'hôtesse s'excuse platement puis repars vous amenez une nouvelle boisson ainsi qu'un dessert.")
        else:
            print("l'hôtesse s'excuse et pour vous remerciez de votre sang froid et vous amène en first place en guise de remerciement de votre comportement")
        print("Soudain, l'avion subit de violentes turbulences et une hôtesse fait une annonce et demande s'il y a un pilote à bord mais personne ne répond.")
        reponse == input("Voulez-vous faire semblant d'être un pilote ?")
        if reponse == "oui":
            print("Vous levez la main et l'hôtesse vient vers vous et vous demande de la suivre. Une fois arrivez au cabinet de pilotage, l'hôtesse vous annonce la mort d'un pilote à cause d'une intoxication alimentaire du à l'entrecôte de boeuf.")
            if metier == "aviation":
                print("Etant donné que vous êtes un passionné d'aviation, vous arrivez à aider l'autre pilote à atterrir dans l'océan. FIN")
            else:
                print("Vous essayez quand même, mais vous ratez votre atterrissage à cause d'un manque de connaissances sur les avions, tout ça par ce que vous dormiez en cours lorsque votre prof de physique parlait d'avions. FIN ")
        if reponse == "non":
            print("L'avion crash et vous mourrez !   FIN")    
        
    
  

