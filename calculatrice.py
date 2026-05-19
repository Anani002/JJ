import os

# Nom du fichier de sauvegarde
FICHIER_HISTORIQUE = "historique.txt"

# ==============================
# FONCTIONS DE FICHIER
# ==============================

def sauvegarder(expression, resultat):
    """Sauvegarde un calcul dans le fichier historique."""
    with open(FICHIER_HISTORIQUE, "a") as f:
        f.write(f"{expression} = {resultat}\n")

def lire_historique():
    """Lit et affiche le contenu du fichier historique."""
    if not os.path.exists(FICHIER_HISTORIQUE):
        print("Aucun historique trouve.")
        return
    with open(FICHIER_HISTORIQUE, "r") as f:
        lignes = f.readlines()
    if not lignes:
        print("L'historique est vide.")
    else:
        print(f"\n-- Historique ({len(lignes)} calcul(s)) --")
        for i, ligne in enumerate(lignes, 1):
            print(f"  {i}. {ligne.strip()}")

def effacer_historique():
    """Efface le contenu du fichier historique."""
    with open(FICHIER_HISTORIQUE, "w") as f:
        f.write("")
    print("Historique efface avec succes !")

# ==============================
# FONCTIONS DE CALCUL
# ==============================

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return None
    return a / b

# ==============================
# FONCTIONS D'AFFICHAGE
# ==============================

def afficher_menu():
    print("\n==============================")
    print("      CALCULATRICE v2.0      ")
    print("==============================")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Voir l'historique")
    print("6. Effacer l'historique")
    print("7. Quitter")
    print("==============================")

# ==============================
# FONCTIONS DE SAISIE
# ==============================

def saisir_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Entree invalide. Veuillez entrer un nombre.")

def saisir_choix(options):
    while True:
        choix = input("Votre choix : ")
        if choix in options:
            return choix
        print(f"Choix invalide. Entrez un chiffre parmi : {', '.join(options)}")

# ==============================
# PROGRAMME PRINCIPAL
# ==============================

def main():
    print("Bienvenue dans la Calculatrice v2.0 !")
    print(f"Les calculs seront sauvegardes dans '{FICHIER_HISTORIQUE}'")

    while True:
        afficher_menu()
        choix = saisir_choix(["1", "2", "3", "4", "5", "6", "7"])

        if choix in ["1", "2", "3", "4"]:
            a = saisir_nombre("Premier nombre  : ")
            b = saisir_nombre("Deuxieme nombre : ")

            if choix == "1":
                resultat = addition(a, b)
                expr = f"{a} + {b}"
            elif choix == "2":
                resultat = soustraction(a, b)
                expr = f"{a} - {b}"
            elif choix == "3":
                resultat = multiplication(a, b)
                expr = f"{a} x {b}"
            elif choix == "4":
                resultat = division(a, b)
                expr = f"{a} / {b}"
                if resultat is None:
                    print("Erreur : division par zero impossible !")
                    continue

            resultat = round(resultat, 4)
            print(f"\nResultat : {expr} = {resultat}")
            sauvegarder(expr, resultat)
            print("Calcul sauvegarde dans l'historique.")

        elif choix == "5":
            lire_historique()

        elif choix == "6":
            effacer_historique()

        elif choix == "7":
            print("Au revoir !")
            break

main()