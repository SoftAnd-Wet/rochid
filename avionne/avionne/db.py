import logging
import sqlite3
import os
import sys

def get_db_path():
    """Returns the path to the database file, adjusted for executable packaging."""
    if getattr(sys, 'frozen', False):  # If the program is running as a packaged .exe
        # PyInstaller creates a temporary folder to extract files and then run them
        app_path = sys._MEIPASS
    else:
        app_path = os.path.dirname(os.path.abspath(_file_))
    return os.path.join(app_path, "gestion_avions.db")

DB_PATH = get_db_path()

def get_connection():
    """Establish a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON;")
        print(f"Connected to database at {DB_PATH}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def initialize_db():
    """Initialize the database schema."""
    schema = """
   CREATE TABLE IF NOT EXISTS AVIONS (
    NUMAV TEXT PRIMARY KEY,
    TYPAV TEXT NOT NULL,
    DATMS DATE NOT NULL,
    NBHDDREV INTEGER NOT NULL,
    DATREV DATE NOT NULL,
    ACTIF BOOLEAN
);

CREATE TABLE IF NOT EXISTS ENVOL (
    NUMAV TEXT NOT NULL,
    NUMVOL TEXT NOT NULL,
    FOREIGN KEY(NUMVOL) REFERENCES VOLS(NUMVOL) ON DELETE CASCADE,
    FOREIGN KEY(NUMAV) REFERENCES AVIONS(NUMAV) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS REVISIONS (
    IDREV INTEGER PRIMARY KEY,
    DATREV DATE NOT NULL,
    NBHREV INTEGER NOT NULL,
    TEXTE TEXT
);

CREATE TABLE IF NOT EXISTS REVISER (
    NUMAV TEXT NOT NULL,
    IDREV INTEGER NOT NULL,
    FOREIGN KEY(NUMAV) REFERENCES AVIONS(NUMAV) ON DELETE CASCADE,
    FOREIGN KEY(IDREV) REFERENCES REVISIONS(IDREV) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS EMPLOYE (
    NUMEMP INTEGER PRIMARY KEY,
    NOM TEXT NOT NULL,
    PRENOM TEXT NOT NULL,
    TEL TEXT,
    ADRESSE TEXT,
    SAL REAL NOT NULL,
    FONCTION TEXT NOT NULL,
    DATEMB DATE NOT NULL,
    NBMHV INTEGER DEFAULT 0,
    NBTHV INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS EMPLOYE_AVIONS (
    NUMAV TEXT NOT NULL,
    NUMEMP INTEGER NOT NULL,
    FOREIGN KEY(NUMAV) REFERENCES AVIONS(NUMAV) ON DELETE CASCADE,
    FOREIGN KEY(NUMEMP) REFERENCES EMPLOYE(NUMEMP) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS VOLS (
    NUMVOL TEXT PRIMARY KEY,
    IDJOUR INTEGER,
    VILDEP TEXT NOT NULL,
    VILARR TEXT NOT NULL,
    HDEP TIME NOT NULL,
    DURVOL TIME NOT NULL,
    FOREIGN KEY(IDJOUR) REFERENCES SCHEDULE(IDJOUR) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS SCHEDULE (
    IDJOUR INTEGER PRIMARY KEY,
    JVOL TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ESCALES (
    IDESC INTEGER PRIMARY KEY,
    VILESC TEXT NOT NULL,
    HARRESC TIME NOT NULL,
    DURESC TIME NOT NULL,
    NOORD INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS STOP (
    NUMVOL TEXT NOT NULL,
    IDESC INTEGER NOT NULL,
    FOREIGN KEY(NUMVOL) REFERENCES VOLS(NUMVOL) ON DELETE CASCADE,
    FOREIGN KEY(IDESC) REFERENCES ESCALES(IDESC) ON DELETE CASCADE
);

    """
    with get_connection() as conn:
        conn.executescript(schema)
    print("Database initialized successfully!")