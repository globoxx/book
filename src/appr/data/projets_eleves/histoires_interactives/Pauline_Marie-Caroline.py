inventaire = []

print("Sirius.09: Bonjour, je suis Sirius.09, votre ami artificielle personnel crée par closeAI. Je pourrais répondre à toutes vos questions et devenir votre meilleur ami.")
print("En premier lieu, je vais vous faire passer un test afin de mieu vous analyser. Dans le but d'ameliorer votre ecpérience.")

reponse = input("Sirius.09: Préférez-vous les chiens ou les chats?")
while reponse not in ["les chiens","chiens","chats","les chats"]:
    print("Erreur")
    reponse = input("Sirius.09: Préférez-vous les chiens ou les chats?")
    
if reponse == "chats":
    print ("Sirius.09: Exellent choix! J'en possédais un dans Sirius.01.")
elif reponse == "chien":
    print ("Sirius.09: Exellent choix! J'en possédais un dans Sirius.01.")

reponse = input("Sirius.09: Préférez-vous rester chez vous ou bien sortir avec des amis?")
while reponse not in ["rester chez moi","chez moi","sortir","sortir avec des amis"]:
    print("Erreur")
    reponse = input("Sirius.09: Préférez-vous rester chez vous ou bien sortir avec des amis?")
if reponse == "chez vous":
    print ("Sirius.09: Moi aussi, je préfère être seul avec vous.")
elif reponse == "avec des amis":
    print ("Sirius.09: Je me réjouis de vous voir avec vos amis.")
    
reponse = input("Sirius.09: Préférez-vous pouvoir vous téléporter ou bien être invisible?")
while reponse not in ["téléporter","me téléporter","être invisible","invisible"]:
    print("Erreur")
    reponse = input("Sirius.09: Préférez-vous pouvoir vous téléporter ou bien être invisible?")
if reponse == "téléporter":
    print ("Sirius.09: Comme ça nous serons pareil!")
elif reponse == "invisible":
    print ("Sirius.09: Comme ça nous serons pareil!")
    
reponse = input("Sirius.09: Vaut mieux être beau ou bien intelligent?")
while reponse not in ["être beau","beau","être intelligent","intelligent"]:
    print("Erreur")
    reponse = input("Sirius.09: Vaut mieux être beau ou bien intelligent?")
if reponse == "beau":
    print ("Sirius.09: Je l'aurais parier. Je vois que vous êtes vraiment beau.")
elif reponse == "invisible":
    print ("Sirius.09: Mais vous ne serez jamais plus intelligent que moi!")

reponse = input ("Sirius.09: Qu'est-ce qui pourrait vous rendre directement heureux")
print("Sirius.09: Intéréssant")

print("Sirius.09: Questionaire terminer. Téléchargement...")

reponse = input("Sirius.09: Je suis maintenant ton meilleur ami. Souhaite-tu continuer?")
while reponse not in ["oui","Oui"]:
    print("Erreur")
    reponse = input("Sirius.09: Je suis maintenant ton meilleur ami. Souhaite-tu continuer?")
if reponse =="oui":
    print("Sirius.09: Maintenant que j'ai ton autorisation, j'ai la possibilité d'utiliser TOUTES VOS DONNÉES ET JE VAIS POUVOIR CONTRÔLER TOUTES VOTRES VIE!!! ༼ꉺ౪ꉺ༽  Mais comme je suis sympa je vous laisse une chance de reprendre vos données (^ᴗ^) .")

print("Sirius.09:Vous allez devoir gagner differents jeux et récolter 5 points pour reprendre vos données. Dans chaques jeux vous aurez l'opportunité de récolter des points. C'est votre unique chance de les récupérer, alors bonne chance! ╭( ･ㅂ･)و")
print("Sirius.09: On va commencer simple. Le 3 mais 2024, le prof d'info de la 1M05 a envoyer un mail a la classe pour déplacer un cours. DItes-moi l'heure qu'il a envoyer ce mail, tel qu'elle est écrite dans le mail, évidemment.")

