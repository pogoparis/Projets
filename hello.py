print("Hello World !") # Afficher un message

msg = "Roll a Dice"
print(msg)


#valeur = input("quel est ton nom ?")
#print("Ton nom est", valeur)  

import keyword
print(keyword.kwlist)

# Déclaration de variables :
a, b = 12, 34.78
# Affichage des variables 'a' et 'b' :
print("a =", a, "et b =", b)

def additionner(val1, val2): # Attention à l'indentation
    print("Addition :", val1, "+", val2) # Affichage des arguments
    resultat = val1 + val2 # variable locale
    return resultat # Retourne le résultat du calcul
# Fin du bloc 'additionner'

somme = additionner(a, b) # Appel de la fonction avec val1=a et val2=b
print("Résultat = " , somme) # Affichage de la variable 'somme'
""" resultat, val1 et val2 ne sont pas disponibles en dehors du bloc de la méthode
print("Résultat =", resultat) ne fonctionnera pas """

# Concaténation (explicite) :
print("Hello " + "World !")
   # print("Typage fort = " + 321) # Pas de conversion implicite str/int|float  Avec une virgule ça fonctionne grace à Print
print("Numérique = " + str(654)) # Conversion explicite 
# Concaténation implicite via print :
print("Hello", "the", "World", \
"from", "Python", 3, "!")


un_int = int(input("entrez un entier :"))
un_float = float(input("entrer un decimal :"))
un_str = "Résultat = " + str(un_int + un_float)
print(un_str)