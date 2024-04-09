import psycopg2

def connect():
    connection = psycopg2.connect(
        dbname="cripto_project",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    return connection

def get_user_info():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_info;")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

def insert_user_info(login, password):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user_info (login, password) VALUES (%s, %s);", (login, password))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        return e
    
def delete_user_info(login):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM user_info WHERE login = %s;", (login))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        return e
    
def update_user_info(login, password):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE user_info SET password = %s WHERE email = %s;", (password, login))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        return e
