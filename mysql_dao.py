
import mysql.connector
from produit import Produit
from client import Client


class MySQLDAO:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="boutique"
        )

        self.creer_tables()

    def creer_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produit (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(100) NOT NULL,
                prix FLOAT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS client (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE NOT NULL
            )
        """)

        self.conn.commit()

    def ajouter_produit(self, produit):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO produit (nom, prix) VALUES (%s, %s)",
            (produit.nom, produit.prix)
        )
        self.conn.commit()

    def ajouter_client(self, client):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO client (nom, email) VALUES (%s, %s)",
            (client.nom, client.email)
        )
        self.conn.commit()

    def lister_produits(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produit")
        lignes = cursor.fetchall()

        return [
            Produit(id, nom, prix)
            for id, nom, prix in lignes
        ]

    def lister_clients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM client")
        lignes = cursor.fetchall()

        return [
            Client(id, nom, email)
            for id, nom, email in lignes
        ]

    def rechercher_client(self, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM client WHERE email = %s",
            (email,)
        )

        ligne = cursor.fetchone()

        if ligne:
            return Client(*ligne)

        return None

    def modifier_prix(self, id, nouveau_prix):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE produit SET prix = %s WHERE id = %s",
            (nouveau_prix, id)
        )
        self.conn.commit()

        return cursor.rowcount > 0

    def fermer(self):
        self.conn.close()
