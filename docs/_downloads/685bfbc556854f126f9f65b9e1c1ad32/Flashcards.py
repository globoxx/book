import json  # Pour sérialiser et désérialiser des données pour le format json l'import du module json est nécessaire.
import random  # Dans le but de pauser les questions en aléatoire importer le module random est nécessaire.


class Question:  # Je vous recommande de lire les définions de la classe question que lorsque le programme y fait appel
    # (les commentaires sont écrit dans l'ordre chronologique du déroulement du programme et non dans l'ordre des lignes
    # de code. Je pourrai faire référence à des éléments passé du programe dans les définitions)
    def __init__(self, q, a, n):
        """
        Ceci est la méthode d'initialisation pour une question, elle utilise des object de types str(), int() entré en
        paramètres (q pour question, a pour réponse, n pour nombre de points) pour créer un seul object de
        type(= de classe) : Question.
        """
        self.q = q
        self.a = a
        self.n = n

    def ask(self):
        """
        Ceci est la méthode utilisée pour tester l'utilisateur avec les question enregistrée au préalable.
        Ici ua est la réponse entrée par l'utilisateur, elle peut être str() (dans ce cas, quand la méthode retourne 3,
        le programme intérprète la réponse vide comme "passer la question", auqun point n'est enlevé ou ajouté.)
        """
        ua = input(f"{self.q} :\n")
        if not ua:  # Si la réponse est str() (-> vide) la méthode retourne 3
            return 3
        if ua == self.a:  # Si la réponse est juste ont retire un point (valeur self.n)
            self.n -= 1
            if self.n == 0:  # Si il n'y as plus de points la méthode retourne 2
                return 2
            return 1  # Si la question as encore des points et que la réponse entrée était juste elle retourne 1
        else:  # Si la réponse était fausse ont ajoute un point et retourne 0
            self.n += 1
            return 0

    @staticmethod
    def ask_new_question():
        """
        Cette méthode est utilisée pour demander à l'utilisateur des valeurs dans le but d'initialiser une nouvelle
        question (elle aurait pu ne pas exister, ce code se serait retrouvé dans la méthode __init__ de la classe)
        cependant j'ai décidé de créer cette méthode à part pour que je puisse si je le souhaite, initialiser une
        question plus tard sans devoir demander à l'utilisateur les paramètres -> charger des questions d'un fichier
        de donnée, en l'occurence json.
        Etant donné que cette section de code est utilisée pour accompagner l'utilisateur dans l'initialisation d'un
        objet Question, j'ai trouvé approprié de la définire comme méthode de la classe Question plutôt que simple
        fonction du programme séparée de la classe.
        """
        def ap(key):
            """
            Cette fonction sert à récupérer une valeur (dans le but de construire une nouvelle question) entrée par
            l'utilisateur, elle prend un paramètre key qui correspont à l'information que l'on va demander à
            l'utilisateur (question ou réponse). Elle force l'utilisateur à entrer une valeur autre que str().
            C'est une fonction définie dans une méthode car seulement la méthode ask_new_question() l'utilise.
            """
            u = str()
            while not u:
                u = input(key + " :\n")
            return u
        while True:
            if input("If you want to exit enter anything\n"):  # L'utilisateur entre une valeur si il veut quitter pour
                # passer aux "tests" si auqune question n'est enregistrée le programme quitte.
                return
            question = ap("Question")
            answer = ap("Answer")
            number_of_points = int()
            while number_of_points < 1:  # Cette partie de code fonctionne comme la fonction ap() mais il force
                # l'utilisateur à entrer un entier suppérieur à 0 on utilise également la fonction ap() pour forcer
                # l'utilisateur à entrer une valeur différente de str() avant de tester si c'est un entier supérieur à 0
                try:
                    number_of_points = int(ap("Number of points"))
                except ValueError:
                    pass
            if not input(f"\n\nIf you want to abort the following data enter anything :\nQuestion : {question}\nAnswer "
                         f": {answer}\nNumber of points : {number_of_points}\n"):  # On propose à l'utilisateur de se
                # relire pour confimer ou infirmer les donées pour sa question (cela est très important surtout si l'on
                # révise comme moi du vocabulaire en vue d'un test.) L'utilisateur aura encore l'occasion de supprimer
                # des questions à l'avenir si il remarque une errreur.
                return Question(question, answer, number_of_points)  # Dans le cas ou il confirme les données, celles-ci
                # sont envoyées dans la méthode d'initialisation pour créer une question qui sera retournée.

    @staticmethod
    def user_append_question():
        """
        Avant ce bout de code était tout simplement répété deux fois dans le programme, j'en ai donc fais une méthode.
        """
        que = Question.ask_new_question()  # après s'être occupé de charge de sauvegarde et d'initialisation du
        # questionnaire on propose à l'utilisateur d'ajouter des questions, (que) est égal à une nouvelle question
        while que:
            qs.append(que)  # la nouvelle questions est ajouté dans le questionnaire ici. Si l'utilisateur entre str()
            # au moment où ont lui propose de quitter dans la fonction Question.ask_new.question(), la valeur attribuée
            # à que correspond à rien ce qui ne satisfait pas la condition de la boucle et nous permet de passer à la
            # suite.
            que = Question.ask_new_question()

    @staticmethod
    def pop_qs(d):
        """
        J'ai créer cette méthode car ce code se répétait  deux fois dans le programme.
        """
        for j in d:  # ont liste tout les éléments sauvegardé et on propose à l'utilisateur d'en supprimer
            print(f"{d.index(j) + 1}. {j.q} : {j.a}    {j.n}")
        user_pop_answer = input(f"\n\nEnter the specific index to delete a specific question\n")
        while user_pop_answer:  # Tant que l'utilisateur répond quelque chose d'autre que a on essaie de retirer
            # l'élément demadé puis on lui redemande jusqu'à ce qu'il entre str()
            if user_pop_answer == "a":
                Question.user_append_question()
            try:
                d.pop(abs(int(user_pop_answer)) - 1)  # si l'utilisateur entre un index négatif on supprime
                # la valeur absolue de l'index
                if not d:
                    break
            except (ValueError, IndexError):  # Ici ont teste si l'utilisateur à entrer un entier et un index comporté
                # dans la liste (on lui présente les index avec + 1 donc on doit soustraire 1 à sa réponse). Pour gérer
                # 2 erreur j'aivais fait except ValueError or IndexError: mais ça ne marchait pas... j'ai utilisé chat
                # gpt pour savoir comment gérer 2 erreur en un except; except (erreur, erreur)
                pass
            for j in d:
                print(f"{d.index(j) + 1}. {j.q} : {j.a}    {j.n}")
            user_pop_answer = input(f"\n\nEnter the specific index to delete a specific question\n")

    @staticmethod
    def upload_data():
        """
        Cette méthode sert à utiliser des questions enregistrée sur un fichier json. Au début c'était une simple
        fonction mais puisqu'elle crée des objet de la classe Question uniquement, j'ai trouvé approprié de placer
        dans la classe Question en staticmethod, notamment car c'est le même principe que ask_new_question() ; elles
        créent des question, l'une depuis des données inscrite directement par l'utilisateur et l'autre en les
        téléchargeant d'un fichier json.
        """
        try:  # Ici on teste si un fichier "dq.json" existe (dans le répertoire ou le programme est exécuté)
            f = open("dq.json", "r")
        except FileNotFoundError:
            return list(), False  # dans le cas ou il n'existe pas la méthode retourne une liste comptenant une liste
            # vide (-> un questionnaire vide), et la valeur False la seconde valeur indique si l'utilisateur souhaite
            # utiliser les données chargées ou non, en l'occurence si aucune données n'existent ont considère que
            # l'utilisateur ne peut pas désirer utiliser des données sauvées donc on retourne False à l'index 1 de la
            # liste.
        else:
            # dans le cas ou un fichier existe (dans le même répertoire que le programme) on essaie de récupérer ses
            # données et on transforme chaque dictionnaire (dc) en objet, **dc sert à déployer un dictionnaire en
            # paramètres pour une Question() (les clés de chaques dictionnaires doivent correspondre aux paramètre
            # utilisé pour l'initialisation d'un objet).
            d = [Question(**dc) for dc in json.load(f)]
            f.close()
            if not d:  # si le fichier est vide (cas impossible pour l'instant) ont retourne comme si il n'existait pas
                return list(), False
            if input("Would you like to use previous saved data ?\n"):
                Question.pop_qs(d)
                return d, True  # dans le cas où l'utilisateur avait accepté d'utiliser des données sauvegardées ont
                # retourne une liste contenant la liste de question et la valeur True pour indiquer que l'utilisater
                # souhaite utiliser ces données
            return d, False  # dans le cas échéant ont retourne une liste contenant la liste de données sauvegardée et
            # la réponse de l'utilisateur : False


