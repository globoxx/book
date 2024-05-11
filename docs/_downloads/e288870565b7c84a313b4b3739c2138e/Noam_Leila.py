inventaire = []
santé_mentale = 100
Game_over = False

def enquete():
    global santé_mentale
    global Game_over
    reponse = input("Où souhaitez vous aller ? A la cave, à l'étage ou dans la salle de bain ?")
    while "cave" not in reponse and "Cave" not in reponse and "etage" not in reponse and "étage" not in reponse and "Etage" not in reponse and "salle de bain" not in reponse and "Salle de bain" not in reponse:
        reponse = input("Où souhaitez vous aller ? A la cave, à l'étage ou dans la salle de bain ?")
        
    if "cave" in reponse or "Cave" in reponse:
        print("En descendant à la cave, vous entendez des chants horrifique venant du fantôme, cela vous fait baisser votre santée mentale de 15%")
        santé_mentale = santé_mentale - 15
        print("Vous ne trouvez rien de plus à la cave")
        
    elif "etage" in reponse or "étage" in reponse or "Etage" in reponse:
        print("En arrivant à l'étage les lumières s'éteignent, vous perdez 15% de santé mentale")
        santé_mentale = santé_mentale - 15
        
        reponse = input("Deux pièces se présentent à vous, la chambre et le bureau, où souhaitez vous aller ?")
        while "chambre" not in reponse and "Chambre" not in reponse and "bureau" not in reponse and "Bureau" not in reponse:
            reponse = input("Deux pièces se présentent à vous, la chambre et le bureau, où souhaitez vous aller ?")
        
        if "chambre" in reponse or "Chambre" in reponse:
            print("En entrant dans la chambre, vous voyez à votre gauche une armoire remplie de vêtement féminin et sur votre droite il y a un lit")
            reponse = input("Souhaitez vous vous reposer dans le lit ?")
            while "oui" not in reponse and "Oui" not in reponse and "non" not in reponse and "Non" not in reponse:
                reponse = input("Souhaitez vous vous reposer dans le lit ?")
                
            if "oui" in reponse or "Oui" in reponse:
                print("Malheureusement vous ne vous réveillerez jamais, le fantôme a profité de votre sommeil pour mettre fin à vos jours...")
                Game_over = True
                
            elif "non" or "Non" in reponse:
                reponse = input("Souhaitez vous alors aller dans le bureau ?")
                while "oui" not in reponse and "Oui" not in reponse and "non" not in reponse and "Non" not in reponse:
                    reponse = input("Souhaitez vous alors aller dans le bureau ?")
                    
                if "oui" in reponse or "Oui" in reponse:
                    print("En arrivant dans le bureau, vous glissez sur un stylo et vous vous énuquez sur le rebord du bureau, CHEH !")
                    Game_over = True
                
        if "bureau" in reponse or "Bureau" in reponse:
            print("En arrivant dans le bureau, vous glissez sur un stylo et vous vous énuquez sur le rebord du bureau, CHEH !")
            Game_over = True
            
    elif "salle de bain" in reponse or "Salle de bain" in reponse:
        print("Vous entrez dans la salle de bain et sur le rebord du lavabo vous trouvez des médicament. Ils permettent de restaurer 25 % de santé mentale")
        reponse = input("Voulez vous les utiliser maintenant ou les garder pour plus tard ?")
        while "utiliser" not in reponse and "Utiliser" not in reponse and "maintenant" not in reponse and "Maintenant" not in reponse and "garder" not in reponse and "Garder" not in reponse and "plus tard" not in reponse and "Plus tard" not in reponse:
            reponse = input("Voulez vous les utiliser maintenant ou les garder pour plus tard ?")
            
        if "utiliser" in reponse or "Utiliser" in reponse or "maintenant" in reponse or "Maintenant" in reponse:
            print("Votre santé mentale augmente de 25% !")
            santé_mentale = santé_mentale + 25
            
        elif "garder" in reponse or "Garder" in reponse or "plus tard" in reponse or "Plus tard" in reponse:
            inventaire.append("Médicaments")
            print("Les médicaments sont maintenant dans votre inventaire !")
        
        if not Game_over:
            print("Vous êtes maintenant devant un miroir et le fantôme est susceptible d'y avoir laissé des traces, vous pourriez les voir avec une lampe UV !")
            if "Lampe UV" in inventaire:
                print("Vous avez une lampe UV ! Grâce à elle vous détectez les empreintes du fantôme, bravo !")
                
            if "Lampe UV" not in inventaire:
                print("Vous n'avez pas de lampe UV, tant pis !")
                
            if not Game_over:
                reponse = input("Il y a une douche dans la salle de bain, souhaitez vous vous doucher ?")
                while "oui" not in reponse and "Oui" not in reponse and "non" not in reponse and "Non" not in reponse:
                    reponse = input("Il y a une douche dans la salle de bain, souhaitez vous vous doucher ?")
                    
                if "oui" in reponse or "Oui" in reponse:
                    print("Vous êtes maintenant tout beau et tout propre ! Vous pouvez retourner à vos activités !")
                
                
            
            
            
        
        
        
    if not Game_over:
        reponse = input("Souhaitez vous continuer votre enquête dans les autres pièces ou pensez vous que vous avez assez de preuves et vous mettez fin à l'enquête ?")
        while "continuer" not in reponse and "Continuer" not in reponse and "fin" not in reponse and "Fin" not in reponse and "mettre fin" not in reponse and "Mettre fin" not in reponse:
            reponse = input("Souhaitez vous continuer votre enquête dans les autres pièces ou pensez vous que vous avez assez de preuves et vous mettez fin à l'enquête ?")
            
        if "continuer" in reponse or "Continuer" in reponse:
            enquete()
            
            
        elif "fin" in reponse or "Fin" in reponse or "mettre fin" in reponse or "Mettre fin" in reponse:
            print("Vous pensiez pouvoir sortir de la maison sans problèmes mais à la dernière minute le fantôme lance une chasse contre vous, vous devez choisir un endroit où vous cacher !")
            reponse = input("Où souhaitez vous vous cacher ? Dans l'armoire ou sous le lit ?")
            while "armoire" not in reponse and "Armoire" not in reponse and "sous le lit" not in reponse and "Sous le lit" not in reponse and "lit" not in reponse and "Lit" not in reponse:
                reponse = input("Où souhaitez vous vous cacher ? Dans l'armoire ou sous le lit ?")
                
            if "armoire" in reponse or "Armoire" in reponse:
                print("Malheureusement votre cachette n'était pas assez élaborée pour fuir le fantôme, il vous attrape et vous mourrez dans l'agonie...")
                Game_over = True
                
            elif "sous le lit" in reponse or "Sous le lit" in reponse or "lit" in reponse or "Lit" in reponse:
                print("Vous survivez à la chasse du fantôme mais c'était moins une ! Vous avez perdu 50% de santé mentale")
                santé_mentale = santé_mentale - 50
                
                if "Médicaments" in inventaire:
                    print("Votre santé mentale est à", santé_mentale)
                    reponse = input("Voulez vous utlisier les médicaments afin de récupérer 25% de santé mentale ?")
                    while "oui" not in reponse and "Oui" not in reponse and "non" not in reponse and "Non" not in reponse:
                        reponse = input("Voulez vous utlisier les médicaments afin de récupérer 25% de santé mentale ?")
                        
                    if "oui" in reponse or "Oui" in reponse:
                        print("Vous récupérez 25% de santé mentale !")
                        santé_mentale = santé_mentale + 25
                        
                if not Game_over:
                    print("Vous sortez enfin de cette maison dont vous pensiez ne plus pouvoir vous échapper")
                    if santé_mentale >= 25:
                        print("Vous avez réussi à sortir, bravo !")
                        print("Vous allez maintenant avoir devant vous une liste avec trois type de fantômes et leurs caractéristiques, vous aller devoirs trouver celui qui réside dans la maison")
                        print("Le Démon, mâle : - Chasse très souvent ; - Est silencieux ; - Possible de l'invoquer grâce à un cercle satanique.")
                        print("La Banshee, femelle : - Laisse entendre sa voix, parfois comparée aux chants des sirènes ; - Laisse parfois des traces de son passage ; - Aime le jardinage.")
                        print("Le Poltergeist, sexe inconnu : - Vous lance parfois des objets dessus ; - Peut imiter certaines de vos actions ; - S'entraine parfois au chant sous la douche.")
                        reponse = input("Lequel voulez vous choisir ?")
                        while "demon" not in reponse and "démon" not in reponse and "Demon" not in reponse and "Démon" not in reponse and "banshee" not in reponse and "Banshee" not in reponse and "poltergeist" not in reponse and "Poltergeist":
                            reponse = input("Lequel voulez vous choisir ?")
                            
                        if "demon" in reponse or "démon" in reponse or "Demon" in reponse or "Démon" in reponse:
                            Game_over = True
                            
                        elif "banshee" in reponse or "Banshee" in reponse:
                            print("VICTOIRE, vous avez trouvé l'identité qui se cachait à l'intérieur de la maison !")
                            
                        else:
                            Game_over = True
                            
                        
                        
                        
                        
                    else:
                        print("En sortant, votre santé mentale est tellement basse que vous devenez fou")
                        Game_over = True
                    
    

