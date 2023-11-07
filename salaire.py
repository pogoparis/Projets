# Constantes
TAUX_HORAIRE = 10
SEUIL_NORMAL = 169
SEUIL_MAJORATION_1 = 180
SEUIL_MAJORATION_2 = 999
TAUX_MAJORATION_1 = 1.5  # Majoration de 50%
TAUX_MAJORATION_2 = 1.6  # Majoration de 60%
PRIME_0_ENFANT = 0
PRIME_1_ENFANT = 20
PRIME_2_ENFANTS = 50

# Saisie
nom = input("Entrez le nom de l'employé : ")
prenom = input("Entrez le prénom de l'employé : ")
statut = input("Entrez le statut (cadre, agent de maîtrise, employé de bureau) : ")
nb_heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
nb_enfants = int(input("Entrez le nombre d'enfants : "))

# Salaire base
if nb_heures_travaillees <= SEUIL_NORMAL:
    salaire_base = nb_heures_travaillees * TAUX_HORAIRE
elif SEUIL_NORMAL < nb_heures_travaillees <= SEUIL_MAJORATION_1:
    salaire_base = nb_heures_travaillees * TAUX_HORAIRE * TAUX_MAJORATION_1
else:
    salaire_base = nb_heures_travaillees * TAUX_HORAIRE * TAUX_MAJORATION_2

# cotises
cotisations_salariales = salaire_base * 0.0349 + salaire_base * 0.0615 + salaire_base * 0.0095 + \
 salaire_base * 0.0844 + salaire_base * 0.0305 + salaire_base * 0.0381 + salaire_base * 0.0102

# Prime par rapport aux enfants
if nb_enfants == 0:
    prime = PRIME_0_ENFANT
elif nb_enfants == 1:
    prime = PRIME_1_ENFANT
elif nb_enfants == 2:
    prime = PRIME_2_ENFANTS
else:
    prime = 70 + (nb_enfants - 2) * 20

# Calcul salaire net
salaire_net = salaire_base - cotisations_salariales + prime

# Affichage Salaire
print("-" *64)
print("Bulletin de salaire de", prenom, nom)
print("Statut :", statut)
print("Nombre d'heures travaillées :", nb_heures_travaillees)
print("Salaire de base :", salaire_base)
print("Total des cotisations salariales :", cotisations_salariales)
print("Prime :", prime)
print("Salaire net à verser :", salaire_net)
