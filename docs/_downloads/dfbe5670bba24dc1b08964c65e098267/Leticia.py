

def debut ():
	print ("Vous avez trois mondes")
	reponse = input ("Qu'elle monde choissez-vous ? (Verdentis, Sombra, Aurorea)")
	while reponse not in ["Verdentis, Sombra, Aurorea"]:
		reponse = input ("Qu'elle monde choissez-vous ?")
	if reponse == "Verdentis" :
		Verdentis()
	elif reponse == "Sombra":
		Sombra()
	elif reponse == "Aurorea": 
		Aurorea()
		
def Verdentis ():
	print ("Vous accedez à un jardin secret, mais pour ouvrir la porte, vous devez avoir l'artefact qui a été...  ")
	reponse = input (" Voulez-vous nous aider à retrouver l'artefact ? (oui ou non)")
	while reponse not in ["oui", "non"]:
		reponse = input (" Voulez-vous nous aider à retrouver l'artefact ? ")
	if reponse =="oui" :
		print ("Il a été voler par notre ennemi le phénix.")
		print ("Il doit être dans sa grotte.")
		reponse = input ("voulez-vous aller voir chez lui ? (la grotte ou non)")
		while reponse not in ["la grotte", "non"]:
			reponse = input ("voulez-vous aller voir chez lui ?")
		if reponse == "la grotte":
			print ("il n'est pas chez lui")
			print ("Vous entrez et voyez l'artefact sur une armoir.")
			print ("Vous le prenez et vous avancez vers la proche, mais au même moment arrive le phénix.")
			reponse = input ("Ou vous vous cachez pour qu'il ne vous vois pas? (dans l'armoir ou sous le lit)")
			while reponse not in ["dans l'armoir", "sous le lit"]:
				reponse = input ("Ou vous vous cachez pour qu'il ne vous vois pas?")
			if reponse = "dans l'armoir":
				print (" il va se coucher et quand vous sortez de l'armoire il vous entend")
				print(" Game over")
			elif reponse == "sous le lit":
				print (" il se couche donc vous pouvez partir et retourner au jardin secret")
				print ("Victoire")
				
		elif reponse == "non":
		 print ("vous allez à la rencontre du dragon qui va vous tenir compagnie")
		 print (" ne lui faites pas trop confiance")
		 print (" Game over")
		
	elif reponse == "non":
		print (" vous êtes pas gentils")
		print (" vous allez à la rencontre du dragon qui va vous tenir compagnie")
		print (" Game Over")
		

