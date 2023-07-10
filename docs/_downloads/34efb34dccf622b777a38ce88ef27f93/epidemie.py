# 1. Caractéristiques de la population ------------------------------------

# Nombre total d'individus: 1 000 000
susceptibles = ...
malades = ...
gueris = ...
morts = ...

contacts_par_jour = ...

print("A la fin du jour 0 de l'épidémie:")
print(f"\tSusceptibles: {susceptibles}")
print(f"\tMalades: {malades}")
print(f"\tGuéris: {gueris}")
print(f"\tMorts: {morts}")

# 2. Caractéristiques de la maladie ---------------------------------------

nom_maladie = ...

p_infection = ...
p_guerison = ...
p_deces = ...

# 3. Simulation -----------------------------------------------------------

# 3.1 Calcul des cas quotidiens -------------------------------------------

nb_contacts_du_jour = ...
nb_contacts_susceptibles_du_jour = ...
nb_infections = ...
nb_guerisons = ...
nb_deces = ...

# On ne peut pas avoir plus d'infections que de susceptibles à infecter, cette ligne permet de s'en assurer
nb_infections = min(nb_infections, susceptibles)

print(f"Au cours du jour 1:")
print(f"\t{nb_infections} nouvelles infections")
print(f"\t{nb_guerisons} nouvelles guérisons")
print(f"\t{nb_deces} nouveaux décès")

# 3.2 Mise à jour de la population -----------------------------------------

# Enlever les ''' quand vous avez terminé la partie 3.1 afin de dé-commenter le code ci-dessous
'''
susceptibles = 
malades = 
gueris = 
morts = 

print(f"A la fin du jour 1 de l'épidémie:")
print(f"\tSusceptibles: {susceptibles}")
print(f"\tMalades: {malades}")
print(f"\tGuéris: {gueris}")
print(f"\tMorts: {morts}")
'''