lda = Question.upload_data()  # On commence par savoir si on as des données sauvées et si l'utilisateur est intéressé
#  la fonction renvoie une liste avec index 0 la liste de question trouvée dans un fichier de sauvegare, si il n'y as
#  pas de fichier ou qu'il est vide on retourne une liste vide, l'index 1 est True si l'utilisateur veut utiliser des
#  données sauvées sinon sa valeur est False (lda c'est pour list, data, answer je ne savais pas quoi mettre d'autre)
if lda[1]:
    qs = lda[0]  # si l'utilisateur veut utiliser des données sauvées qs qui correspond à notre liste de question (qs
    # vient de questionnaire) est égal à l'élément 0 de la liste lda qui correspond à nos données chargées depuis le
    # fichier de données
    sd = list()  # la valeur sd (saved data) correspond a une liste de questions chargée d'un fichier json si celle si
    # ne veut pas être utilisée par l'utilisateur sinon, si l'utilisateur veut utiliser les données sauvegardées sd
    # correspond à list(). Cette valeur sera utile au moment de la sauvegarde des données. (si aucune données n'est
    # chargée sd correspond à une liste vide)
else:
    qs = list()  # Le questionnaire est vide si il n'y as pas de données ou si l'utilisateur ne veut pas utiliser de
    # données sauvegardées
    sd = lda[0]  # déjà expliqué plus haut
