from datetime import datetime
import sqlite3


class Database():

    def __init__(self, dbName: str):
        self.dbName = dbName

    def get_connection(self):
        """
        This function establishes connection with database.
        """
        try:
            db = sqlite3.connect(self.dbName)
            return db
        except:
            print("Connection could not be established.")

    def create_table_name(self):
        """
        This function creates the names of the tables in the database.
        """
        tableName = "data_" + str(datetime.today().strftime('%Y%m%d'))
        return tableName

    def create_table(self):
        """
        This function creates the database table.
        """
        tableSql = f'''
        CREATE TABLE IF NOT EXISTS "{self.tableName()}" (
            "email" text,
            "username" text,
            "name_surname" text,
            "emailuserlk" integer,
            "usernamelk" integer,
            "year_of_birth"	integer,
            "month_of_birth" integer,
            "day_of_birth" integer,
            "country" text,
            "ap" integer
        );
        '''
        self.get_connection().execute(tableSql)

    def bulk_insert(self,user_list):
        """
        This function adds the information in the user_list in bulk
        """
        for user in user_list:
            self.insert_data(user)

    def insert_data(self, user):
        """
        This function created to insert user to database
        """
        dbConnection = self.get_connection()  # Try to connect to the requested database
        try:
            insertSql = f'''
            INSERT INTO {self.tableName()}(
            email,
            username,
            name_surname,
            emailuserlk,
            usernamelk,
            year_of_birth,
            month_of_birth,
            day_of_birth,
            country,
            ap)
            VALUES (?,?,?,?,?,?,?,?,?,?)'''

            cur = dbConnection.cursor()
            cur.execute(insertSql, (user.email, user.username, user.name_surname, user.emailuserlk, user.usernamelk,
                                    user.year_of_birth, user.month_of_birth, user.day_of_birth, user.country,
                                    user.ap))  # Execute the given insert query
            dbConnection.commit()  # Commit ends a transaction within database

        except:
            print("Transaction failed.")

        finally:
            dbConnection.close()

