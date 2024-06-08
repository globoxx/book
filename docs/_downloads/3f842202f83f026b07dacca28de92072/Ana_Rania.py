sac = []
poches = []
argent = []
vie = 100
humeur = 100
peur = 0
fatigue = 15
dexterite = 0
relation_Kraglin = 0
relation_Yondu = 0

def intro():
    print("...Oh ?")
    print("Salut !")
    print("Désolé, je suis encore en formation de narratrice...")
    print("J'ai pas vraiment de nom...")
    reponse = input("et toi, est-ce que tu as un prénom ?")
    while reponse not in ["non", "oui"]:
        print("...")
        reponse = input("je t'ai demandé si tu as un prénom, t'en as un ?")
    if reponse == "oui":
        print("Oh trop cool !")
        name = input("Et c'est quoiii ?")
        print("Eh bah bonjour alors (name)!")
    elif reponse == "non":
        print("arrete de te moquer de moi !!")
        print("Eh bah si t'en as pas, t'as qu'a t'en créer un.")
        name = input("Du coup ?")
        print("Bonjour du coup (name)")
    print("J'ai remarqué que t'étais pas du genre bavard... je vais t'aider du coup ! J'aime bien blablatter moi.")
    print("au fait... tu sais pas pourquoi je suis là...")
    print("J'ai fuit les Ravageurs.")
    reponse = input("Tu sais qui sont les Ravageurs ?")
    while reponse not in ["non", "oui"]:
        print("...")
        reponse = input("Je t'ai demandé si tu sais qui sont les ravageurs ? oui ou non ?")
    if reponse == "oui":
        print("Alors j'ai pas besoin de te dire qu'ils sont juste derrière toi, si ?")
        print("Petit malin va...")
    elif reponse == "non":
        print("MHm..")
        print("Je sais pas ce que je peux te dire sur eux.")
        print("ce que tu dois retenir, c'est qu'ils sont dange-")
        print("ATTENTION !!")
        peur += 5
    print('tu n"as pas le temps de parler')
    print('tu vois un vaisseau spatiale imposant se poser sur le terrain vaste à tes cœtés')
    print('une créature bleue, si c"est ça le terme adéquat s"approcher dangereusement vite')
    print("Lui, c'est Yondu Udonta, le capitaine des Ravageurs.")
    print("T'as un pistolet ?")
    if "pistolet" not in sac:
        print("Arg... T'en as pas...")
        print("Oh mince...")
    print("Yondu s'approche vite de toi !! Fais attention !!")
    peur += 10
    reponse = input("Est-ce que tu tentes de fuir ?")
    while reponse not in ["non", "oui"]:
        print("'viteee t'as pas le temps là !! arrête d'hésiter !!'")
        reponse = input("'tu tentes de fuir ? oui ou non ??!!'")
    if reponse == "oui":
        print("Cours le plus vite que tu peux !!")
        print("Malheureusement, alors que tu courrais...")
        print("T'es tombé.e et tu t'es ouvert le genou.")
        print("Tu vois un menu étrange apparaitre devant toi disant 'vie -20'")
        vie -= 20
        humeur -= 20
        peur += 10
    elif reponse == "non":
        print("Mince...")
        print("tu dois être terrifié.e...")
        print("Je serai là pour te guider, promis.")
        print("OH ! attends !!")
        print("Tu baisses la tête avec espoir et tu remarques simplement des écouteurs au sol")
        print("Aller, rammasse les.. qui sait, ça peut t'aider à passer le temps.")
        reponse = input("Suivre le conseil de la voix amie et ramasser les écouteurs ?")
        while reponse not in ["non", "oui"]:
            print("Yondu se rapproche de toi")
            reponse = input("'Est-ce que tu veux ramasser les écouteurs ?? oui ou non ? je te conseille de le faire'")
        if reponse == "oui":
            print("Tandis que Yondu s'approchait, tu eus juste le temps de ranger tes écouteurs.")
            print("Ils sont dans ton sac")
            sac.append("écouteurs")
            print("Au moins t'aura de quoi occuper ton esprit..")
            print("Cette pensée te fit sourire.")
            humeur += 10
        elif reponse == "non":
            print("Tu as ignoré ce que la voix t'as conseillé.")
            print("C'est bien domage")
            print("Ta peur augmente")
            peur += 10
            print("Tu vas bien t'ennuyer.")
    print("Quand tu releva la tête, tu vis une flèche à la trainée rouge t'arriver dessus.")
    print("Elle ne te toucha pas.")
    print("Le fait de la voir si proche de toi avait suffit à te faire tomber évanoui")
    vie -= 5

def vaisseau():
#Vaisseau des Ravageurs
    print("Tu ne te souviens de plus rien")
    print("ta tête fait mal et tu entends un bourdonnement")
    print("Puis une petit voix que tu connais bien.")
    print("'EH eh eh ??? {char} ? tu m'entends ?'")
    reponse = input("Est ce que tu lui fais une farce un peu cruelle et l'ignorer ?")
    while reponse not in ["non", "oui"]:
        print("...")
        reponse = input("Est-ce que tu ignores ta voix amie ? oui ou non ?")
    if reponse == "oui":
        print("Tu ignores ta voix amie.")
        print("'EH !! M'ignore pas comme ça !!'")
        print("Tu finis par rire aux éclats en entendant la 'narratrice' comme elle se surnommait vexée")
        print("'Me refait plus jamais ça, je me suis inquiétée !!'")
        humeur += 10
        peur -= 5
    elif reponse == "non":
        print("Tu lèves le pouce pour signaler que tu l'entendais bien.")
        print("'ouf... Si jamais, Yondu t'as soigné...")
        print("Tu fronces les sourcils confus")
        reponse = input("Questionner la voix amie sur ce que Yondu a fait pendant ton inconscience ?")
        while reponse not in ["non", "oui"]:
            print("...")
            reponse = input("Tu veux savoir ce que Yondu a fait pendant ton inconscience ? oui ou non ?")
        if reponse == "oui":
            print("La voix amie soupira profondement")
            print("'Je te résume ce que j'ai vu alors...'")
            print("'Tu t'es évanoui et Yondu t'as porté jusqu'au vaisseau.'")
            print("'Il t'as posé ici, dans une des cellules et a posé de quoi manger.'")
        elif reponse == "non":
            print("Tu décides de ne rien dire et de juste attendre que la voix reprenne")
            print("Ton humeur se dégrade.")
            humeur -= 10
        elif reponse != "non" and "oui":
            print("Eh l'ami ? tu m'entends ?")   
            print("'Y a de quoi mangé sur la table, Yondu t'as apporté des provisions...'")

