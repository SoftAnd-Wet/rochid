from gestion_avions.db import get_connection

def insert_employe(numemp, nom, prenom, tel, adresse, sal, fonction, datemb, nbmhv=0, nbthv=0):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO Employes (NUMEMP, NOM, PRENOM, TEL, ADRESSE, SAL, FONCTION, DATEMB, NBMHV, NBTHV) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (numemp, nom, prenom, tel, adresse, sal, fonction, datemb, nbmhv, nbthv)
        )

def retrieve_employes():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM Employes").fetchall()

def delete_employe(numemp):
    with get_connection() as conn:
        conn.execute("DELETE FROM Employes WHERE NUMEMP = ?", (numemp,))


