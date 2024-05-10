import mysql.connector
import datetime



def get_connection():
    try :
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="supervision_onduleurs"
        )
        return mydb
    except:
        print("Connection failes")


def get_min_consumption():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT MIN(consomation) FROM consomation")
    return cursor.fetchone()[0]

def get_max_consumption():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT MAX(consomation) FROM consomation")
    return cursor.fetchone()[0]

def get_avrg_consumption():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT AVG(consomation) FROM consomation")
    return cursor.fetchone()[0]

def get_current_month_consumption():
    curent_month = 9
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT SUM(consomation) FROM consomation WHERE MONTH(date_de_consomation) = %s", (curent_month,))
    return cursor.fetchone()[0]