def episode_2():
    print("Une fois le ventre remplis tu vois Yondu devant toi")
    print("Il te demande comment est-ce que tu te sens")
    if peur >= 20:
        print("Yondu te rassure et te dis de te calmer.Il dit vouloir juste discuter.")
        relation_Yondu += 10
        reponse = input("Lui demander pourquoi t'es la ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Il explique vouloir un nouvel atout pour son équipe des Ravageurs")
            relation_Yondu += 5
        elif reponse == "non":
            print("...")
        print("Il te conseilles de te reposer un peu et qu'il reviendrai te voir plus tard")
        if "ecouteur" in sac:
            print("Tu mets les écouteurs sur ta tête et ta petite voix amie chantonne avec toi")
        else:
            print("Yondu à de la peine pour toi et te  lance un casse tête en bois à tes pieds")
        print("Après un moment, quand t'es calmé, Yondu revient.")        
        relation_Yondu += 5
    else:
        print("Il dit que c'est bien de garder ton sang froid")
        relation_Yondu -= 10
    reponse = input("Il demande si tu as bien mangé ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("Tu le remercies pour la nourriture et il hoche la tête amicalement")
    elif reponse == "non":             
        print("Il voit que tu n'as pas encore tout mangé et te conseille d'en garder un peu te prévenant que ça te fera du bien après.")
              
def n_ourriture():
    reponse = input("Est-ce que tu vas manger ?")
    while faim == "oui":
        while reponse not in ["non", "oui"]:
            print("...")
            reponse = input("Est-ce que tu as un petit creux ?")
        if reponse == "oui":
            print("Tu t'approches alors de la petite table et vois des barres de cereales, du chocolat, un sandwich et une bouteille d'eau")
            reponse = input("QU'est-ce que tu manges en premier ?")
            while reponse not in ["chocolat", "sandwich", "bouteille d'eau", "barre de cereale"]:
                print("Oh tu sais peut-être pas ce qu'il y a.")
                print("il y a du chocolat, sandwich, bouteille d'eau et barre de céréales")
                reponse = input("QU'est-ce que tu manges en premier ?")
            if reponse == "barre de cereales":
                manger = input("manger ou garder pour plus tard ?")
                while manger not in ["manger", "garder pour plus tard"]:
                    print("tu dois soit 'manger' un peu ou si tu veux pas, 'garder pour plus tard'")
                    manger = input("manger ou garder pour plus tard ?")
                if manger == "manger":
                    print("Tu commences à manger la barre de cereales, c'est pas beaucoup, mais ça fait du bien.")
                    vie += 7
                elif manger == "garder pour plus tard":
                    print("t'en mets un peu dans ta poche pour plus tard, qui sait si t'as faim")
                    print("'t'avais mieux que des céréales en batre à manger quand même !'")
                    print("dit la voix amie, ce qui te fait marrer")
                    humeur += 7
                    poches.append("barre céréales")
            elif reponse == "chocolat":
                print("La douceur du chocolat fondant dans ta bouche te rend heureux")
                print("Tu décides d'en garder un peu dans ta poche")
                poches.append("chocolat")
                vie += 10
            elif reponse == "sandwich":
                manger = input("manger ou garder pour plus tard ?")
                while manger not in ["manger", "garder pour plus tard"]:
                    print("tu dois soit 'manger' un peu ou si tu veux pas, 'garder pour plus tard'")
                    manger = input("manger ou garder pour plus tard ?")
                if manger == "manger":   
                    print("C'était un bon sandwich thn mayo")
                    print("Tu te demandes comment ils ont accès à du Thon")
                    print("Cette pensée te fait rire")
                    humeur += 5
                elif manger == "garder pour plus tard":
                    print("tu le remballes et tu le range dans tes poches pour plus tard")
                    poches.append("sandwich")
            elif reponse == "bouteille d'eau":
                print("Tu prefères pas risquer de manger la nourriture.")
                print("Tu bois une gorgée d'eau")
                print("C'est rafraichissant")
                vie += 5
                print("'garde le reste dans ton sac, ça te fera du bien de pas être déshydratée'")
                sac.append("bouteille d'eau")
            faim = input ("'Est-ce que t'as encore faim ?'")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui":
                n_ourriture()
            elif reponse == "non":
                episode_2()

def rencontre():
    print("Alors que tu dégustais ce qui était posé sur la table, tu remarquas une silouhette")
    print("Tu reconnu la personne bleue")
    print("C'était Yondu.")
    print("Tu reculais de peur, mais ta voix amie, qui t'avais pourtat laisser manger tranquille, parla enfin")
    print("'Il va rien te faire, il a l'air tout calme '")
    print("La peur en toi augmentait")
    peur += 10
    print ("'Gamin ? Eh, tranquille, tu vas encore te refaire mal.'")
    print("ça va ? pas trop effrayé ?")

def partie_3():
    if peur >= 30:
        print("Yondu s'approcha de toi en soupirant et posa une main sur ton épaule")
        print("'gamin, je veux pas te faire de mal. S'il-te-plaît, reste calme'")
        reponse = input("lui demander pourquoi t'es là ?")
        if reponse == "oui":
            print("J'avais besoin d'un nouvel atout. et un terrien c'est parfait pour moi")
        elif reponse == "non": 
            print ("tu n'oses rien demander de plus sur ce qu'il veut de toi")
            print("il te terrifie")
            peur += 5
    else:
        print("C'est bien, tu sais garder ton sang froid.")
        print("bon gamin, tu ferais mieux de te reposer. je viens demain")
    if "écouteurs" in sac:
        print("tu mets les écouteurs sur ta tête et tu fermes les yeux en écoutant de la musique pré-enregistrée.")
        print("tu te demandes comment, d'ailleurs")
        humeur += 10
    else:
        print("Yondu te regarde regardes avec de la peine et te lance un petit casse tête en bois à tes pieds")
        print("tu le regardes confuse et il te fait un clin d'œil")
        print("'ça va t'occuper l'esprit, aller, essaie quand même de dormir'")
        poches.append("casse-tête bois")
    print("après un moment, Yondu revient avec une question qui semble être importante")
    print("'en fait gamin, t'as bien mangé ?'")
    print("t'entends la petite voix rire aux éclats à la question")
    print("vu que tu réponds pas, trop distrait par la voix que seul toi entend, il redemande")
    reponse = input("Tu m'écoutes ? Est-ce que tu as bien manger ?")
    while reponse not in ["oui", "non"]:
        print("'oui ou non ?'")
        reponse = input("'T'as bien manger ?'")
    if reponse == "oui":
        print("Tu le remercies pour la nourriture et il hoche la tête amicalement")
    elif reponse == "non":
        print("'Je vois que tu n'as pas fini ton plat. Garde le pour plus tard si tu n'as pas faim, ça ne te fera pas de mal'")
        n_ourriture()


def visite():
    reponse = input("'T'es partante pour une visite des lieux ou tu préfères un peu de repos ?'")
    while reponse not in ["visite", "me reposer"]:
        print("Hehe la réponse c'est soit 'me reposer' soit 'visite' patate !")
        reponse = input("'Alors une visite ou du repos ???'")
    if reponse == "visite":  
        print("Il commença par lui montrer la salle d'entrainement qui avait diverses armes.")
        reponse = input("'Voici nos armes. Tu peux essayer le sabre, le revolver, les dagues ou le fusil, sers toi.'")
        while reponse not in ["sabre", "revolver", "dagues", "fusil"]:
            print("Non non non joueur, cette reponse est fausse !!! écrit bien pls")
        reponse = input("Le sabre, le revolver, les dagues et le fusil sont les quatre armes à ta disposition. Essaie en une ")
        if reponse == "sabre":
            print("Tu empoignes le sabre fermement et décapite le mannequin avec aisance")
            print("'Pas mal'")
            print("Tu es heureuse de voir Yondu fier de toi")
            dexterite += 15
            humeur += 10
        elif reponse == "revolver":
            print("Avec maladresse tu attrapes le revolver pour tirer sur la tête du mannequin. Tu rates. ")


def kraglin():
    print("Kraglin s'incruste dans un coin du bureau de Yondu, restant cependant silencieux")
    relation_Kraglin += 10
    print("Yondu t'expliqua qu'il souhaitait que tu les rejoignes et qu'il te voulait sur le terrain pour ta première mission")
    reponse = input("Il te demande si tu as hâte")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("As- tu hâte ?")
    if reponse == "oui":
        print("Il admire ta motivation et commence à t'expliquer la mission")
        relation_Kraglin += 6
    elif reponse == "non":
        print("Il en rigole un peu et t'ébouriffe les cheveux")
    print("Il en rigole un peu et te rassure en disant que c'est qu'un simple vol, piquer un orbe à un certain Peter Quill")
    print("Il te conseille de pas oublier tes armes et te donne quelques rubis te disant qu'avoir de la monnaie sur toi c'est toujours bien")  
    if "couteau deux lames" or "dague" or "sabre" or "blaster" or "revolver" or "fusil" in sac:
        print("Yondu est fier de voir que tu as une arme sur toi")
        humeur += 10
        relation_Yondu += 15
    reponse = input("Tu vas te reposer là où Yondu te conseilles de dormir, ou tu vas admirer la galaxie avec Kraglin ?")
    while reponse not in ["suivre le conseil", "admirer la galaxie"]:
        print("tape soit 'suivre le conseil' ou 'admirer la galaxie'")
        reponse = input("alors?")
    if reponse == "suivre le conseil":
        print("Yondu t'emmènes dans une salle à l'arrière du vaisseau où tu peux aussi admirer l'espace")
        reponse = input("Il te demandes si tu as déjà volé (cambrioler) ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("As tu deja voler")
        if reponse == "oui":
            print("Il est étonné mais en bien et te dis que tu vas alors l'aider dans cette mission là")
        elif reponse == "non":
            print("il dit que c'est pas grave il va tapprendre")
            print("Il dit que vous allez voler un orbe")
    reponse = input("lui demander pourqioi ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("lui demander ?")
        if reponse == "oui":
            relation_Yondu -= 4
            print("Il ricanne à la question et dit que t'es un drole de personnage de pas savoirce qu'est cette pierre")
        elif reponse == "non":
            print(" Il te frappe amicalement le dos et te dis etre fier que tu ne le questionne pas")
    print("Il explique qu'il aura besoin de toi, vu que t'es petit pour aller dans un temple chercher la pierre")
    reponse = input("demander d'aller seul ou accompagnee ?")
    while reponse not in ["seul", "accompagné"]:
        print("hein ? c'est seul ou accompagné")
        reponse = input("alors ?")
    if reponse == "seul":
        print("tu demandes daller seul")
        print("il dit que c'est une sage decison mais kraglin et les autres protegeront tes arrieres")
    elif reponse == "accompagné": 
        print("il semble reticent à la proposition")
        if relation_Yondu > relation_Kraglin:
            print(" Yondu soupir profondèment et te dis qu'en tant que commandant, c'est son devoir de t'accompagner pour ta première mission.")
        elif relation_Kraglin > relation_Yondu:
            print("il dit que tu feras alors equipe avec krags et qu'il t'aideras pour ta premiere mission")
        else:
            print("il dit que c'est mieux que tu y ailles seul et que tout ira bien")
    elif reponse == "admirer la galaxie":
        print("Tout content, il passe un bras autour de tes épaules et vous allez au cockpit") 
        print("Il prend les commandes du vaisseau pour changer le cap et te monter de belles constellations")
        reponse = input("Kraglin te propose de te laisser guider le vaisseau un moment")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("tu veux guider le vaisseau ?")  
        if reponse == "oui":
            print("Avec hésitations tu prends les commandes du vaisseau écoutant les conseils du pilote")
            print("krag est fier de toi")
        elif reponse == "non":
            print("La petite voix répond pour toi toute excitée. Kraglin semble même pas remarquer que c'est pas toi qui as parlé")
            print("Il voit que t'es pas encore très à l'aise pour conduire le vaisseau et t'aide un sourire aux lèvres")
            reponse = input("Est-ce que tu aimes conduire le vaisseau ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
            reponse = input("tu aimes ?")
            if reponse == "oui": 
                print("il est fier de toi")
            elif reponse == "non":
                print("Il trouve ça très dommage et te propose de juste regarder si t'aimes vraiment pas")   
    print("Il te propose de mettre un peu de musique")
    if "radio" in sac:
        print("Vous faites un karaoké qui s'entend dans tout le vaisseau")
    else:
        print("Il te dis que c'est pas grave et commence à chante 'back in black' accapela")        
        
def nar():         
    print("vous finissez par atterir sur une planete")
    print("tu sors du vaisseau apres tes amis, kraglin te conseilles de rester pres de lui")
    print("vous arrivez vers le temple, il y a un monstre qui tattends là bas")

def test_dexterite(): 
    if dexterite<30:
        if "revolver" or "fusil" or "blaster" in sac:
            print("Tu prends ton arme et tu tires sur la bestiole qui n'a pas le temps de réagir")
        else:
            print("Tu cours avec ton arme blanche dans la main et tranche le bas du dos de la créature mais elle ne meurt pas.")
        print("Tu donnes assez de temps à ton équipe pour qu'ils prennent l'orbe qui étais gardé par la créature")
        print("Yondu te gueule pour que tu rentres dans le vaisseau la mission étant accomplie.")
    else:
        print("Tu fais trop de bruit, la bete te vois et te fonce dessus")
        print("T'essaies donc de courir et de fuir la créature")
               
def combat():   
    reponse = input("Essayer de la combattre ou rester discret ?")
    while reponse not in ["discret", "combattre"]:
        print("hein ? c'est discret ou combattre.")
        reponse = input("ta reponse ?")
    if reponse == "discret": 
        print("Kraglin te dit d'aller par un des côtés de la bete en te cachant derrière des piliers")
        reponse = input("Aller à gauche ou droite ?")
        while reponse not in ["gauche", "droite"]: 
            print("hein ? c'est oui ou non.")
            reponse = input("dcp?")
        if reponse == "gauche":
            print("Tu t'encoubles sur une pierre et t'ouvre le coude en tombant")
            print("Tu fais trop de bruit, la bete te vois et te fonce dessus")
            print("T'essaies donc de courir et de fuir la créature")
        elif reponse == "droite":
            print("Tu arrives aux arrières de la bête et fait signe aux autres de venir")
            print("Tu trouves un sac de rubis par terre, tu le ramasse et le range dans ton porte monnaie")
    elif reponse == "combattre":
        test_dexterite()
 
def funeraille():
    reponse = input("Faire des funérailles à Kraglin plus tard ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("donc?") 
    if reponse == "oui":
        print("Tu acceptes finalement et il te promet qu'une fois tout ça fini, vous lui ferez des funérailles sous les plus belles galaxies.")
    elif reponse == "non":
        print("Tu lui dis que tu préfères que Kraglin puisse reposer en paix") 
        print("Il te propose alors de te reposer pour que demain tu te sentes mieux.")
        if "casse_tete" in sac:
            print("Il te souris en voyant le prendre et te propose de t'emmener chez toi si tu arrives à le résoudre")
        else:
            print(" Il te souris en voyant le prendre et te propose de t'emmener chez toi si tu arrives à le résoudre")
        reponse = input("T'obstiner à le réussir ?")   
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("alors?")    
        if reponse == "oui":
            print("Tu as l'air déterminé à réussir le cassé-tête et tu peux apercevoir une fierté dans le regard du commandant.")  
        elif reponse == "non":
            print("Tu décides de laisser couler l'envie de rentrer à la maison. Te joindre à l'equipe semble pas si mal au final.")
        print("Yondu fini par te dire d'aller dormir.")
        reponse = input("tenter de resoudre le casse tete")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")                       
        if reponse == "oui":
            print("Tu y passes toute la nuit et en fait, tu le résous même assez rapidement.")
            print("Tu décides de le ranger dans ta poche et de tenter de t'endormir.")
        elif reponse == "non":
            print("Tu décides de le ranger dans ta poche et de tenter de t'endormir.")
            
        if dexterite >= 25:
            print("Tu arrives à fuir jusqu'au vaisseau et tu vois que Kraglin peine à arriver au vaisseau et qu'il risque de pas réussir à monter.")   
            if dexterite >= 30:
                print("Tu le tire de justesse dans le vaisseau et vous tomber les deux essouffés dans le vaisseau.")
                print("Tu te regardes avec Kraglin en riant avant de soupirer profondément, épuisé")
                print("Il te salue d'un signe, part au cockpit pour sortir de la zone d'ordination de cette planète et tu pars dans ta chambre")
            else:
                print("Tu n'arrives pas à attraper le main de Kraglin et il se fait attraper par le monstre qui le lamine")
                if relation_Kraglin >= 45:
                    print("Tu es tellement attristé par son décès violent devant tes yeux que tu te jettes du vaisseau")
                    exit()  # jsp cmmt on revient au debut du jeu dcp je mets ça en attendant
                else:
                    print("Tes furieux que Yondu n'ait rien fait pour le sauver que tu pars dans ton coin dans le vaisseau.")
                    print("Yondu vient te voir et il semble tout autant malheureux en te regardant.")
                    reponse = input("etre sensible avec lui?")
                    while reponse not in ["oui", "non"]:
                        print("hein ? c'est oui ou non.")
                        reponse = input("oui ou non ?")                           
                    if reponse == "oui":
                        print("Tu finis par t'excuser et il te propose de te dire qui Kraglin était")
                        print("Il te racontes des aventures sans fin de qui il était et te propose que quand l'orbe est rendu à l'acheteur, que vous fassiez des funérailles pour Krag.")
                    elif reponse == "non":
                        print(" Tu ne le laisse même pas s'expliquer que tu l'insultes déjà de tous les noms possibles.")
                        reponse = input("Il te demande si tu veux qu'il te laisse tranquille ?")
                        while reponse not in ["oui", "non"]:
                            print("hein ? c'est oui ou non.")
                            reponse = input("oui ou non ?")   
                        if reponse == "oui":
                            print("Il murmure ce qui semble être un Désolé et ferme la porte derrière toi")
                        elif reponse == "non":
                            print("Tu finis par t'excuser et il te propose de te dire qui Kraglin était") 
                            print("Il te racontes des aventures sans fin de qui il était et te propose que quand l'orbe est rendu à l'acheteur, que vous fassiez des funérailles pour Krag.")
                            funeraille()
        else:
            print("Tu essaies de fuir la bête mais tu tombe dans des débris du pilier que la bête viens de casser")
            if relation_Yondu>= 40:
                print("Yondu siffle et sa flèche vient à toute vitesse")
                print("Il te siffle. de manière à ce que tu comprenne qu'il te faut la prendre")
                print("Tu prends la flèche et il te tire à l'intérieur du vaisseau")
                print("Tu te regardes avec Kraglin en riant avant de soupirer profondément, épuisé")
                print("Il te salue d'un signe, part au cockpit pour sortir de la zone d'ordination de cette planète et tu pars dans ta chambre")
            else:
                print("Yondu te regarde dans les yeux, secoue l'orbe devant toi et rentre dans le vaisseau, sans même t'aider à te sortir des débris")
                print("T'essaies d'appeler à l'aide, mais le vaisseau ferme la porte")
                print("Tu sais qu'ils ne reviendront plus.")
                print("La haine te consume, tu prend ton arme et tu massacres la créature.")
                print("Tu restes sur la planète et massacre tout mercenaire qui y rentre.")
                print("TU es devenu la créature que la planète craint. Beaucoup tentent de te tuer, tous échouent. Tu reverras plus jamais les ravageurs.")
                print("game over buddy")
                intro() #game over blahblah
        
def faim():
    if "sandwich" in sac:
        print("Tu commences alors à manger le sandwich et tu le finis")
    elif "chocolat" in sac:
        print("Tu souris et la douceur se fait déjà ressentir, le chocolat dure peu dans ta bouche")
    elif "barre de cereal" in sac:
        print("Meme si ça n'a pas l'air appétissant, ça te rempli bien l'estomac")
    elif "bouteille deau" in sac:
        print("Tu t'hydrate bien et tu soupir en t'adossant contre un mur, ventre rempli avec ce que tu avais")
    else: 
        print("tu n'as rien à manger.")  #je sais, c'st pas dans miro mais brf
    reponse = input("as tu encore faim?")   
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")   
    if reponse == "oui":
        faim()
    elif reponse == "non":   
        print("Le ventre bien rempli tu te décides d'aller te reposer et attendre pour la prochaine mission, si y en a une.")      #sur miro ya une flèche qui mène à ce dialogue mais j'ai trouvé ça bizarre vu que à tout moment le personnage a rien manger et on dit qu'il a l'estomac rempli mais brf
        
def episode_6():
    print("Tu lui dis que tu vas bien et il commence à te parler de la mission")
    reponse = input("Il te demande si la mission a été ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("Tu dis que c'était assez marrant et il commence à te faire des blagues assez sympa pour te mettre à l'aise")
        print("Tu commences à bien rigoler avec lui et à te sentir à l'aise, moins effrayé")
        reponse = input("Il te demande si tu as hate de la prochaine mission ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Tes yeux brillent déjà rien que de penser à ce que vous allez encore faire")
        elif reponse == "non":
            print("Tu  lui avoues avoir quand meme peur de ce qui peut arriver il se montre assez compréhensif avec ça et te dis que t'y prendras gout.")
        reponse = input("Il te demandes si la fatigue commence à prendre le dessus ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Tu tente encore de détourner la chose mais tu bailles et il en ricanne")
            print("Il se moque de toi avec gentillesse et te conseilles d'aller dormir, t'accompagnant jusqu'à la chambre")
        elif reponse == "non":
            print("Il remarque t'es yeux fatigués, lui aussi il l'est. Mais il te sourit de manière rassurante et te propose de juste discuter et jouer aux cartes")
            print("Après quelques parties d'un faux poker qui avait un peu de rubis en jeu, il te dit qu'il allait fermer les yeux deux petites minutes, mais tu remarques vite qu'il s'est endormi")
            print("tu le couvres et tu t'assures que le vaisseau et en pilote automatique et tu pars dans ta chambre")    
        episode_7()
    elif reponse == "non": 
        print("Tu lui avoues que tu n'as pas du tout aimé l'ambiance et que c'est pas pour toi.")
        reponse = input("Il te demande si tu veux quand meme finir celle-là ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Il t'ébouriffe les cheveux rassuré et décides de te poser une question")
        elif reponse == "non":    
            print("Tu lui confit le fait que tu veux pas finir celle là et il soupir peiné")
            reponse = input("Est-ce que tu veux rentrer chez toi ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui":
                print("Il semble très triste mais décide d'accomplir ta volonté en changeant le cap et te laissant alors sur terre.")
                print("Yondu n'arrive pas à temps de te rattraper, Kraglin arrive à partir avant pour que tu puisses vivre en paix.")
                exit()  #gaaaaame over
            elif reponse == "non":  
                print("Il est bien heureux que tu veuilles rester")
        orbe_reveal()                      

def informations():
    print("Tu manges ton plateau avec lui et tu as quelques questions en tête.")
    reponse = input("Lui demander ce qu'est cet orbe qu'ils ont volés ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("Yondu t'expliques que l'orbe contient la Power Stone et que ça vaut cher au marché")
        informations()
    elif reponse == "non":
        reponse = input("Lui demander si tu fais partie de l'équipe maintenant ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Il a l'air assez scéptique par la question mais il aquiesce. Il semble quand meme réticent.")
            informations()
        elif reponse == "non":
            reponse = input("Le questionner sur la prochaine mission ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui": 
                print("Il te dis de ne pas trop te préoccucper avec ça. Mais il te raconte quand même que la prochaine mission est d'aller sur Xandar trouver les GotG")
                informations()
            elif reponse == "non":
                print("tu lui demandes si tu peux rentrer chez toi")   # ici j'ai pas suivi le mindmap parce qu'il manque une fleche 
                print("Il fronce les sourcils et te demande d'un air amusé si tu as résolu le casse-tête en bois")
 
 
 
def la_petite_voix():
    reponse = input("les thèmes qu'elle te propose sont: son passé, les ravageurs, les pierres ou sa mort")
    while reponse not in ["sont passé", "les ravageurs", "les pierres", "sa mort"]:
        print("choisis un des themes proposés.")
        reponse = input("alors ?")      
    if reponse == "sa mort":
        print("La voix te dit qu'il était un mercenaire et qu'il y a longtemps de cela il avait aussi eu comme mission de prendre cette pierre.")
        reponse = input("l'mpecher de divaguer et demander d'aller droit au but?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Il te dis que t'es comme les gens qui parlent au cinéma et que tu gâches tout le jeu.")
            print("Il te résume toute l'histoire")
        elif reponse == "non":
            print("Tu l'écoute patiemment te raconter tes mésaventures.")
        la_petite_voix()        
    elif reponse == "son passé":    
        print("La voix te dis que son prénom c'est Wade, son nom de famille Wilson mais que généralement on l'appelle Deadpool")
        reponse = input("Demander pourquoi Deadpool ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("La voix t'expliques que c'est un jeu de pari dans le bar qu'il fréquente sur le prohain mercenaire qui doit crever.")
        elif reponse == "non":    
            print("Tu préfères te dire qu'il est complétement taré et qu'il a dû mourir dans une piscine.")
        la_petite_voix()  
    elif reponse == "les ravageurs": 
        print("Il te raconte qu'il devait tuer un des Ravageurs pour prendre la fameuse pierre mais qu'il a fini mort.")
        la_petite_voix()
    elif reponse == "les pierres":
        print("La voix dit que depuis des décénies, ces pierres sont recherchées par des milers sans que personne sache ce qu'elles sont réellement")
        reponse = input("Questionner comment Yondu les connait du coup ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Elle dit que maintenant que Thanos est apparu, la connaissance des pierres est devenue de la culture G")
        elif reponse == "non":    
            print("Elle dit que maintenant que Thanos est apparu, la connaissance des pierres est devenue de la culture G")        
        reponse = input("Demander pourquoi Thanos est consideré comme si... grandiose ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Elle t'explique qu'il escravise des peuples entiers ou les extermine pour atteindre son but.")
            reponse = input("Demander si elle à déjà été une de ces personnes sous son contrôle OU demander si elle était une de ses allié ?")
            while reponse not in ["allié", "contrôle"]:
                print("hein ?")
                reponse = input("allié ou contrôle ?")      
            if reponse == "allié":
                print("Alliée est un grand mot mais elle te dit que partiellement.")
                reponse = input("Demander des précisions sur le statut entre la voix et Thanos ?")
                while reponse not in ["oui", "non"]:
                    print("hein ? c'est oui ou non.")
                    reponse = input("oui ou non ?")      
                if reponse == "oui":
                    print("Il te dit qu'il a bossé pour lui. Mais qu'il a jamais eu sa paye, vu qu'il est mort.")
                    reponse = input("encore une question ?")
                    while reponse not in ["oui", "non"]:
                        print("hein ? c'est oui ou non.")
                        reponse = input("oui ou non ?")      
                    if reponse == "oui":
                        la_petite_voix()
                    elif reponse == "non":  
                        print("Yondu remarque que tu sembles perdue dans tes pensées")
                        print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                        episode_7()                     
                elif reponse == "non":
                    reponse = input("encore une question ?")
                    while reponse not in ["oui", "non"]:
                        print("hein ? c'est oui ou non.")
                        reponse = input("oui ou non ?")      
                    if reponse == "oui":
                        la_petite_voix()
                    elif reponse == "non":  
                        print("Yondu remarque que tu sembles perdue dans tes pensées")
                        print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                        episode_7()                  
            elif reponse == "contrôle":    
                print("Avec honte, partiellement, elle te dit qu'elle était plus consentante que ce que tu pourrais imaginer.")
                reponse = input("Lui demander si ce n'était qu'elle ou si c'était tout son peuple ?")
                while reponse not in ["oui", "non"]:
                    print("hein ? c'est oui ou non.")
                    reponse = input("oui ou non ?")      
                if reponse == "oui":
                    print("Elle t'explique que c'était juste elle, mais que plus d'une peronne de so peuple ont aidés Thanos.")
                    la_petite_voix()
                elif reponse == "non":   
                    print("Elle t'apprend avoir été une clé certaine pour Thanos de son vivant")
                    reponse = input("Demander si elle est morte ?")
                    while reponse not in ["oui", "non"]:
                        print("hein ? c'est oui ou non.")
                        reponse = input("oui ou non ?")      
                    if reponse == "oui":
                        print("Elle te dit que chaque conscience et pressentiment ne sort pas de nulle part")
                        reponse = input("Demander si chaque avertissement invisible vient de quelque part ?")
                        while reponse not in ["oui", "non"]:
                            print("hein ? c'est oui ou non.")
                            reponse = input("oui ou non ?")      
                        if reponse == "oui":
                            print("Elle t'explique que ça dépend. et que l'après mort a beaucoup de variables en jeu.")
                            reponse = input("Demander si c'est comme une histoire à choix ?")
                            while reponse not in ["oui", "non"]:
                                print("hein ? c'est oui ou non.")
                                reponse = input("oui ou non ?")      
                            if reponse == "oui":
                                print("Elle semble s'exciter et doit visiblement hocher la tête, mais tu vois rien.")
                                reponse = input("Lui demander si elle sait comment ce déroule cette histoire ?")
                                while reponse not in ["oui", "non"]:
                                    print("hein ? c'est oui ou non.")
                                    reponse = input("oui ou non ?")      
                                if reponse == "oui":
                                    print("Elle t'explique que tout commences avec une 'voix narratrice en formation qui choisi une personne et la maudit à son tour' ")
                                    print("Tu commences à tout comprendre maintenant.")
                                    reponse = input("Demander pourquoi elle t'as maudit ?")
                                    while reponse not in ["oui", "non"]:
                                        print("hein ? c'est oui ou non.")
                                        reponse = input("oui ou non ?")      
                                    if reponse == "oui":
                                        print("La voix en rit et te dit que ça l'amuse")
                                    elif reponse == "non":    
                                        print("La voix dit qu'elle ne t'en veux pas personnellement mais que c'est comme ça")
                                    reponse = input("encore une question ?")
                                    while reponse not in ["oui", "non"]:
                                        print("hein ? c'est oui ou non.")
                                        reponse = input("oui ou non ?")      
                                    if reponse == "oui":
                                        la_petite_voix()
                                    elif reponse == "non":  
                                        print("Yondu remarque que tu sembles perdue dans tes pensées")
                                        print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                                        episode_7()                
                                elif reponse == "non":    
                                    print("Tu préfères même plus approfondir le sujet. Ca te donne des frissons.")
                                    reponse = input("encore une question ?")
                                    while reponse not in ["oui", "non"]:
                                        print("hein ? c'est oui ou non.")
                                        reponse = input("oui ou non ?")      
                                    if reponse == "oui":
                                        la_petite_voix()
                                    elif reponse == "non":  
                                        print("Yondu remarque que tu sembles perdue dans tes pensées")
                                        print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                                        episode_7()                
                            elif reponse == "non":  
                                print("Elle te décrit ça comme quelque chose de confus. Auquel tu commences à jouer sans même t'en rendre compte.")
                                reponse = input("encore une question ?")
                                while reponse not in ["oui", "non"]:
                                    print("hein ? c'est oui ou non.")
                                    reponse = input("oui ou non ?")      
                                if reponse == "oui":
                                    la_petite_voix()
                                elif reponse == "non":  
                                    print("Yondu remarque que tu sembles perdue dans tes pensées")
                                    print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                                    episode_7()                  
                        elif reponse == "non":  
                            print("Tu penses que cette voix est simplement folle.")  
                            reponse = input("Arrêter de parler définitivement à la voix ?/!\ CETTE ACTION AURA DES CONSE+QUENCES GRAVES ET IRREVERSIBLES.")
                            while reponse not in ["oui", "non"]:
                                print("hein ? c'est oui ou non.")
                                reponse = input("oui ou non ?")      
                            if reponse == "oui":
                                print("Tu vas regretter.")
                                episode_7()
                            elif reponse == "non":   
                                reponse = input("encore une question ?")
                                while reponse not in ["oui", "non"]:
                                    print("hein ? c'est oui ou non.")
                                    reponse = input("oui ou non ?")      
                                if reponse == "oui":
                                    la_petite_voix()
                                elif reponse == "non":  
                                    print("Yondu remarque que tu sembles perdue dans tes pensées")
                                    print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                                    episode_7()                                
                                
                    elif reponse == "non":   
                        print("Elle te répond, même sans question, qu'une voix n'est pas sortie de nulle part.")
                        la_petite_voix()
        elif reponse == "non":
            print("La voix semble simplement soupirer et l'insulta de 'titan violet tyranique'")
            reponse = input("Demander ce qu'est un titan ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui":
                print("Elle t'explique qu'il est juste très grand et un dictateur. de la galaxie entière.")
            elif reponse == "non":
                print("La voix soupir et demande la boule au ventre si t'as encore une question.")
            reponse = input("encore une question ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui":
                la_petite_voix()
            elif reponse == "non":  
                print("Yondu remarque que tu sembles perdue dans tes pensées")
                print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                episode_7()
                
def episode_7():
    print("Tu quittes le cockpit pour te reposer dans ta chambre en remarquant qu'elle à l'air plus accueillante.")
    print("Le lendemain t'es devant la trappe qui déballe sur l planète de rencontre avec les GotG")
    print("Tu descend du vaisseau en checkant ton inventaire.")
    if "arme blanche" in sac: #quelle arme blanche ?
        print("Tu t'amuses à l'empoigner d'une main et poignarder le vide en regardant tes amis arriver")
    else:
        print("Tu fouilles dans ton sac pour voir quelle arme est-ce que t'as pris")
        print("et tu vérifie le chargeur qui est complet.")  #dans le miro ya une bulle violette à ce moment qui verifie s'il y a des armes à feux dans linventaire, mais ya aucune fleche qui orend en compte la possibilité qu'il n'y ait pas d'arme à feux, alors voila je savais pas quoi faire
    if "ecouteurs"  in sac:
        print("Tu fouilles tes poches pour voir si t'as quelque chose à grignoter.")
        print("Tu te demanda ce que t'as bien piu faire pour rien manger.") #again bulle violette mais que 1 option possible  
        print("La petite voix se moque de toi.")
    else:
        print("Tu mets tes écouteurs un moment en descendant du vaisseau tout en t'ambiançant sur 'warriors' Imagine Dragons")
        print("Tu t'adosse contre un mur en attendant que quelqu'un descende") #meme chose ici
        if "casse-tête en bois" in sac:
            print("Tu commences à le résoudre pour passer le temps.")
        else: 
            print("tu attends avec ennuis")
    print("Un main se pose sur ton épaule, le commandant qui te dit de descendre pour faire la rencontre de l'équipe.")
    print("Tu descend du vaisseau, arme à la main, prêt à tirer si necessaire.")
    print("Tu vois les gardiens prendre leurs armes aussi, le raton laveuur semble pas vouloir jouer.")
    reponse = input("leur demander ce qu'ils veulent?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")    
    if reponse == "oui":
        print("ils repondent qu'ils veulent la pierre")  #mindmap pas terminé
    elif reponse == "non":
        print("Tu vois juste un humain entre eux et il te fait de la peine. Il semble avoir de la nostalgie dans le regard.")
        reponse = input("demander si c'est peter Quill ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")   
        if reponse == "oui":
            print("Tu demandes si c'est bien lui.")
            reponse = input("Il te demandes ce que tu sais de lui. Répondre ?")  #mindmap pas terminé
        elif reponse == "non":
            print("Convaincu d'avance que c'était lui, tu te racles la gorge")
            print("Lui dire que Yondu t'as beaucoup parlé de lui.")   
            reponse = input("Il te demandes si tu veux le tuer ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")     
            if reponse == "oui":
                print("T'as simplement le temps d'entendre un sifflement.")
                print("La flèche de Yaka te travèrse. Yondu a pris ça comme une trahison et t'as tué.")
                exit() #game over
            elif reponse == "non":
                print("Tu lui dis que malgré son abandon, tu comprends.")
                print("Il te raconte en bref son passé et traumatisme d'avoir été avec les Ravageurs.")    
                reponse = input("Rejoindre les Gardiens et abandonner les Ravageurs ?")  #finir le mindmap
                while reponse not in ["oui", "non"]:
                    print("hein ? c'est oui ou non.")
                    reponse = input("oui ou non ?")
                if reponse == "oui":
                    print("Alors que tu te prépares à fuir, la petite voix t'appelle et te sors complétement de ce monde.")
                    print("Tu te retrouves face à sa silouhette iconique et il te souris malgré son visage defiguré.")                    
                    reponse = input("Lui demander comment il a fait ça ou pourquoi ?")
                    while reponse not in ["pourquoi", "comment"]:
                            print("hein ? c'est pourquoi ou comment.")
                            reponse = input("alors ?")  
                    if reponse == "pourquoi":
                            print("Il t'explique que si tu pars, ce sera un adieu.")
                            reponse = input("Demander Comment ça un adieu ? un adieu ?")
                            while reponse not in ["oui", "non"]:
                                print("hein ? c'est oui ou non.")
                                reponse = input("oui ou non ?")   
                            if reponse == "oui":
                                print("Il t'explique que si tu pars avec les gardiens il ne pourra plus te parler. Sa mission s'achève là")
                            elif reponse == "non":
                                print("Tu te montres indifférent et le fixe simplement l'air de dire ouais et ?")     
                                reponse = input("Il te demande ce que l'amitié que vous aviez signifiait pour toi.")
                                while reponse not in ["rien", "une bonne experience", "tout"]:
                                    print("tout rien ou une bonne experience")
                                    reponse = input("reponse ?") 
                                if reponse == "rien":
                                    print("Il ricanne et roule des yeux en se foutant de toi.")   #le reste est pas fini 
                                                                                
                                  
                                               
def orbe_reveal():
    reponse = input("Est-ce que tu veux savoir ce que c'est cet orbe ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("Selon les rumeurs, la pierre du pouvoir, une des 6 plus puissantes de l'univers.")
    elif reponse == "non":
        print("Il hausse les épaules disant que c'est dommage mais que ça vau très cher.")
    reponse = input("Tenter de mettre les mains sur cette relique ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("Tu décides de penser à comment mettre la main sur cette pierre")
    elif reponse == "non":   
        print("Tu te dis que c'est pas pour toi et tu preferes rester dans une vie sans pierres magiques.")
    print("Kraglin te vois pensif face à la pierre et te dis que tu devrais plutôt penser à te reposer.")
    reponse = input("Si tu avais l'orbe, tu le garderai pour toi meme?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("La petite voix semble inquiète par ce choix et tente de t'en dissuader")
    elif reponse == "non":    
        print("La petite voix qui t'écoute toujours en est rassurée et te previent qu'il vaut mieux pas s'en mêler")
    print("Elle te conseilles de ne pas laisser le pouvoir te monter à la tête")
    reponse = input("Kraglin demande avec qui tu parles. Dire la vérité  ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("Tu lui dis que t'as une voix qui te parle depuis peu avant ton kidnapping")
        print("Il te demande assez pâle si cette voix à unnom")
        reponse = input("demander à ta voix amie son nom ?")
        while reponse not in ["oui", "non"]:
             print("hein ? c'est oui ou non.")
             reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Tu tentes de lui demander son nom, et sa voix tremble.")
            reponse = input("Est-ce que tu es sûr de lui demander ça ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui":
                print("Elle te dis qu'elle te le dira peut-être en temps voulu.")
            elif reponse == "non":   
                print("Tu préfères laisser ça couler et pas insister. après tout, elle n'avait pas quitté tes côtés")
        elif reponse == "non":
            print("Tu dis simplement et bêtement qu'elle n'a pas de nom, à part voix amie")
            print("Il en rit et te traite de pschyso et te conseille de juste aller te reposer")
    elif reponse == "non":   
        print("Tu dis que tu parles juste seul. ça le fait marrer")
        print("La petite voix te dis de ne jamais parler de sa présence à qui que ce soit sinon elle partira pour ne plus revenir.")
        reponse = input("Demander le pourquoi de cette demande ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("La petite voix te dit que si tu parles d'elle, tout le monde oubliera qui elle avait été") #il manque une flèche 
        elif reponse == "non":
            print("Tu ne questionnes pas ta voix amie qui était d'ailleurs étrangement silencieuse depuis qu'elle s'était liée d'amitié avec les deux Ravageurs.")
            print("T'es juste d'accord avec elle et Kraglin te propose un petit combat amicale pour t'entraîner un peu")
            if "arme blanche" in sac:
                print("Il sourit en te voyant prêt pour t'entraîner et t'apprends à te mettre en place")
                print("vous vous amusez en combat malgré quelques chutes")
            else:
                print("Tu lui dis être fatigué, il comprend et te souhaites une bonne nuit.")
    episode_7()
    
print("Tu te reposes alors toute la nuit")
print("Le lendemain, Yondu vient te réveiller pour te demander si tu veux prendre un petit déjeuner")
reponse = input("Lui dire que tu vas manger seul, ou accepter ?") 
while reponse not in ["seul", "accepter"]:
    print(" c'est seul ou accepter les reponses.")
    reponse = input("alors ?")                              
if reponse == "seul":
    faim()
    print("Tu vas au cockpit dans l'espoir d'y trouver ton ami krag") # ici il manquait une flèche sur miro dcp j'ai ignoré une bulle.
    if kraglin in equipe:  
        print("Il te fait un peu mal mais tu sens les plaies être maintenues en place")
        reponse = input("Lui demander de t'aider avec les soins ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")    
        if reponse == "oui":
            print("Il te laisse entrer et te propose de commencer par les grosses blessures")
            print("Il te fait un peu mal mais tu sens les plaies être maintenues en place") 
            reponse = input("veut tu discuter?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")   
            if reponse == "oui":
                episode_6()
            elif reponse == "non":                                
                print("Il espère t'avoir aidé et te souhaite un bon repos")
                episode_7()
        elif reponse == "non":   
            episode_6()
    else:
        print("Tu t'attendais déjà à ce que tu as vu. Rien. Kraglin n'était évidemment plus là")
        print("Tu te mets aux commandes du vaisseau qui était encore sous pilote automatique")
        reponse = input("piloter le vaisseau ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")            
        if reponse == "oui":
            print("tu prends les commandes de pilote pendant quelques instants")
            if pilotage > 20:
                print("Tu arrives à guider le vaisseau dans la bonne direction et tu sais que Krag's serait fier de toi.")
            else:
                print("Tu essaies de reprendre les commandes, mais tu ne réussi pas et tu fais crasher le vaisseau.")
                print("Tu as tué tout l'équipage, toi inclus. Au moins maintenant tu as rejoins ton ami")    
                exit() #js tjrs pas faire un game over
        elif reponse == "non":
            print("Par respect à Kraglin, tu ne prends pas les commandes du vaisseau. tu préfères tasseoires à côté de la fenêtre pour admirer les constellations")
            print("Tu regardes au loin la planète sur laquelle tu étais y a pas si longtemps et tu jure vengeance")   
        episode_7()
elif reponse == "accompagné":
    print("Tu hésite mais tu finis par accepter pour discuter avec lui et te changer les idées")
    reponse = input("Est-ce que tu demandes à t'entrainer pour augmenter tes stats ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("Il te demande de sortir ton arme et te guide")
        if "revolver" or "blaster" or "fusil" in sac:
            print("Il te mets une cible au loin et t'apprend alors à bien viser les points vitaux")
        else:
            print("Il te propose quelques exercices pour t'aider à manier ton arme blanche plus facilement")
        print("Il te félicites pour tes résultats et te propose d'aller manger en tant que récompense")
        dexterite +=15        # peut etre augmenter la relations entre les perso aussi ?
    elif reponse == "non":
        print("tu ne t'entraines pas.")
    print("Vous allez à une espèce de réfectoire et il te tend un plateau avec plusieurs choses à manger")
    informations()  
    if "bois résolu" in sac:
        print("Il regarde l'objet dans ta main et hoche finalement la tête en te regarde")  
        reponse = input("Il te demande si tu veux vraiment rentrer ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Il change le cap du vaisseau et t'emmènes sur terre où il te laisse finalement")
            print("Il te laisse sur terre avec comme seul souvenir le casse-tete, récupérant les armes prêtées")
            exit() #game end
        elif reponse == "non":
            print("Il semble rassuré et te tapote amicalement le dos") #relatiin ameliorée ?
    else:
        print("Il en ricanne un peu mais tu peux voir que ça le rassure que tu n'aies pas réussi de le résoudre")
    print("Il te dis que si vraiment tu veux rentrer chez toi après la prochaine mission, il t'y emmenera de lui-meme")
    print("Il te propose d'aller te reposer pour voir l'orbe pour que tu comprennes pourquoi il le voulait.")
    reponse = input("Aller voir l'orbe ?")
    while reponse not in ["oui", "non"]:
        print("hein ? c'est oui ou non.")
        reponse = input("oui ou non ?")      
    if reponse == "oui":
        print("t'es assez scéptique mais il te montre l'orbe et le fait tourner dans un paterne qui semble contrôlé")
        reponse = input("Demander ce qu'est cet orbe ?")
        while reponse not in ["oui", "non"]:
            print("hein ? c'est oui ou non.")
            reponse = input("oui ou non ?")      
        if reponse == "oui":
            print("Il t'explique que cet orbe contient donc la pierre du pouvoir.")
            reponse = input("Lui demander ce que c'est plus précisément ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui":
                print("Il t'explique que lors du Big bang, 6 pierres ont été créer pour proteger l'univers")
                reponse = input("Demander ce qu'il compte faire avec ?")
                while reponse not in ["oui", "non"]:
                    print("hein ? c'est oui ou non.")
                    reponse = input("oui ou non ?")      
                if reponse == "oui":
                    print("Il ricanne et te dis qu'il compte la vendre au marché noir inter-galactique")
                elif reponse == "non":    
                    print("Tu as très peur de lui demander pourquoi il veut la pierre et tu decides de simplement le regarder avec la pierre à la main")
                print("Il te montre la pierre et te conseilles de dormir et que demain tu vas peut-être même jouer un peu avec.")
                episode_7()    
            elif reponse == "non": 
                print("Tu vois la pierre violette et il te regarde très sérieusement.")
                print("Il te prévient que si il découvre que tu as touché la pierre, il te tue avec sa flèche")
                print("Il te demande si part hasard tu venais à mettre les mains dessus, utiliserais-tu la pierre ?")
                if peur >= 10:
                    print("Tu lui avoues que non, t'aurais pas utilisé la pierre pour ton propre interêt")
                    print("Il te dit être fier et que c'est ça être un Ravageur.")
                    print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                    episode_7()   
                else:
                    print("Tu souris simplement pour dire que ouais, t'aurais utilisé la pierre si tu pouvais")
                    print("Il te pointe alors la pierre de la main en souriant, sadiquement")
                    reponse = input("Il te dit de prendre la pierre.La prendre ?")
                    while reponse not in ["oui", "non"]:
                        print("hein ? c'est oui ou non.")
                        reponse = input("oui ou non ?")      
                    if reponse == "oui":
                        print("Tu tends ta main vers la pierre mais t'entends la petite voix te crier dessus pour pas que tu la touche")
                        reponse = input("la voix te suppie de ne pas toucher la pierre.L'écouter ?")
                        while reponse not in ["oui", "non"]:
                            print("hein ? c'est oui ou non.")
                            reponse = input("oui ou non ?")      
                        if reponse == "oui":
                            print("Tu n'y touches pas, te demandant comment elle savait pour la pierre.")
                            reponse = input("Lui demander une fois dehors comment elle savait ?")
                            while reponse not in ["oui", "non"]:
                                print("hein ? c'est oui ou non.")
                                reponse = input("oui ou non ?")      
                            if reponse == "oui":
                                print("La petite voix soupire profondément et te dis qu'elle connait mieux les pierres que ce que tu croit.")
                                la_petite_voix()
                            elif reponse == "non":
                                print("La petite voix ne te parle pas malgré toutes les tentatives de la faire parler")
                                reponse = input("Essayer de la faire parler et insister ?")
                                while reponse not in ["oui", "non"]:
                                   print("hein ? c'est oui ou non.")
                                   reponse = input("oui ou non ?")      
                                if reponse == "oui":
                                    print("La voix soupir en te disant qu'elle a un long passé avec les pierres.")
                                    reponse = input("Demander si les pierres l'ont tués ?")
                                    while reponse not in ["oui", "non"]:
                                       print("hein ? c'est oui ou non.")
                                       reponse = input("oui ou non ?")      
                                    if reponse == "oui":
                                        print("La voix aquiesce, en ricannant te disant que c'est bien la seule chose qui pouvait tuer un immortel jusqu'à ce jour.")
                                        print("Tu comprends pas et la voix te dit que Deadpool est connu")
                                    elif reponse == "non":
                                        print("Tu hoches la tête et lui propose de la laisser en paix.")
                                    episode_7            
                                elif reponse == "non":    
                                    print("Tu la laisse tranquille et te dis que demain tu lui reparleras de ce qui s'est passé")
                                    print("Tu termines ta conversation avec Yondu et pars te coucher")
                                    print("Le lendemain soir, lors d'une discussion avec Yondu, la petite voix te dit qu'elle est prête à se confier")
                                    la_petite_voix()
                        elif reponse == "non":    
                            print("Tu roules des yeux et tu prends la pierre dans les mains.")
                            print("Tu sens tes mains brûler et le pouvoir dela pierre couler dans tes veines. tu veux la scéller et tu réussi, devenant le nouvel orbe protecteur de la pierre")
                            exit()# game over
                    elif reponse == "non":     
                        print("Tu lui fais signe qu'il vaudrait mieux pas la toucher")
                        print("Yondu se dit que tu changes bien vite d'avis. Girouettte va.")
                        print("Il te propose d'aller te coucher et demain vous ferez la mission pour donner l'orbe à l'acheteur.")
                        episode_7()  
        elif reponse == "non":  
            print("Tu le regardes simplement ouvrir l'orbe et il tourne une demi-sphère pour faire tomber une pierre violacée")
            print("Tu admires la pierre un bon moment, comprenant pourquoi elle est recherchée. tu ressens le pouvoir rien qu'en la regardant.")
            reponse = input("Demander qui veut cette pierre ?")
            while reponse not in ["oui", "non"]:
                print("hein ? c'est oui ou non.")
                reponse = input("oui ou non ?")      
            if reponse == "oui":
                print("Il te dit que c'est Thanos pour gouverner la galaxie et que lui veut protéger la pierre")
                print("Tu es assez confus sur qui est Thanos et tu dis que t'as besoin de dormir pour réflechir mieux demain.")
            elif reponse == "non":  
                print("Tu regardes bêtement la pierre, un peu ennuyé par ça")
                print("Tu dis qu'il a qu'à garder ce bout de roche magique et que toi tu préfères garder ta sanité")
            episode_7()        
    elif reponse == "non":
        print("Tu décides de refuser l'offre et de pas te mêler avec cette pierre dans l'orbe")
        episode_7()            
        
intro()                                  
vaisseau()
n_ourriture()
episode_2()
rencontre()
partie_3()
visite()
kraglin()
nar()
test_dexterite()
    