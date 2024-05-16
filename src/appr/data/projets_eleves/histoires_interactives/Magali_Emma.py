print("Le jeu commence maintenant, votre vie est à 10")
vie = 10

def Australie():
    while True:
        reponse = input("Voulez-vous aller en Allemagne ou en Australie? (entrez 'Allemagne' ou 'Australie') ")
        if reponse.lower() == "allemagne":
            Allemagne()
            break
        elif reponse.lower() == "australie":
            print("Vous êtes donc bien en Australie, vous vous retrouvez au bord d'une rivière.")
            while True:
                reponse = input("Voulez-vous traverser la rivière? (oui/non) ")
                if reponse.lower() == "oui":
                    print("Vous ne savez pas nager, c'était un élément à ne pas négliger, vous êtes nul.")
                    print("Votre vie diminue de 1")
                    global vie
                    vie -= 1
                    if vie <= 0:
                        print("Vous avez perdu! Votre vie est à 0.")
                        return
                    while True:
                        reponse = input("Voulez-vous demander de l'aide? (oui/non) ")
                        if reponse.lower() == "oui":
                            print("C'est une touriste allemande qui vous sauve avec son gros bateau bleu, elle vous emmène dans un restaurant sur le bord de plage.")
                            print("Acceptez-vous de manger avec elle malgré le fait que vous ayez une copine?")
                            while True:
                                reponse = input("Oui ou non? ")
                                if reponse.lower() == "oui":
                                    print("Vous mangez donc avec elle et pendant le repas, elle vous demande en mariage.")
                                    while True:
                                        reponse = input("Est-ce que vous acceptez? (oui/non) ")
                                        if reponse.lower() == "oui":
                                            print("Pour célébrer cela, vous décidez ensemble d'aller en Allemagne pour l'annoncer à sa famille.")
                                            Allemagne()
                                            return
                                        elif reponse.lower() == "non":
                                            print("Très bon choix, par contre, par peur, vous partez en direction de l'aéroport de la plage. Vous prenez le premier vol direction Allemagne voisine de la Suisse là où vous habitez.")
                                            Allemagne()
                                            return
                                        else:
                                            print("Désolé, je n'ai pas compris votre réponse. Veuillez répondre par 'oui' ou 'non'.")
                                elif reponse.lower() == "non":
                                    print("Très bon choix, par contre, par peur, vous partez en direction de l'aéroport de la plage. Vous prenez le premier vol direction Allemagne voisine de la Suisse là où vous habitez.")
                                    Allemagne()
                                    return
                                else:
                                    print("Désolé, je n'ai pas compris votre réponse. Veuillez répondre par 'oui' ou 'non'.")
                        elif reponse.lower() == "non":
                            print("Vous n'arrivez pas à vous sauver. Votre vie diminue de 5. Pour la peine, vous ne pouvez pas rester en Australie, vous devez partir en Allemagne.")
                            vie -= 5
                            if vie <= 0:
                                print("Vous avez perdu! Votre vie est à 0.")
                                return
                            Allemagne()
                            return
                        else:
                            print("Désolé, je n'ai pas compris votre réponse. Veuillez répondre par 'oui' ou 'non'.")
                elif reponse.lower() == "non":
                    print("Vous longez la rivière et vous trouvez une pomme.")
                    while True:
                        reponse = input("Voulez-vous manger la pomme? (oui/non) ")
                        if reponse.lower() == "oui":
                            print("Votre vie augmente de 3 et la pomme vous téléporte jusqu'en Allemagne")
                            global vie
                            vie += 3
                            if vie <= 0:
                                print("Vous avez perdu! Votre vie est à 0.")
                                return
                            Allemagne()
                            return
                        elif reponse.lower() == "non":
                            print("Votre vie diminue de 1. Vous tombez dans les pommes de faim et vous vous réveillez en Allemagne.")
                            global vie
                            vie -= 1
                            if vie <= 0:
                                print("Vous avez perdu! Votre vie est à 0.")
                                return
                            Allemagne()
                            return
                        else:
                            print("Désolé, je n'ai pas compris votre réponse. Veuillez répondre par 'oui' ou 'non'.")
                else:
                    print("Désolé, je n'ai pas compris votre réponse. Veuillez répondre par 'oui' ou 'non'.")
        else:
            print("Désolé, je n'ai pas compris votre réponse. Veuillez répondre par 'Allemagne' ou 'Australie'.")

def Allemagne():
    reponse = input("Vous vous retrouvez dans un champ de bataille. Vous voyez un avion libre qui semble être abandonné. Voulez-vous le voler ? (oui/non) ")
    if reponse.lower() == "oui":
        print("Vous réussissez à vous échapper et retourner chez vous, en Suisse, en 2024. Fin du programme.")
    elif reponse.lower() == "non":
        print("Vous vous faites tirer dessus et vous mourrez. Fin du programme.")
    else:
        print("Désolé, je n'ai pas compris votre réponse. Veuillez répondre par 'oui' ou 'non'.")

Australie()