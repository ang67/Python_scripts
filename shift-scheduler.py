import random

# Les noms des employés
employees = ["Alice", "Bob", "Charlie", "David", "Emily"]

# Les jours de la semaine
days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

# Les plages horaires
shifts = ["Matin", "Matin", "Après-midi", "Après-midi", "Après-midi"]

# Initialise le calendrier à vide
schedule = {day: {shift: None for shift in shifts} for day in days}

# Assigne les plages horaires pour chaque jour de la semaine
for day in days:
    # Copie la liste des employés pour la journée
    day_employees = employees.copy()
    # Assigne les plages horaires pour la journée
    for shift in shifts:
        # Choisi un employé aléatoirement pour le shift
        employee = random.choice(day_employees)
        # Retire l'employé de la liste pour le shift suivant
        day_employees.remove(employee)
        # Assigne l'employé pour la plage horaire
        schedule[day][shift] = employee

# Affiche le calendrier
for day in days:
    print(day)
    print("Matin:", schedule[day]["Matin"], "Après-midi:", schedule[day]["Après-midi"])
    print()

