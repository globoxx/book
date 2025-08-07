print ("Vous êtes un aventurier solitaire, qui se réveille au cœur d’une forêt dense et mystérieuse. L’air est frais, et une brume épaisse recouvre le sol. À vos pieds, vous trouvez un sac à dos avec quelques provisions et une carte partiellement déchirée. Vous êtes perdu, et le seul moyen de sortir semble être d’explorer cette forêt étrange. Au loin, vous entendez le bruit d’une rivière. Vous voyez aussi deux chemins : l’un à gauche, qui semble mener vers une montagne, et l’autre à droite, plus obscur, plongeant dans des arbres épais.")

inventaire= []
vie = 100

choix = input("Vous devez maintenant choisir quel chemin prendre. Que faites-vous ?]")
if choix == "prendre le chemin de gauche vers la montagne ":
    print("vous commencez à gravir la montagne, mais le chemin est difficile. Apres quelques heures de marche, vous arrivez à un précipite. En bas, vous apercevez un vieux pont suspendu qui semble peu fiable.")
    choix = input("Vous avez deux choix qui s'offre a vous ?]")
    if choix == "traverser le pont malgré son état":
        print("le pont craque sous vos pieds à chaque pas, mais vous réussissez à le traverser. De l'autre cote, vous trouvez une grotte sombre. En entrant, vous découvrez une étrange lumière venant d'un cristal géant. Mais attention, un dragon semble dormir près du cristal. Vous avez deux options.")
        choix = input("vous devez choisir entre voler le cristal ou faire demi-tour?]")
    if choix == "voler le cristal":
        print("vous avez réussi à ne pas réveiller le dragon et grâce à cela votre vie augmente de 20")
        vie = vie + 20
        if vie > 50:
            print("Vous avez accomplis votre mission")
elif choix == "revenir en arrière et explorer un autre chemin":
    print("vous réussissez à attraper le cristal sans faire de bruit. Le dragon ne bouge meme pas. Vous repartez prudemment et quittez la montagne avec un précieux cristal en main.")
elif choix == "suivre le chemin à droite vers la foret dense":
    print("vous marchz et trouver un sac a dos abandonner vous l'ouvrez et trouvé une arme et des ressources")
    choix = input("vous prenez le sac a dos et la gourde ? ")
    if choix == "oui":
        print("Vous prenez le sac et la gourde")
        inventaire.append("sac et gourde")
    print("vous vous enfoncez dans la foret. Soudain, vous entendez des bruits étranges derrière vous. Un loup apparait, affamé. Vous avez une chance de vous défendre si vous avez une arme ou des ressources pour l'éloigner.")
    if vie > 120:
        print ("Vous avez gagnö!")
    elif "sac et gourde" in inventaire :
        print("vous avez ramassé l'arme et les ressources, vous avez reussi a léloigner et poursuivez votre chemin. Au bout d'un moment vous voyez la fin de la foret et sortez vivant")
        print("Vous avez accomplis votre mission")



