prix_cafe = 0.60
pieces_acceptees = [2, 1, 0.50, 0.20, 0.10, 0.05]
credit = 0
pieces_rendues = {2: 0, 1: 0, 0.50: 0, 0.20: 0, 0.10: 0, 0.05: 0}

while credit < prix_cafe:
    piece = float(input("Entrez la valeur de la pièce : "))

    if piece in pieces_acceptees:
        credit += piece
        print(f"Crédit : {credit:.2f}€ / {prix_cafe:.2f}€")
    else:
        print("Pièce non acceptée")

if credit > prix_cafe:
    monnaie = round(credit - prix_cafe, 2)
    print(f"Voici votre café et votre monnaie ({monnaie:.2f}€) :")

    for piece in pieces_acceptees:
        while monnaie >= piece and pieces_rendues[piece] < 2:
            monnaie = round(monnaie - piece, 2) 
            pieces_rendues[piece] += 1
            print(f"1 pièce(s) de {piece:.2f}€")
