import random

# Définition des employés
employes = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Initialisation des horaires de travail
horaires = {employe: [0, 0, 0, 0, 0] for employe in employes}

# Boucle de planification
for jour in range(5):
    # Sélection de deux employés pour le shift du matin
    matin = random.sample(employes, 2)
    for employe in matin:
        horaires[employe][jour] = 1
    
    # Sélection de trois employés pour le shift de l'après-midi
    apres_midi = list(set(employes) - set(matin))
    apres_midi = random.sample(apres_midi, 3)
    for employe in apres_midi:
        horaires[employe][jour] = 2

# Vérification des horaires de travail
for employe in employes:
    if horaires[employe].count(1) != 2 or horaires[employe].count(2) != 3:
        print(f"L'employé {employe} n'a pas les bonnes heures de travail.")
