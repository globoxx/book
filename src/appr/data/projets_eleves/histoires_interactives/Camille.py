from random import*

print("Vous rentrez d'un spectacle de flûte et êtes dans la rue et voyez la plante de vos rêves à 10 francs dans une vitrine") 
print("Vous n'avez pas d'argent mais la voulez tout de suite") 
print("Vous devez trouver l'argent maintenant sans rentrer chez vous avant que le magasin ne ferme") 

chiffre = [2, 4, 6, 8]

def debut():
    argent = 0 
    inventaire = ["flûte"] 
    print("Voulez-vous aller dans la ruelle de droite ou de gauche?") 
    reponse = input() 
    if reponse == "droite": 
        print("Vous tombez sur un mendiant avec un verre rempli de pièces") 
        print("Vous volez une pièce ou passez votre chemin?") 
        reponse = input() 
        if reponse == "voler une pièce": 
            print("Vous avez réussi à lui voler deux pièces et un dé!") 
            print("Vous avez maintenant 4 francs de plus") 
            argent = argent + 4 
            inventaire.append("dé")
        elif reponse == "passer mon chemin":
            print("Vous passer donc votre chemn avec un regard de pitié")
            
    elif reponse == "gauche": 
        print("Une vieille dame vous bouscule sans faire exprès et fait tomber son gros sac de courses") 
        print("Comme vous l'avez aidée à ramasser ses trucs, elle vous donne 3 francs pour vous remercier") 
        argent = argent + 3 
 
    print("Vous arrivez enfin sur la place du marché où un musicien de rue est entrain de jouer") 
    if "flûte" in inventaire:
        print("Voulez-vous jouer de la flûte avec lui ou continuer à marcher?") 
        reponse = input() 
        if reponse == "jouer avec lui": 
            print("Le musicien se fâche et vous poursuit en courant") 
            print("Vous arrivez à le semer mais dans la course vous avez perdu tout ce que vous aviez sauf votre flûte") 
            print("Vous vous retrouver malheureusement au début")
            if "dé" in inventaire:
                inventaire.remove("dé")
            argent = argent - argent
            debut() 
     
        elif reponse == "continuer à marcher": 
            print("Vous voyez un attroupement de personnes et vous approchez") 
            print("Vous voyez que c'est un jeu de hasard sur une petite table pour gagner de l'argent avec un dé") 
            if "dé" in inventaire:
                print("Grâce au mendiant vous avez heureusement un dé sur vous")
                print("Voulez-vous tenter votre chance?")
                reponse = input()
                if reponse == "oui": 
                    print("Grâce au mendiant vous avez un dé sur vous et vous vous mettez donc à table") 
                    print("Vous devez tomber sur un 2 pour gagner 7 francs ")
                    chiffre_tire = choice(chiffre)
                    print("Vous avez tiré le chiffre", chiffre_tire)
                    if chiffre_tire == 2:
                        print("Super! Vous avez gagné 10 francs")
                    else:
                        print("Mince, Vous avez perdu! Pas grave")
                
                elif reponse == "non": 
                    print("Vous continuez alors votre quête d'argent") 
 
            else: 
                print("Vous n'avez malheureusement pas de dé et continuez votre quête d'argent") 
 
 
    print("Vous retombez par hasard devant le magasin qui vend la plante et il ferme dans 2 minutes") 
    if argent >= 10: 
        print("Trop bien! Vous avez pu acheter votre super plante!") 
 
    elif argent < 10: 
        print("Oups! Vous n'avez malheureusement pas assez de moulaga pour votre chère plante. Revenez un autre jour")
 
debut() 
