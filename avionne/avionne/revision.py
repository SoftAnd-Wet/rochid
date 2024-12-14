from gestion_avions.db import get_connection

def insert_revision(idrev, numav, datrev, nbhrev, texte):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO Revisions (IDREV, NUMAV, DATREV, NBHREV, TEXTE) 
            VALUES (?, ?, ?, ?)""",
            (idrev, numav, datrev, nbhrev, texte)
        )

def retrieve_revisions():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM Revisions").fetchall()

def delete_revision(idrev):
    with get_connection() as conn:
        conn.execute("DELETE FROM Revisions WHERE IDREV = ?", (idrev,))

