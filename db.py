import mysql.connector
import os
#from dotenv import load_dotenv

#load_dotenv()


def get_connectionn():
    return mysql.connector.connect(
       host=os.getenv("mysql_host"),
        user=os.getenv("mysql_user"),
        password=os.getenv("mysql_passwd"),
        database=os.getenv("mysql_db")
    )


def get_connection():
    return mysql.connector.connect(
        host="192.168.56.102",
        user="wans",
        password="wans",
        database="commerce"
)

