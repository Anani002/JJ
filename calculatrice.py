import os

def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_banniere():
    print("╔══════════════════════════════════╗")
    print("║       CALCULATRICE AVANCÉE       ║")
    print("║         Version 2.0              ║")
    print("╚══════════════════════════════════╝")

def afficher_menu_principal():
    effacer_ecran()
    afficher_banniere()
    print("\n  CATEGORIES D'OPERATIONS\n")
    print("  1.  Operations de base")
    print("  2.  Operations avancees")
    print("  3.  Historique des calculs")
    print("  4.  Quitter")
    print("\n" + "-" * 36)

def afficher_menu_base():
    effacer_ecran()
    afficher_banniere()
    print("\n  OPERATIONS DE BASE\n")
    print("  1. Addition        (+)")
    print("  2. Soustraction    (-)")
    print("  3. Multiplication  (x)")
    print("  4. Division        (/)")
    print("  5. Modulo          (%)")
    print("  6. Retour au menu principal")
    print("\n" + "-" * 36)

def afficher_menu_avance():
    effacer_ecran()
    afficher_banniere()
    print("\n  OPERATIONS AVANCEES\n")
    print("  1. Puissance       (x^n)")
    print("  2. Racine carree   (sqrt)")
    print("  3. Valeur absolue  (|x|)")
    print("  4. Retour au menu principal")
    print("\n" + "-" * 36)

def saisir_nombre(message, accepter_zero=True):
    while True:
        try:
            valeur = float(input(message))
            if not accepter_zero and valeur == 0:
                print("  Ce nombre ne peut pas etre zero.")
                continue
            return valeur
        except ValueError:
            print("  Entree invalide. Veuillez entrer un nombre.")

def saisir_choix(message, options_valides):
    while True:
        choix = input(message).strip()
        if choix in options_valides:
            return choix
        print(f"  Choix invalide. Options : {', '.join(options_valides)}")

def afficher_resultat(expression, resultat):
    print("\n" + "-" * 36)
    print(f"  Resultat : {expression} = {resultat}")
    print("-" * 36)

def operations_base(historique):
    while True:
        afficher_menu_base()
        choix = saisir_choix("  Votre choix : ", ["1", "2", "3", "4", "5", "6"])

        if choix == "6":
            break

        a = saisir_nombre("  Premier nombre  : ")
        if choix == "4":
            b = saisir_nombre("  Deuxieme nombre : ", accepter_zero=False)
        else:
            b = saisir_nombre("  Deuxieme nombre : ")

        if choix == "1":
            res = a + b
            expr = f"{a} + {b}"
        elif choix == "2":
            res = a - b
            expr = f"{a} - {b}"
        elif choix == "3":
            res = a * b
            expr = f"{a} x {b}"
        elif choix == "4":
            res = a / b
            expr = f"{a} / {b}"
        elif choix == "5":
            res = a % b
            expr = f"{a} % {b}"

        afficher_resultat(expr, round(res, 6))
        historique.append(f"{expr} = {round(res, 6)}")
        input("\n  Appuyez sur Entree pour continuer...")

def operations_avancees(historique):
    import math
    while True:
        afficher_menu_avance()
        choix = saisir_choix("  Votre choix : ", ["1", "2", "3", "4"])

        if choix == "4":
            break

        if choix == "1":
            a = saisir_nombre("  Base     : ")
            b = saisir_nombre("  Exposant : ")
            res = a ** b
            expr = f"{a} ^ {b}"
        elif choix == "2":
            a = saisir_nombre("  Nombre (>= 0) : ")
            if a < 0:
                print("  Impossible : racine d'un nombre negatif.")
                input("\n  Appuyez sur Entree pour continuer...")
                continue
            res = math.sqrt(a)
            expr = f"sqrt({a})"
        elif choix == "3":
            a = saisir_nombre("  Nombre : ")
            res = abs(a)
            expr = f"|{a}|"

        afficher_resultat(expr, round(res, 6))
        historique.append(f"{expr} = {round(res, 6)}")
        input("\n  Appuyez sur Entree pour continuer...")

def afficher_historique(historique):
    effacer_ecran()
    afficher_banniere()
    print("\n  HISTORIQUE DES CALCULS\n")
    if not historique:
        print("  Aucun calcul effectue pour l'instant.")
    else:
        for i, entree in enumerate(historique, 1):
            print(f"  {i}. {entree}")
    print("\n" + "-" * 36)
    input("\n  Appuyez sur Entree pour continuer...")

def main():
    historique = []
    while True:
        afficher_menu_principal()
        choix = saisir_choix("  Votre choix : ", ["1", "2", "3", "4"])

        if choix == "1":
            operations_base(historique)
        elif choix == "2":
            operations_avancees(historique)
        elif choix == "3":
            afficher_historique(historique)
        elif choix == "4":
            effacer_ecran()
            print("\n  Merci d'avoir utilise la Calculatrice Avancee. Au revoir !\n")
            break

if __name__ == "__main__":
    main()