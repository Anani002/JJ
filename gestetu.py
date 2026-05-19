# Liste pour stocker les étudiants
etudiants = []

def afficher_menu():
    print("\n==============================")
    print("    GESTION DES ETUDIANTS    ")
    print("==============================")
    print("1. Ajouter un etudiant")
    print("2. Afficher tous les etudiants")
    print("3. Rechercher un etudiant")
    print("4. Supprimer un etudiant")
    print("5. Quitter")
    print("==============================")

def ajouter_etudiant():
    print("\n-- Ajouter un etudiant --")
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    matricule = input("Matricule : ")
    note = float(input("Note (sur 20) : "))

    etudiant = {
        "nom": nom,
        "prenom": prenom,
        "matricule": matricule,
        "note": note
    }

    etudiants.append(etudiant)
    print(f"Etudiant {prenom} {nom} ajoute avec succes !")

def afficher_etudiants():
    print("\n-- Liste des etudiants --")
    if len(etudiants) == 0:
        print("Aucun etudiant enregistre.")
    else:
        for i, e in enumerate(etudiants, 1):
            statut = "Admis" if e["note"] >= 10 else "Recale"
            print(f"{i}. {e['prenom']} {e['nom']} | Matricule: {e['matricule']} | Note: {e['note']}/20 | {statut}")

def rechercher_etudiant():
    print("\n-- Rechercher un etudiant --")
    nom_recherche = input("Entrez le nom ou le matricule : ")
    trouve = False

    for e in etudiants:
        if nom_recherche.lower() in e["nom"].lower() or nom_recherche in e["matricule"]:
            statut = "Admis" if e["note"] >= 10 else "Recale"
            print(f"Trouve : {e['prenom']} {e['nom']} | Matricule: {e['matricule']} | Note: {e['note']}/20 | {statut}")
            trouve = True

    if not trouve:
        print("Aucun etudiant trouve.")

def supprimer_etudiant():
    print("\n-- Supprimer un etudiant --")
    matricule = input("Entrez le matricule de l'etudiant a supprimer : ")

    for e in etudiants:
        if e["matricule"] == matricule:
            etudiants.remove(e)
            print("Etudiant supprime avec succes !")
            return

    print("Aucun etudiant avec ce matricule.")

# Programme principal
while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_etudiant()
    elif choix == "2":
        afficher_etudiants()
    elif choix == "3":
        rechercher_etudiant()
    elif choix == "4":
        supprimer_etudiant()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez reessayer.")