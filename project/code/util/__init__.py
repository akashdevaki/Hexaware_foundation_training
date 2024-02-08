import _mysql_connector

# Package: util

import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser


class dbutil:
    def __init__(self,host,user,password,port,database):
        self.connection=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            port = '3306',
            database = 'virtualartgallery'
        )
        self.cursor=self.connection.cursor()










'''class PropertyUtil:

    @staticmethod
    def get_property_string():
        config = ConfigParser()
        config.read('db_config.ini')  # Assume the property file is named 'db_config.ini'

        host = config.get('virtualartgallery', 'localhost')
        database = config.get('virtualartgallery', 'virtualartgallery')
        user = config.get('virtualartgallery', 'root')
        password = config.get('virtualartgallery', 'root')
        port = config.get('virtualartgallery', '3306')

        return f"host={host} dbname={database} user={user} password={password} port={port}"


class DBConnection:

    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                connection_string = PropertyUtil.get_property_string()
                DBConnection.connection = mysql.connector.connect(connection_string)
                if DBConnection.connection.is_connected():
                    print("Connected to the database")
                else:
                    print("Failed to connect to the database")

            except Error as e:
                print(f"Error: {e}")

        return DBConnection.connection


# Example usage:
connection = DBConnection.get_connection()
#Perform database operations using the 'connection' object

host = 'localhost'
database = 'virtualartgallery'
user = 'root'
password = 'root'
port = 3306
'''