def Sombra ():
	print (" attention, il y a des menaces dans chaque coin")
	print (" pour réussir à vous sauver vous devrez faire des choix")
	reponse = input (" que voulez-vous comme aide ? (alliés ou armes)")
	while reponse not in ["alliés", "armes"]:
		reponse = input (" que voulez-vous comme aide ?")
	if reponse == "alliés":
		print (" vous avez l'aide d'un ami")
		print ("il vous ammene jusqu'à un volcan")
		print (" il vous laisse là-bas et s'enfuit")
		reponse = input ("Voulez-vous aller derrière lui ? ( oui ou non )")
		while reponse not in ["oui","non"]:
			reponse = input ("Voulez-vous aller derrière lui ? ")
		if reponse == "non":
			print ("Vous mourrez au bas  du volcan à cause de la lave")
			print ("Game Over")
		elif reponse == "oui":
			print ("Il vous emmène dans une forêt lugubre remplie de serpents vénimeux ")
			print ("Pour traverser la forêt vous devez éviter le sable mouvant et les trous pleins de serpents ")
			reponse = input ("Vous êtes prêts ? (oui ou non)")
			while reponse not in ["oui","non"]:
				reponse = input ("Vous êtes prêts ?")
			if reponse == "non":
				print ("Game Over")
			elif reponse == "oui":
				print ("Balancez-vous d'arbre en arbre et de liane en liane ")
				print ("a la fin de se périple, le grand sage de la forêt vous posera une question.")
				print ("la question est...")
				reponse = input ("Vous êtes prêts ? (éléphant ou chimpanzé)")
				while reponse not in ["éléphant","chimpanzé"]:
					reponse = input ("Vous êtes prêts ?")
				if reponse == ("éléphant")
				print ("Game Over")
				elif reponse == ("chimpanzé")
				print ("Victoire")

	elif reponse == "armes":
		inventaire =[]
		reponse = input ("quelles armes voulez vous ? (gants de boxe ou fleche ou pistolet)")
		while reponse not in ["gants de boxe", "fleche", "pistolet"]:
			reponse = input ("quelles armes voulez vous ?")
		
		inventaire.append ("gants de boxe")
		print ("vous devez combattre Lysander, la créature des enfers.")
		print ("Vos gants de boxe ont un bouton magique qui vous fait avoir des petits bonus pour pouvoir le battre.")
		print ("Vous activez le bouton magique qui vous donnes la possibilité d'avoir la force en x3.")
		print ("Je suis fier de vous grâce a votre buste de force vous avez atteint la victoire.")
		print ("VOUS  L'AVEZ EXTERMINE ! ! !")
		print ("Victoire")



		inventaire.append ("fleche")
		print ("Vous devez tirer une flèche dans la cavité d'un arbre ")
		reponse =input ("que se passe-t-il ? ("Droite ou gauche")
		while reponse not in ["droite", "gauche"]:
			reponse =input ("que se passe-t-il ?")
		if reponse == "droite":
		print ("si la fleche part à droite vous tomber dans un trou noir")
		print ("Game Over")
		elif reponse == "gauche":
		print ("si la flèche part à gauche vous passez au niveau suivant")
		print ("vous vous teleportez vers une autre dimension ")
		print ("ou vous aller rencontrer une fée enchantée qui va vous amener a la victoire ")
		print ("Victoire")
		
		inventaire.append("pistolet")
		print ("Game Over")

	
	
def Aurorea ():
	print ("c'est un monde illuminer et joyeux. Vous rencontrez la déesse, Nyx.")
	print ("elle vous donne une mission, c'est de sauver son royaume.")
	reponse =input ("voulez-vous l'aider? (oui ou non)")
	while reponse not in ["oui", "non"]:
		reponse =input ("voulez-vous l'aider?")
	if reponse == "non":
		debut ()
	elif reponse == "oui":
		reponse =input ("voulez-vous l'aider?")
		print (" vous accéder au jardin Étoile")
		print ("L'arbre de vie du royaume est en train de mourir car il a été contaminé.")
		print ("Il contamine tous les arbres autour faut aller le purifier.")
		print ("Pour pouvoir purifier l'arbre il faut aller chercher une larme de crocodile")
		print ("Faut aller la chercher dans la vallée des eaux.")
		print ("La vallée des eaux était un lieu sombre et sinistre, ou les murmure des esprits aquatique raisonner dans l'air.")
		print ("Alors qu'il  pénétrer plus profondément dans les profondeurs de la vallée. ")
		print (" Les arbres étaient déformés et tordu, témoin silencieux de la contamination qui se répondait. ")
		print ("La larme de crocodile était la seule chance de purifier l'arbre de vie et de sauver le royaume.")
		print ("Des énigmes complexes ils attendaient pour qu'il puisse vaincre les créatures des eaux sombres.")
		reponse =input ("Voulez-vous répondre à l'énigme ?(oui ou non)")
		while reponse not in ["oui", "non"]:
			reponse =input ("Voulez-vous répondre à l'énigme ?")
		if reponse == "non":
		print ("Game Over")
		elif reponse == "oui":
			inventaire =[]
		reponse = input ("J’ai des dents, mais je ne mords pas. D’ailleurs je n’ai pas de bouche. Je n’ai pas de tête, pourtant j’ai souvent des cheveux. Qui suis-je ? ( une brosse à dent ou un peigne ou un dentier) ")

		while reponse not in ["une brosse à dent", "un peigne", "un dentier"]:
			reponse = input ("J’ai des dents, mais je ne mords pas. D’ailleurs je n’ai pas de bouche. Je n’ai pas de tête, pourtant j’ai souvent des cheveux. Qui suis-je ?")
		inventaire.append ("une brosse à dent")
		print ("Game Over")
		inventaire.append ("un dentier")
		print ("Game Over")
		inventaire.append ("un peigne")
		print ("Bravo ! Vous avez la possibilité d'utiliser un bocal pour récolter la larme de crocodile")
		print (" maintenant il reste plus qu'à trouver le bon crocodile pour pouvoir le faire pleurer et avoir une larme.")
		print ("Pour reconnaitre le bon crocodile, il y a plusieurs indices, il porte une casquette Lacoste, un couteau en bois et une veste rouge écrit j'accoste au lieu de Lacoste")
		print ("Regardez il est devant vous !!! ")
		print ("Vous devez essayer  de le faire pleurer, pour pouvoir récolter une larme, il adore les histoires dramatiques et de meurtres.")
		print ("Pour reconnaitre le bon crocodile, il y a plusieurs indices, il porte une casquette Lacoste, un couteau en bois et une veste rouge écrit j'accoste au lieu de Lacoste")
		print ("Regardez il est devant vous !!!")
		print ("Vous devez essayer  de le faire pleurer, pour pouvoir récolter une larme, il adore les histoires dramatiques et de meurtres.")
			inventaire =[]
		reponse = input ("Quel histoire choisissez-vous ? ( le lièvre et la tortue ou Iron man ou Romeo et Juliette)")
		while reponse not in ["le lièvre et la tortue", "Iron man", "Romeo et Juliette"]:
			reponse = input ("Quel histoire choisissez-vous ?")
		inventaire.append ("le lièvre et la tortue")
		print ("Game Over")
		inventaire.append ("Iron man")
		print ("Game Over")
		inventaire.append ("Romeo et Juliette")
		print ("Victoire")


debut ():
Verdentis ():
Sombra ():
Aurorea ():







