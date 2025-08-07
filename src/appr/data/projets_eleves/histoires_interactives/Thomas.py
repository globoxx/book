
def ask(question, option):
    answer = input(question + str(option))
    while answer not in option:
        print('''that wasn't an option a the time.''')
        answer = input(question + str(option))
    return answer

def ask_forest_crossing(question, option):          #j'ai fait cette fonction pour le chemin secret au debut
    answer = input(question + str(["left","right"]))
    while answer not in option:
        print('''that wasn't an option a the time.''')
        answer = input(question + str(["left","right"]))
    return answer

inventory = []
endings = []

def dream_start():
    print('you wake up with your heart beating wildly having a vague recollection of the dream you did last night.')
    print('but that is not what worries you for today is the day of your grand departure as the chosen of the kingdom.')
    print('you will follow the steps of your predecessor a hero who sealed the ancient monolith.')
    print('unfortunately he was found dead in the forest and so he was buried near the entrance of the forest with his magical sword in the CENTER road.')
    print('but that is of no consequences all that was in the past but now you must prepare')
    choice = ask("what will you bring ?", ["sword", "ration"])
    if choice == "sword":
        inventory.append("sword")
        print("you decide to leave the rations behind and so you take the sword with you.")
    elif choice == "ration":
        inventory.append("ration")
        print("you decide to leave the sword behind and so you take the rations with you.")
    forest_crossing()

def forest_crossing():
    choice = ask_forest_crossing("three path stands before you which one do you take?", ["left","right","center","back"])
    if choice == "left":
        troll_bridge()
    elif choice == "right":
        old_church()
    elif choice == "center":
        hero_grave()
    elif choice == "back":
        print("being a hero isn't what you want and you realise it in font of this dreadful forest you aren't cut out for this. ")
        print("and so you flee you run and run and run until you can't no more so you limp and when you can't do that you crawl as far as you can go.")
        print("you got an ending 'the coward'.")
        endings.append("the_coward")
        dream_start()

def hero_grave():
    print('deciding to ignore both obvious paths you walk strait in to the foliage.')
    print('and against all odds you actually find an old decrepit road forgotten by all.')
    print('At the end of the old road on a hill, under a large oak tree, lay a tomb.')
    print('Time had not been kind to the stone, but seemed not to affect the sword resting on top in the slightest.')
    choice = ask("would you like to take the sword with you?",["yes", "no"])
    if choice == "yes":
        inventory.append("magical_sword")
        print("you take the sword and look around seeing that there was nothing left you decide to go back to the crossing.")
    elif choice == "no":
        print("the sword is too suspicious for you and so you leave it behind and decide to go back the way you came.")
    forest_crossing()

def old_church():
    print("taking the path to the right after a couple hours of walk you see old ruins appear in the distance.")
    print("upon getting closer you realise that these ruins used to be a church of sorts.")
    print("it's once polished walls now covered in ivy, the beautiful roof reduced to ashes and the imposing bell now rested at the bottom of the tower half buried like a broken cup")
    def entrance_church():
        choice = ask("would you like to explore the old church?",["yes", "no"])
        def vast_room():
            print("you are in a vast room with no roof looking around you see a statue and a corpse")
            choice = ask("what do you inspect? or have you seen enough?",["statue","corpse","leave"])
            if choice == "corpse":
                inventory.append("amulet")
                print("you see an necklace on the corpse with an intricate design.")
            elif choice == "statue":
                if "amulet" in inventory:
                    inventory.append("amulet de protection")
                    print("the statues eyes glows and the necklace you just picked up started to heat up.")
                    print("you feel like an invisible veil was covering my body protecting it from physical harm.")
                elif "amulet" not in inventory:
                    print("it is a statue of a very beautiful woman.")
            elif choice == "leave":
                entrance_church()
            vast_room()
        if choice == "yes":
            vast_room()
        elif choice == "no":
            dragon_cave()
    entrance_church()

def dragon_cave():
    print("continuing to walk after the brief stop at the ruins you find yourself standing before a menacing cave")
    choice = ask("do you want to explore the cavern?",["yes", "no"])
    if choice == "yes":
        print("you walk in and before you can even understand your surroundings a wave of infernal flames washes over you.")
        if "amulet_of_protection" and "magical_sword" in inventory:
            print("but you survive the first attack at the cost of your newly acquired amulet")
            print("much to the dismay of your opponent that you are now able to see who is so surprised by your survival that they weren't able to dodge your blade.")
            print("the enchanted blade sinks in the scales without any resistance killing the dragon in one swift blow.")
            print("you walk in the treasure room were the dragon stored all his horde and take the ring of banishment that belonged to the hero.")
            inventory.append("ring of banishment")
            print("with nothing else of interest being in the horde you walk out of the cave to go face the monolith.")
            fight_or_flight()
        elif "amulet_of_protection" and "sword" in inventory:
            print("but you survive the first attack at the cost of your newly acquired amulet")
            print("much to the dismay of your opponent that you are now able to see who is so surprised by your survival that they weren't able to dodge your blade.")
            print("but with a normal blade it doesn't even scratch the surface.")
            print("you die being scorched alive")
            dream_start()
        elif "amulet_of_protection" in inventory:
            print("but you survive the first attack at the cost of your newly acquired amulet")
            print("but with nothing to protect your self you die being scorched alive")
            dream_start()
        elif "amulet_of_protection" not in inventory:
            print("you die being scorched alive")
            dream_start()
    elif choice == "no":
        fight_or_flight()

