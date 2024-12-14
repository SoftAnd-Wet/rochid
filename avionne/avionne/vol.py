from gestion_avions.db import get_connection

def insert_catalogue_vol(numvol, vildep, vilarr, hdep, durvol):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO CatalogueVols (NUMVOL, VILDEP, VILARR, HDEP, DURVOL) 
            VALUES (?, ?, ?, ?, ?)""",
            (numvol, vildep, vilarr, hdep, durvol)
        )

def retrieve_catalogue_vols():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM CatalogueVols").fetchall()

def delete_catalogue_vol(numvol):
    with get_connection() as conn:
        conn.execute("DELETE FROM CatalogueVols WHERE NUMVOL = ?", (numvol,))
