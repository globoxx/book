vie = 100
    
inventaire = []

def debut () :
        global vie
        reponse = input ("Prendre la ruelle ou continuer tout droit ?")
        if reponse == "Prendre la ruelle" :
            print ("Vous tombez sur une Goule")
            reponse = input ("Prendre la batte de baseball ou les gants de boxe ?")
            if reponse == "La batte de baseball" :
                print ("La batte de baseball se casse et la Goule vous dévore")
                print ("GAME OVER")
        
            elif reponse == "Les gants de boxe" :
                print ("Vous tuez la Goule")
                print ("Vous récupérez les gants de boxe")
                inventaire.append ("gants de boxe")
                print ("Votre vie augmente de 30")
                vie += 30
                print ("Vous avez",130,"points de vie")
            
                print ("Vous sortez de la ruelle et vous tombez sur un zombie")
                reponse = input ("Combattre le zombie ou s'enfuire ?")
                if reponse == "S'enfuire" :
                    print ("Vous revenez sur vos pas")
                    debut()
                    
                elif reponse == "Combattre le zombie" :
                    print ("Vous gagnez mais vous êtes contaminé")
                    print ("Votre vie diminue de 40")
                    vie -= 40
                    print ("Vous avez",90,"points de vie")
               
                    print ("Vous devez trouvez un remède pour vous soignez")
                    reponse = input ("Aller dans une pharmacie ou aller à l'hôpital ?")
                    if reponse == "Aller dans une pharmacie" :
                        print ("Vous ne trouvez rien et devenez un zombie")
                        print ("GAME OVER")
                    
                    elif reponse == "Aller à l'hôpital" :
                        print ("Sur le chemin vous trouvez une potion violet aux propriétées inconnues")
                        reponse = input ("Boire la potion ou continuer d'aller à l'hôpital ?")
                        if reponse == "Aller à l'hôpital" :
                            print ("Vous arrivez à l'hôpital, vous trouvez un médicament qui vous transforme en chauve-souris")
                            print ("Vous restez donc coincé dans la dimension")
                            print ("GAME OVER")

                        elif reponse == "Boire la potion" :
                            print ("Vous guérissez et obtenez la capacité de voler")
                            print ("Votre vie augmente de 100")
                            vie += 100
                            print ("Vous avez",190,"points de vie")
    
                            print ("Vous avancez dans la ville et trouvez un coffre fort verouillé")
                            reponse = input ("Chercher la clé ou casser le coffre avec un pied de biche ?")
                            if reponse == "Chercher la clé" :
                                print ("En cherchant la clé vous tombez dans une bouche d'égout")
                                print ("Arrivé en bas, vous rencontrez les tortues ninja")
                                print ("Ils vous aident à retourner dans votre dimension")
                                print ("VICTOIRE")
        
                            elif reponse == "Casser le coffre" :
                                print ("Le coffre est vide et vous vous faites aspirez dedans")
                                print ("Vous retourenz dans la ruelle")
                                debut()
                                
        elif reponse == "Continuer tout droit" :
            print ("Vous rencontrez une fille")
            reponse = input ("Continuer tout droit ou aller lui parler ?")
            if reponse == "Continuer tout droit" :
                print ("Vous tomber sur un groupe qui veut vous guidez vers leur repère")
                reponse = input ("Les ignorez et continuer ou les suivre ?")
                if reponse == "Continuer tout droit" :
                    print ("Vous tomber sur une orde de loup-garous")
                    print ("Vous ne pouvez pas vous défendre, vous mourrez déchicté")
                    print ("GAME OVER")
                
                elif reponse == "Les suivre" :
                    print ("Ils vous proposent soit de boire un jus soit de manger un cake")
                    reponse = input ("Boire le jus ou manger le cake ?")
                    if reponse == "Manger le cake" :
                        print ("Vous êtes empoisonné, et perdez 200 point de vie")
                        print ("Vous mourrez car vous avez perdu tous vos points de vie")
                        vie -= 200
                        print ("Vous avez",-10,"points de vie")
                        print ("GAME OVER")
                        
                    elif reponse == "Boire le jus" :
                        print ("Vous perdez connaisances et vous dévore car en réalité ils sont canibales")
                        print ("GAME OVER")
                        
            elif reponse == "Aller lui parler" :
                print ("Vous décidez de devenir coéquipier et continuer votre chemin")
                print ("Soudain, vous tombez sur une maison sur une plage")
                reponse = input ("Rentrer dans la maison ou continuer votre chemin ?")
                if reponse == "Continuer mon chemin" :
                    print ("En continuant votre chemin un tsunami arrive et vous engloutit")
                    print ("GAME OVER")
                    
                elif reponse == "Rentrer dans la maison" :
                    print ("Des gens s'y trouvent déjà et ils vous prenent en otage")
                    print ("Une fois les kidnapeurs parti de la pièce, la fille sort un couteau et découpe la corde")
                    print ("Vous êtes désormais libre mais vous devez trouvez une sortie")
                    print ("La fille trouve une fenêtre et voit une piscine en bas, elle décide donc de sauter dedans")
                    reponse = input ("sauter aussi ou trouver une autre sortie ?")
                    if reponse == "Sauter" :
                        print ("Vous sautez et durant votre chte vous vous rendez compte que la piscine est vide")
                        print ("Vous mourrez tous les deux écrasé")
                        print ("GAME OVER")
                        
                    elif reponse == "Trouver une autre sortie" :
                        print ("Vous tombez dans une pièce avec une trappe")
                        print ("Vous arrivez au point de départ")
                        debut()
                        
        
    
                            
                            
                            
print ("Vous avez attérit dans une autre dimension appelée Borderland")
print ("Vous êtes dans une ville abondonnée et à votre gauche se trouve une ruelle")

debut()

    