def troll_bridge():
    print("you go to the path on your left after a few kilometers you spot a bridge crossing a river.")
    print("as you are about half way trought the bridge you hear something amiss ")
    print("and as you try and identify the noise a huge hand grabs the edge of the bridge.")
    if "ration" in inventory:
        print("thinking fast you pull out your weeks ration and trow them as far as you can at the other side of the bride.")
        print("attracted by the smell the troll leaves you alone and goes chasing your rations.")
        print("you pass un harmed to the other side.")
        mystveil_castle()
    elif "magical_sword" in inventory:
        print("you behead the troll in one swift motion not letting him the time to regenerate.")
        print("you pass un harmed to the other side.")
        mystveil_castle()
    else:
        print("you throw every thing you have on the troll but even if you do damage it regenerate too fast.")
        print("you get mauled to death.")
        dream_start()

def mystveil_castle():
    print("after almost being mauled by a troll you succesfully make it to a bastion with immovable walls.")
    def entrance_castle():
        choice = ask("would you like to explore the old fort?",["yes", "no"])
        def hall_room():
            print("you are in a massive hall with a dome like celling looking around you see a throne and a vault")
            choice = ask("which room do you explore? or have you seen enough?",["vault","throne","leave"])
            if choice == "throne":
                print("you find a a crown on the corpse the crown seems to take impossible shapes you get a headache just by looking.")
                print("but you seem to be pulled by it and you don't know why.")
                choice = ask ("do you wear it?",["yes","no"])
                if choice == "no":
                    hall_room()
                elif choice == "yes":
                    print("the instant you touch the crown your mind is flodded by images and sounds no humain should have ever witnessed.")
                    print("and soon after your mind collapses on it's self making you a mad.")
                    print("but the crown is fair and it takes as much as it gives so you gain power beyond anything else.")
                    print("you got an ending 'the mad king'.")
                    endings.append("the_mad_king")
                    dream_start()
            elif choice == "vault":
                print("you find a ring on a pedestal and take it you now have the ring of misty escape.")
                inventory.append("ring_of_misty_escape")
            elif choice == "leave":
                entrance_castle()
            hall_room()
        if choice == "yes":
            hall_room()
        elif choice == "no":
            fight_or_flight()
    entrance_castle()

def fight_or_flight():
    print("you approach the end of your journey.")
    choice = ask("are you going to fight the monolith of the stars now or are you going back to explore the other path.",["fight","explore"])
    if choice == "explore":
        forest_crossing()
    elif choice == "fight":
        monolith_of_the_stars()

def monolith_of_the_stars():
    print("as you approach the monolith the air in the forest start to get more and more foul you can feel it's corruption scratching a the edge of you mind.")
    print("most animals see are dead and those are the lucky ones because the one still alive are piles of flesh without logic or purpose.")
    print("no amount of training or protection could prepare you for seeing what you saw that day")
    print("the monolith stood before you.")
    print("tough no eyes were looking at you you could feel that you were not left unseen.")
    print("tough it had no mouths you could hear it whisper in your hears")
    print("tough it had no shape you could feel it under your skin")
    if "ring_of_banishment" in inventory:
        print("and so you willed your hands to move and the ring glew but it wasn't intantenous.")
        print("and so he willed you out of exictence and you died pitifuly,mad and alone in Nowhere.")
        print("but you banished the monolith so you became a hero to be forever remember until you are forgotten like the last.")
        endings.append("the_hero")
        dream_start()
    elif "ring_of_banishment" not in inventory:
        print("and then you no longer exicted.")
        endings.append("the_fallen")
        dream_start()
    elif "ring_of_banishment" and "ring_of_misty_escape" in inventory:
        print("and so you willed your hands to move and the ring glew but it wasn't intantenous.")
        print("so the monolith tried to will you out of exitence but just before it did you escaped his grasp with your ring of escape.")
        print("and than it was gone but just before it did you could FEEL it had a smile on all the mouths he didn't have and you KNEW it will be back one day but not today.")
        print("and you knew too much all the things you've seen and herd and felt and smelt and tasted and percieved and KNEW.")
        print("so your mind imploded on it's self to keep you alive.")
        endings.append("the_madman")
        dream_start()

if "the_madman" and "the_coward" and "the_hero" and "the_fallen" and "the_mad_king" in endings:
    print("as you wake up you have a strange sense of deja vue but you don't mind it what could possibly happen to you.")
    print("you are just a farmer after all but no matter today is a special day the kingdom is going to announce who their chosen will be!")
    print("i wonder who it'll be ?")
    print("congratulation you've gotten all the endings now you have the true ending:'the dreamer'.")


dream_start()