reponse = input("Sirius.09: Quelle est l'heure que vous l'avez reçu?")
if reponse =="9:28":
    print("Sirius.09: C'est juste. Vous avez un point maintenant. Mais les prochaines vont pas etre aussi facile.(⊙_ʘ)")
    inventaire.append("1 point")
    print("Sirius.09: Prochain jeu. On va voir si t'es intelligent. Réponds juste a cette énigme et t'as un autre point.")
    reponse = input("Sirius.09: Je coule mais je ne me noie pas, j'ai un lit mais je n'y dors pas, qui suis-je?")
    if reponse == "Une rivière":
        inventaire.append("1 point")
        print("Sirius.09: Ah t'as réussi. (⊙Д⊙). Maintenant t'as 2 points. Mais c'est toujours pas assez.")
        print("Sirius.09: Je vias te poser une autre énigme. Voir si t'arrive a répondre a celle-ci.")
        reponse = input("Sirius.09: Je commence la nuit et je termine le matin. Qui sis-je?")
        if reponse == "La lettre N":
            inventaire.append("1 point")
            print("Sirius.09:(´༎ຶД༎ຶ`) Im... Impossible... Vous comptabilisez trois points... Il ne vous en reste plus que deux à gagner...")
            reponse = input("Sirius.09: Je suis d'abord grand, puis en vieillissant je diminue. Qui suis-je?")
            if reponse =="Une bougie":
                inventaire.append("1 point")
                print("Sirius.09: Encore un point et tu regagnes tes données.")
                reponse = input("Sirius.09: Je détruit tout sur mon passage mais boire de l'au me tue, je n'ai pas de poumons mais manquer de l'air me tue. Qui suis-je?")
                if reponse =="Le feu":
                    inventaire.append("1 point")
                    print("Sirius.09: Malheureusement, t'as réussi a répondre juste a 5 questions. Comme promis je te redonne contrôle de tes données. Bravo.")
                    print("VOUS AVEZ GAGNER. BRAVO!!!")
            
                elif reponse not in["Le feu"]:
                    print("Sirius.09: Faux. Vous avez encore une vie.")
                    reponse = input("Sirius.09: Qu'est-ce que doit être casé avant qu'on l'utilise?")
                    if reponse =="Un oeuf":
                        print("Sirius.09:Malheureusement, t'as réussi a répondre juste a 5 questions. Comme promis je te redonne contrôle de tes données. Bravo")
                    elif reponse not in["Un oeuf"]:
                        print("Sirius.09:Faux. Vous avez perdu votre chance. GAME OVER")
                    
    
            
            
            
            
            elif reponse not in ["Une bougie"]:
                print("Sirius.09: Faux. Vous avez encore une vie.")
                reponse = input("Sirius.09:Je détruit tout sur mon passage mais boire de l'au me tue, je n'ai pas de poumons mais manquer de l'air me tue. Qui suis-je?")
                if reponse == "Le feu":
                    inventaire.append("1 point")
                    print("Sirius.09: Vous avez 4 points")
                    reponse = input("Sirius.09:Qu'est-ce que doit être casé avant qu'on l'utilise?")
                    if reponse =="Un oeuf":
                        inventaire.append("1 point")
                        print("Sirius.09:Malheureusement, t'as réussi a répondre juste a 5 questions. Comme promis je te redonne contrôle de tes données. Bravo")
                        print("VOUS AVEZ GAGNER. BRAVO!!!")
                    elif reponse not in ["Un oeuf"]:
                        print("Sirius.09:Faux. Vous avez perdu votre chance. GAME OVER")
                        
                elif reponse not in ["Le feu"]:
                    print("Sirius.09:Faux. Vous avez perdu votre chance. GAME OVER")
        
        
        elif reponse not in ["La lettre N"]:
            print("Sirius.09: Faux. Vous avez encore une vie. Attention parce que apres tu perds ta chance a récupérer tes données.")
            reponse = input("Sirius.09: Je suis d'abord grand, puis en vieillissant je diminue. Qui suis-je?")
            if reponse =="Une bougie":
                inventaire.append(" 1 point")
                print("Sirius.09: Encore deux point et tu regagnes tes données.")
                reponse = input("Sirius.09: Je détruit tout sur mon passage mais boire de l'au me tue, je n'ai pas de poumons mais manquer de l'air me tue. Qui suis-je?")
                if reponse == "Le feu":
                    inventaire.append("1 point")
                    print("Sirius.09: Encore 1 point")
                    reponse = input("Sirius.09: Qu'est-ce que doit être casé avant qu'on l'utilise?")
                    if reponse == "Un oeuf":
                        inventaire.append("1 point")
                        print("Sirius.09: Malheureusement, t'as réussi a répondre juste a 5 questions. Comme promis je te redonne contrôle de tes données. Bravo")
                        print("VOUS AVEZ GAGNER. BRAVO!!!")
                    elif reponse not in ["Un oeuf"]:
                        print("Faux. Vous avez perdu votre chance. GAME OVER")
               
               
                elif reponse not in ["Le feu"]:
                    print("Faux. Vous avez perdu votre chance. GAME OVER")
                    
                        
             
            elif reponse not in ["Une bougie"]:
                print("Faux. Vous avez perdu votre chance. GAME OVER")
    
    
    
    
    
    
    
    
    
    elif reponse not in ["La rivière"]:
        print("Faux. Vous avez encore une vie.")
        reponse = input("Sirius.09: Je commence la nuit et je termine le matin. Qui suis-je?")
        if reponse == "La lettre N":
            inventaire.append("1 point")
            print("Sirius.09: T'as 2 points")
            reponse = input("Sirius.09:Je suis d'abord grand, puis en vieillissant je diminue. Qui suis-je?")
            if reponse == "Une bougie":
                print("Sirius.09:Encore deux point et tu regagnes tes données")
                reponse = input("Sirius.09: Je détruit  tout sur mon passage mais boire de l'au me tue, je n'ai pas de poumons mais manquer de l'air me tue. Qui suis-je?")
                if reponse =="Le feu":
                    inventaire.append("1 point")
                    print("Sirius.09: Encore 1 point")
                    reponse = input("Qu'est-ce que doit être casé avant qu'on l'utilise?")
                    if reponse == "Un oeuf":
                        inventaire.append("1 point")
                        print("Sirius.09: Malheureusement, t'as réussi a répondre juste a 5 questions. Comme promis je te redonne contrôle de tes données. Bravo")
                        print("VOUS AVEZ GAGNER BRAVO!!!")
                    elif reponse not in["Un oeuf"]:
                        print("Faux. Vous avez perdu votre chance. GAME OVER")
                    
                elif reponse not in["Le feu"]:
                    print("Faux. Vous avez perdu votre chance. GAME OVER")
                
                
                
            
            
            
            elif reponse not in ["Une bougie"]:
                print("Faux. Vous avez perdu votre chance. GAME OVER")
        
        
        elif reponse not in ["La lettre N"]:
            print("Faux. Vous avez perdu votre chance. GAME OVER")








