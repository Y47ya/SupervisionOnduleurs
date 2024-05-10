import mysql.connector



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

