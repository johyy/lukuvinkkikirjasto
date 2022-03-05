from sqlite3 import Error
from database_connection import get_database_connection

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement
    Args:
        conn: Connection object
    	create_table_sql: a CREATE TABLE statement
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except Error as error:
        print(error)

def create_tables(conn):
    """ Create tables.
    Args:
        conn: Connection object
    """

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY,
                                        username text UNIQUE NOT NULL,
                                        password text NOT NULL,
                                        admin boolean NOT NULL
                                    ); """

    sql_create_recommendations_table = """CREATE TABLE IF NOT EXISTS recommendations (
                                    id INTEGER PRIMARY KEY,
                                    title text NOT NULL,
                                    link text NOT NULL,
                                    media text,
                                    author text,
                                    description text, 
                                    like_amount INTEGER REFERENCES likes
                                );"""

    sql_create_likes_table = """CREATE TABLE IF NOT EXISTS likes (
                                id INTEGER PRIMARY KEY,
                                result INTEGER,
                                recommendations_id INTEGER REFERENCES recommendations (i),
                                user_id INTEGER REFERENCES users
                                );"""

    # Create tables
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_recommendations_table)
        create_table(conn, sql_create_likes_table)
    else:
        print("Error! Cannot create the database connection.")

def initialise_database():
    # Create a database connection
    print("Creating database connection")
    connection = get_database_connection()

    # Create tables
    create_tables(connection)

if __name__ == '__main__':
    initialise_database()
