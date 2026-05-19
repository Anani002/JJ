# Liste pour stocker les tâches
taches = []

def afficher_menu():
    print("\n==============================")
    print("         TODO LIST           ")
    print("==============================")
    print("1. Ajouter une tache")
    print("2. Afficher toutes les taches")
    print("3. Marquer une tache comme faite")
    print("4. Supprimer une tache")
    print("5. Quitter")
    print("==============================")

def ajouter_tache():
    print("\n-- Ajouter une tache --")
    titre = input("Titre de la tache : ")
    taches.append({"titre": titre, "faite": False})
    print("Tache ajoutee !")

def afficher_taches():
    print("\n-- Liste des taches --")
    if not taches:
        print("Aucune tache.")
    else:
        for i, t in enumerate(taches, 1):
            statut = "[X]" if t["faite"] else "[ ]"
            print(f"{i}. {statut} {t['titre']}")

def marquer_faite():
    afficher_taches()
    if not taches:
        return
    try:
        num = int(input("Numero de la tache : "))
        if 1 <= num <= len(taches):
            taches[num - 1]["faite"] = True
            print("Tache marquee comme faite !")
        else:
            print("Numero invalide.")
    except ValueError:
        print("Entrez un nombre valide.")

def supprimer_tache():
    afficher_taches()
    if not taches:
        return
    try:
        num = int(input("Numero de la tache a supprimer : "))
        if 1 <= num <= len(taches):
            taches.pop(num - 1)
            print("Tache supprimee !")
        else:
            print("Numero invalide.")
    except ValueError:
        print("Entrez un nombre valide.")

# Programme principal
while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        marquer_faite()
    elif choix == "4":
        supprimer_tache()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide.")