print("Bienvenue sur Poltergeist Proximity, le jeu où les fantômes vous hante !")
print("Vous allez être dirigé devant la maison la plus hantée de la ville et votre devoir est de découvir l'identité du fantôme qui se cache à l'intérieur.")

    

reponse = input("Voulez vous débuter une partie ?")
while "oui" not in reponse and "Oui" not in reponse:
    reponse = input("Voulez vous débuter une partie ?")
    
if "oui" in reponse or "Oui" in reponse:
    print("Vous vous retrouvez dans le quartier le plus sombre de la ville")
    print("La maison se présente à vous : La Willow Street House")
    print("Vous entrez à présent dans la maison")
    print("Vous débutez avec une santé mentale de 100%, faites y attention ou vous deviendrez fou !")
    print("En marchant petit à petit dans la maison vous tombez sur une pièce sombre, un objet brillant y est posé sur le sol")

reponse = input("Souhaitez vous rentrez à l'intérieur de cette pièce ou continuer plus loin dans la maison ?")
while "continuer" not in reponse and "Continuer" not in reponse and "rentrer" not in reponse and "Rentrer" not in reponse:
    reponse = input("Souhaitez vous rentrez à l'intérieur de cette pièce ou continuer plus loin dans la maison ?")


        
if "continuer" in reponse or "Continuer" in reponse:
    reponse = input("En continuant plus loin dans la maison vous trouvez une lampe à ultras-violets, souhaitez vous la ramasser ?")
    while "oui" not in reponse and "Oui" not in reponse and "non" not in reponse and "Non" not in reponse:
        reponse = input("En continuant plus loin dans la maison vous trouvez une lampe à ultras-violets, souhaitez vous la ramasser ?")
        
    if "oui" in reponse or "Oui" in reponse:
        inventaire.append("Lampe UV")
        print("La lampe UV est maintenant dans votre inventaire, elle vous servira peut-être plus tard !")
    


elif "rentrer" in reponse or "Rentrer" in reponse:
    print("Vous perdez 20% de santée mentale")
    santé_mentale = santé_mentale - 20
    print("Vous découvrez que l'objet brillant est une petite statuette")
    reponse = input("Souhaitez vous ramasser la petite statuette ?")
    while "oui" not in reponse and "Oui" not in reponse and "non" not in reponse and "Non" not in reponse:
        reponse = input("Souhaitez vous ramasser la petite statuette ?")
    
    if "oui" in reponse or "Oui" in reponse:
        print("La statuette se met à tournoyer autour de vous, le fantôme apparait et sans que vous ayez le temps de vous cacher, il vous tue !")
        Game_over = True
        
        

if not Game_over:
    print("A présent, vous continuez à marcher dans le couloir principal")
    enquete()
        
                

if Game_over:
    print("GAME OVER, vous n'avez malheureusement pas réussi à découvrir l'identité du fantôme!")