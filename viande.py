"""
type_viande = input("Veuillez entrer le type de viande (boeuf, porc ou canard): ").lower()
poids = int(input("Veuillez entrer le poids de la viande en grammes: "))
mode_cuisson = input("Entrez le mode de cuisson (Bleu, À Point, Bien Cuit, etc.): ").lower()

if type_viande == "boeuf":
    if poids == 500:
        if mode_cuisson == "bleu":
            temps_cuisson = 10
        elif mode_cuisson == "à point":
            temps_cuisson = 17
        elif mode_cuisson == "bien cuit":
            temps_cuisson = 25
        else:
            print("Mode de cuisson non reconnu.")
            temps_cuisson = None
    else:
        print("Poids non pris en charge pour le boeuf.")
        temps_cuisson = None
elif type_viande == "porc":
    if poids == 400:
        if mode_cuisson == "bleu":
            temps_cuisson = 15
        elif mode_cuisson == "à point":
            temps_cuisson = 25
        elif mode_cuisson == "bien cuit":
            temps_cuisson = 40
        else:
            print("Mode de cuisson non reconnu.")
            temps_cuisson = None
    else:
        print("Poids non pris en charge pour le porc.")
        temps_cuisson = None
elif type_viande == "canard":
    if poids == 450:
        if mode_cuisson == "rosé":
            temps_cuisson = 20
        elif mode_cuisson == "à point":
            temps_cuisson = 25
        elif mode_cuisson == "bien cuit":
            temps_cuisson = 30
        else:
            print("Mode de cuisson non reconnu.")
            temps_cuisson = None
    else:
        print("Poids non pris en charge pour le canard.")
        temps_cuisson = None
else:
    print("Type de viande non reconnu.")
    temps_cuisson = None

if temps_cuisson is not None:
    print(f"Le temps de cuisson de {type_viande} de {poids}g pour une cuisson {mode_cuisson} est de {temps_cuisson} minutes.")
   """     
   
   
temps_cuisson = {
    "boeuf": {
        500: {"bleu": 10, "à point": 17, "bien cuit": 25},
    },
    "porc": {
        400: {"bleu": 15, "à point": 25, "bien cuit": 40},
    },
    "canard": {
        450: {"rosé": 20, "à point": 25, "bien cuit": 30},
    }
}

type_viande = input("Veuillez entrer le type de viande (boeuf, porc ou canard): ").lower()
poids_viande = int(input("Veuillez entrer le poids de la viande en grammes: "))
mode_cuisson = input("Entrez le mode de cuisson (Bleu, À Point, Bien Cuit, etc.): ").lower()

if type_viande in temps_cuisson:
    if poids_viande in temps_cuisson[type_viande]:
        if mode_cuisson in temps_cuisson[type_viande][poids_viande]:
            temps = temps_cuisson[type_viande][poids_viande][mode_cuisson]
            print(f"Le temps de cuisson de {type_viande} de {poids_viande}g pour une cuisson {mode_cuisson} est de {temps} minutes.")
        else:
            print("Mode de cuisson non reconnu.")
    else:
        print(f"Poids non pris en charge pour le {type_viande}.")
else:
    print("Type de viande non reconnu.")
