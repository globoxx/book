from time import sleep
vie = 5
inventaire = []
print("Vous êtes coincé sur une île déserte suite à un crash d'avion dont vous êtes le seul survivant")
print ("vous avez 5 point de vie")
sleep(0.5)

def game_over(x):
    for i in "GAME OVER!!":
        print (i, end='')
        sleep(x*0.1)
        
def victoire():
    for i in "VICTOIRE !!":
        print (i, end='')
        sleep(0.1)
    if vie == 5:
        print ("")
        print ("Bien joué ! Vous avez su dévier tous les pièges ;) Vous gagnez un bonbon virtuel !")

print("Vous marchez le long de la plage mais arrivez à un croisement. Aller dans la jungle ou continuer sur la plage ? ")
reponse = input("Jungle ou plage ?")

if reponse ==("plage"):
    print ("En marchant vous tomber sur une étoile de mer")
    sleep(0.5)
    reponse = input("La ramasser ? ")
    if reponse == ("oui"):
        sleep(0.5)
        print ("Elle était vénéneuse, -3 point de vie")
        vie = vie - 3
    else:
        print ("Vous continuez votre route")
        sleep(0.5)
    reponse = input ("Sur la plage, vous apercevez des bouts de bois secs ainsi que des silexs. Les ramassez-vous pour vous faire un feu ? ")
    if reponse == ("oui"):
        print ("Le soir arrive et vous vous faites du feu pour vous réchauffer")
        sleep(0.5)
    else:
        print ("Vous avez froid durant toute la nuit, -2 point de vie")
        vie = vie - 2
            
    if vie > 0 :
        print ("Le lendemain vous vous réveiller et vous voyez un bateau au loin")
        sleep(0.5)
    else:
        print ("les pièges ont eut raison de vous!")
        game_over(1)

    if vie>0:
        reponse = input("Nager jusqu'au bateau ou crier en espérant qu'il vous entende ?")

    if reponse == ("crier"):
        print ("Le bateau vous apperçoit et vient vous secourir.")
        sleep(0.5)
        victoire()
        sleep(0.5)

    if reponse == ("nager"):
        print ("En essayant de le rattraper des algues s'entourent autour de vos jambes et vous vous évanouissez")
        sleep(0.5)
        game_over(1)
    
if reponse == ("jungle"):
    print("En marchant vous trouvez une hache plantée sur un tronc d'arbre")
    sleep(0.5)
    reponse = input("La ramasser, oui ou non ?")
    if reponse == ("oui"):
        inventaire.append("Hache")
    sleep(0.5)
    print("Vous continuez votre route mais un gorille surgit et vous poursuit")
    sleep(0.5)        
    if "Hache" in inventaire:
        print("Vous tuez le gorille")
        sleep(0.5)
        reponse=input("Cuisiner le gorille pour le manger ?")
        if reponse ==("oui"):
            print ("vous avez repris des forces et allez dormir. +5 point de vie")
            vie=vie+5
            sleep (0.5)
            print ("le lendemain vous vous baladez sur la plage et trouvez un téléphone prépayer sur lequel il reste un appel")
            sleep(0.5)
            reponse=input("appelez les secours?")
            if reponse==("oui"):
                print ("vous parvenez à appeller un hélicoptère qui vient vous sauver")
                sleep(0.5)
                if vie==10:
                    print ("Bien joué ! Vous avez su dévier tous les pièges ;) Vous gagnez un bonbon virtuel !")
                    sleep(0.5)
                    victoire()
                else:
                    victoire()
            else:
                print ("vous restez seul sur votre île pour toujours")
                sleep(0.5)
                game_over(2)
        else:
            print ("vous mourrez de faim!")
            game_over(1)
    else:    
        print("le gorille vous mange.")
        game_over(1)