def afficher_menu():
    print("\n=============================")
    print("      CALCULATRICE SIMPLE    ")
    print("=============================")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    print("=============================")

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro impossible !"
    return a / b

def saisir_nombres():
    while True:
        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))
            return a, b
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")

def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "5":
            print("Au revoir !")
            break
        elif choix in ["1", "2", "3", "4"]:
            a, b = saisir_nombres()

            if choix == "1":
                resultat = addition(a, b)
                operation = "+"
            elif choix == "2":
                resultat = soustraction(a, b)
                operation = "-"
            elif choix == "3":
                resultat = multiplication(a, b)
                operation = "*"
            elif choix == "4":
                resultat = division(a, b)
                operation = "/"

            print(f"\nRésultat : {a} {operation} {b} = {resultat}")
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()