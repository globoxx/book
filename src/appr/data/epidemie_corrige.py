import matplotlib.pyplot as plt

# 1. Caractéristiques de la population ------------------------------------

# Nombre total d'individus: 1 000 000
susceptibles = 999999
malades = 1
gueris = 0
morts = 0

contacts_par_jour = 10

print("A la fin du jour 0 de l'épidémie:")
print(f"\tSusceptibles: {susceptibles}")
print(f"\tMalades: {malades}")
print(f"\tGuéris: {gueris}")
print(f"\tMorts: {morts}")

# 2. Caractéristiques de la maladie ---------------------------------------

nom_maladie = 'Corona'

p_infection = 0.1
p_guerison = 0.2
p_deces = 0.01

# 3. Simulation -----------------------------------------------------------

courbe_infection = []
courbe_susceptibles = []
courbe_malades = []
courbe_gueris = []
courbe_morts = []
for jour in range(1, 51):
    # 3.1 Calcul des cas quotidiens -------------------------------------------

    nb_contacts_du_jour = malades*contacts_par_jour
    nb_contacts_susceptibles_du_jour = nb_contacts_du_jour*susceptibles/(susceptibles+malades+gueris)
    nb_infections = nb_contacts_susceptibles_du_jour*p_infection
    nb_guerisons = malades*p_guerison
    nb_deces = malades*p_deces
    
    # On ne peut pas avoir plus d'infections que de susceptibles à infecter, cette ligne permet de s'en assurer
    nb_infections = min(nb_infections, susceptibles)

    print(f"Au cours du jour {jour}:")
    print(f"\t{nb_infections} nouvelles infections")
    print(f"\t{nb_guerisons} nouvelles guérisons")
    print(f"\t{nb_deces} nouveaux décès")

    # 3.2 Mise à jour de la population -----------------------------------------

    susceptibles = susceptibles - nb_infections
    malades = malades + nb_infections - nb_guerisons - nb_deces
    gueris = gueris + nb_guerisons
    morts = morts + nb_deces

    print(f"A la fin du jour {jour} de l'épidémie de {nom_maladie}:")
    print(f"\tSusceptibles: {susceptibles}")
    print(f"\tMalades: {malades}")
    print(f"\tGuéris: {gueris}")
    print(f"\tMorts: {morts}")

    # 4 Remplissage des listes pour les graphiques --------------------------------

    courbe_infection.append(nb_infections)
    
    courbe_susceptibles.append(susceptibles)
    courbe_malades.append(malades)
    courbe_gueris.append(gueris)
    courbe_morts.append(morts)
    
plt.title(f'Epidémie de {nom_maladie}')
plt.plot(courbe_infection,'-')
plt.xlabel('jours')
plt.ylabel("nombre d'infections")
plt.show()

plt.title(f'Epidémie de {nom_maladie}')
plt.plot(courbe_susceptibles,'-', c='blue')
plt.plot(courbe_malades,'-', c='red')
plt.plot(courbe_gueris,'-', c='green')
plt.plot(courbe_morts,'-', c='black')
plt.xlabel('jours')
plt.ylabel("population")
plt.legend(['susceptibles', 'malades', 'guéris', 'morts'])
plt.show()