
from produit import Produit
from client import Client

from sqlite_dao import SQLiteDAO
from mysql_dao import MySQLDAO


print("===== GESTION BOUTIQUE =====")
print("1. SQLite")
print("2. MySQL")

choix = input("Choisir la base de données : ")

try:
    if choix == "1":
        dao = SQLiteDAO()
    elif choix == "2":
        dao = MySQLDAO()
    else:
        print("Choix invalide")
        exit()

    while True:

        print("\n MENU ")
        print("1. Ajouter un produit")
        print("2. Ajouter un client")
        print("3. Lister les produits")
        print("4. Lister les clients")
        print("5. Rechercher un client par email")
        print("6. Modifier le prix d'un produit")
        print("0. Quitter")

        choix = input("Votre choix : ")

        try:
            if choix == "1":
                nom = input("Nom du produit : ")
                prix = float(input("Prix : "))

                produit = Produit(None, nom, prix)
                dao.ajouter_produit(produit)

                print("Produit ajouté avec succès !")

            elif choix == "2":
                nom = input("Nom du client : ")
                email = input("Email : ")

                client = Client(None, nom, email)
                dao.ajouter_client(client)

                print("Client ajouté avec succès !")

            elif choix == "3":
                produits = dao.lister_produits()

                for p in produits:
                    print(p)

            elif choix == "4":
                clients = dao.lister_clients()

                for c in clients:
                    print(c)

            elif choix == "5":
                email = input("Email recherché : ")
                client = dao.rechercher_client(email)

                if client:
                    print(client)
                else:
                    print("Client introuvable")

            elif choix == "6":
                id = int(input("ID du produit : "))
                prix = float(input("Nouveau prix : "))

                if dao.modifier_prix(id, prix):
                    print("Prix modifié avec succès !")
                else:
                    print("Produit introuvable")

            elif choix == "0":
                break

            else:
                print("Choix invalide")

        except (ValueError, Exception) as e:
            print("Erreur :", e)

    dao.fermer()

except Exception as e:
    print("Erreur de connexion ou de base de données :", e)
