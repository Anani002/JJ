def calculatrice():
    print("--- MA CALCULATRICE ---")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Quitter")
    
    choix = input("Choisissez une option (1-3) : ")
    
    if choix in ['1', '2']:
        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
            
            if choix == '1':
                print(f"Résultat : {num1} + {num2} = {num1 + num2}")
            elif choix == '2':
                print(f"Résultat : {num1} - {num2} = {num1 - num2}")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            
    elif choix == '3':
        print("Au revoir !")
    else:
        print("Option invalide.")

if __name__ == "__main__":
    calculatrice()
