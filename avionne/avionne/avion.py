import gestion_avions.db as db

def insert_avion(numav, typav, datms, nbhddrev, datrev, actif=True):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Avions (NUMAV, TYPAV, DATMS, NBHDDREV, DATREV, actif)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (numav, typav, datms, nbhddrev, datrev, actif))
        conn.commit()
        conn.close()

def retrieve_avions():
        conn =db.get_connection() 
        cursor = conn.execute("SELECT * FROM Avions")
        columns = [col[0] for col in cursor.description]  # Get column names
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    def delete_avion(numav):
    with db.get_connection() as conn:
        conn.execute("DELETE FROM Avions WHERE NUMAV = ?", (numav,))