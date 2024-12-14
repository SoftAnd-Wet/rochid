from gestion_avions.db import get_connection

def insert_jour_vol(idjour, numvol, jvol):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO JoursVols (IDJOUR, NUMVOL, JVOL) 
            VALUES (?, ?)""",
            (idjour, numvol, jvol)
        )

def retrieve_jours_vols():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM JoursVols").fetchall()

def delete_jour_vol(idjour):
    with get_connection() as conn:
        conn.execute("DELETE FROM JoursVols WHERE IDJOUR = ?", (idjour,))

