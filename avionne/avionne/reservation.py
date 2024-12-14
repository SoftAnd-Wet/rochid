from gestion_avions.db import get_connection

def insert_reservation(idres ,numvol, numemp, numav, datevol):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO Reservations (IDRES, NUMVOL, NUMEMP, NUMAV, DATEVOL) 
            VALUES (?, ?, ?, ?)""",
            (idres ,numvol, numemp, numav, datevol)
        )

def retrieve_reservations():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM Reservations").fetchall()

def delete_reservation(idres):
    with get_connection() as conn:
        conn.execute("DELETE FROM Reservations WHERE IDRES = ?", (idres,))

