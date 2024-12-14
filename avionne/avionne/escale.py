from gestion_avions.db import get_connection

def insert_escale(idesc, numvol, vilesc, harresc, duresc, noord):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO Escales (IDESC, NUMVOL, VILESC, HARRESC, DURESC, NOORD) 
            VALUES (?, ?, ?, ?, ?)""",
            (idesc, numvol, vilesc, harresc, duresc, noord)
        )

def retrieve_escales():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM Escales").fetchall()

def delete_escale(idesc):
    with get_connection() as conn:
        conn.execute("DELETE FROM Escales WHERE IDESC = ?", (idesc,))