Question.user_append_question()
while qs:  # si le questionnaire est vide ont quitte le programme
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # ces espaces sont présent dans le but de masquer la réponse précédente dans la console
    e = random.randint(0, len(qs) - 1)  # ici on tire au sort un index de qs appelé e
    ar = qs[e].ask()  # ont pose la question de l'index e dans qs
    if ar == 1:  # ar (asking result) sa valeur correspond à la valeur retournée par la méthode ask(), ar peut être égal
        # à 0 ou 1 ou 2 ou 3 il varie en fonction de la réponse de l'utilisateur (voir les commentaires dans la méthode
        # ask())
        program_answer = "Correct p"
    elif ar == 0:
        program_answer = f"False the answer was {qs[e].a} p"
    elif ar == 2:
        qs.pop(e)
        program_answer = "Correct question eliminated p"
        if len(qs) == 0:
            input("\nCorrect all questions finished\n")
            break
    else:
        program_answer = "P"
    c = input(f"{program_answer}ress d to open questions directory or exit to leave\n")  # Ici on indique le message
    # resultat correct, faux, correct éliminé ou passé. Pour les cas ou c'est passé il faut un P plûtot qu'un p
    if c == "exit":  # si l'utilisateur entre exit pour quitter c'est qu'il reste forcément des questions
        if input("\nWould you like to save the data ?\n"):  # alors on lui propose de les sauvegarder
            if sd and not input("\nOverwrite the last saved data ?\n"):  # Si sd n'est pas list() cela signifie que des
                # données on étés chargée et que l'utilisateur n'a pas voulu les utiliser étant donné que je n'arrive
                # pas a ajouter des données au fichier json avec open() en mode a correctement, je dois écraser les
                # données du fichier dq.json à chaque fois que je souhaite sauvegarder. Dans le cas ou on n'écrase pas
                # les données (l'option écraser les données apparaît seulement lorsque nous n'avons pas voulu utiliser
                # ces données) on ajoute sd à qs puis on sauve qs sur le fichier (on écrase les aciennes données avec
                # les ancinnes données plus les nouvelles çela fait comme si nous n'avons rien écrasé). if sd and ...
                # fait que si sd est list() on ne pause même pas la question à l'utilisateur.
                qs.extend(sd)
            rf = open("dq.json", "w")
            json.dump([que.__dict__ for que in qs], rf)  # Sur les fichier json on sauvegarde des données structurées
            # tel que des ditionnaires sérialisés ou une liste de dictionnaire sérialisés. Question().__dict__ prend
            # toutes les valeurs propre à la question et les transforme en dictionnaire ; ce qui est sérialisé puis
            # sauvegardé sur json. Ici on prend pour chaque question dans le questionnaire sa valeur .__dict__ et on
            # forme une liste de dictionnaires. On la sérialise json.dumps() et sauvegarde sur le fichier avec
            # fichier.write() mais la fonction json.dump() fais les deux d'un seul coup.
            rf.close()
        break
    elif c == "d":  # Si il veut vérifier la liste de questions il entre d.
        Question.pop_qs(qs)
input("\n\nEnter to close the widow\n")
exit()