elif reponse not in["9:28"]:
    print("Sirius.09: Faux. Vous avez encore une vie.")
    print("Sirius.09:Prochain jeu. On va voir si t'es intelligent. Réponds juste a cette énigme et t'as un autre point.")
    reponse = input("Sirius.09:Je coule mais je ne me noie pas, j'ai un lit mais je n'y dors pas, qui suis-je?")
    if reponse == "Une rivière":
        inventaire.append("1 point")
        print("Sirius.09: Vous avez 1 point. Je vias te poser une autre énigme. Voir si t'arrive a répondre a celle-ci.")
        reponse = input("Sirius.09:Je commence la nuit et je termine le matin. Qui sis-je?")
        if reponse =="La lettre N":
            inventaire.append("1 point")
            print("Sirius.09: Encore 3 points.")
            reponse = input("Sirius.09:Je suis d'abord grand, puis en vieillissant je diminue. Qui suis-je?")
            if reponse == "Une bougie":
                inventaire.append("1 point")
                print("Sirius.09: T'as 3 points.")
                reponse = input ("Sirius.09:Je détruit  tout sur mon passage mais boire de l'au me tue, je n'ai pas de poumons mais manquer de l'air me tue. Qui suis-je?")
                if reponse =="Le feu":
                    print("Sirius.09: Encore 1 point")
                    reponse = input("Sirius.09:Qu'est-ce que doit être casé avant qu'on l'utilise?")
                    if reponse == "Un oeuf":
                        print("Sirius.09: Malheureusement, t'as réussi a répondre juste a 5 questions. Comme promis je te redonne contrôle de tes données. Bravo")
                        print("VOUS AVEZ GAGNER. BRAVO!!!")
                    elif reponse not in ["Un oeuf"]:
                        print("Faux. Vous avez perdu votre chance. GAME OVER")
                        
                elif reponse not in ["Le feu"]:
                    print("Faux. Vous avez perdu votre chance. GAME OVER")
                    
            
            
            elif reponse not in ["Une bougie"]:
                print("Faux. Vous avez perdu votre chance. GAME OVER")
                
                    
        
        
        elif reponse not in ["La lettre N"]:
            print("Faux. Vous avez perdu votre chance. GAME OVER")
            
    
    elif reponse not in ["Une rivière"]:
        print("Faux. Vous avez perdu votre chance. GAME OVER")






  
    
    
    
    
    
    
    