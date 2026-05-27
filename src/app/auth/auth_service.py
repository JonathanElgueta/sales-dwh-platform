import sqlite3

import hashlib

from pathlib import Path


# ==================================================
# DATABASE PATH
# ==================================================

DB_PATH = Path(

    "data/auth/users.db"

)


# ==================================================
# CREATE AUTH DATABASE
# ==================================================

def create_auth_database():

    DB_PATH.parent.mkdir(

        parents=True,
        exist_ok=True

    )

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(

        """
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password_hash TEXT NOT NULL,

            role TEXT NOT NULL

        )
        """

    )

    conn.commit()

    conn.close()


# ==================================================
# HASH PASSWORD
# ==================================================

def hash_password(password):

    return hashlib.sha256(

        password.encode()

    ).hexdigest()


# ==================================================
# CREATE USER
# ==================================================

def create_user(

    username,
    password,
    role="admin"

):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    password_hash = hash_password(password)

    cursor.execute(

        """
        INSERT INTO users (

            username,
            password_hash,
            role

        )

        VALUES (?, ?, ?)
        """,

        (

            username,
            password_hash,
            role

        )

    )

    conn.commit()

    conn.close()


# ==================================================
# VALIDATE LOGIN
# ==================================================

def validate_login(

    username,
    password

):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    password_hash = hash_password(password)

    cursor.execute(

        """
        SELECT role

        FROM users

        WHERE username = ?
        AND password_hash = ?
        """,

        (

            username,
            password_hash

        )

    )

    result = cursor.fetchone()

    conn.close()

    if result:

        return {

            "authenticated": True,

            "role": result[0]

        }

    return {

        "authenticated": False,

        "role": None

    }

# ==================================================
# USER EXISTS
# ==================================================

def user_exists(username):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT username

        FROM users

        WHERE username = ?
        """,

        (username,)

    )

    result = cursor.fetchone()

    conn.close()

    return result is not None