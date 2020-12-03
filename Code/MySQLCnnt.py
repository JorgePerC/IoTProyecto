# Librería descargada desde MySQL // NO desde pip 
import mysql.connector
from mysql.connector.locales.eng import client_error

if __name__ == "__main__":
    try:
        """
        Intentar crear la conección con la base de datos
        IMPORTANTE:
            * Cambia tu usuario
            * Cambia tu contraseña
            * Cambia el nombre de tu DB (case sensitive)
            * Asegúrate de haber creado la DB, bruh
        """
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='IoT')
        
        # Objeto para ejecutar queries
        cursor = cnx.cursor()

        ## Ejemplos de consulta
        # query_data = (3,) # Tiene que ser una tupla
        # query = (f"SELECT * FROM rooms WHERE id_room > %s;")
        # cursor.execute(query, query_data)
        
        query_data = ()

        query = ("SELECT * FROM users")
        
        cursor.execute(query) # (query, query_data) 

        for result in cursor:
            print(result)

    except mysql.connector.Error as err:

        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            
    finally:
        cnx.close()
        print("Finalizó :^D xdxdxd")


class DB:
    def __init__(self, dbName : str, usr = "root", psw = "password", save = True):
        try:
            # La conexión de la base de datos tal cual
            self.cnx = mysql.connector.connect(user = usr, password = psw, host='127.0.0.1', database= dbName)
            # Objeto para ejecutar queries
            self.cursor = self.cnx.cursor()
            # Para que se guarden los datos o nel, xd 
            self.save = save 
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    
    def getQuerryRes(self, query: str, param = ()):
        """
        Method to read data from the Db, and posibly 
        add some parameters. The querry should be in
        MySQL format.
        """
        # If there are no parameters, we skip that param
        if (len(param) == 0):
            try:
                self.cursor.execute(query)
            except mysql.connector.Error as err:
                print(err)
        else:
            try:
                self.cursor.execute(query, param) # (query, query_data) 
            except mysql.connector.Error as err:
                print(err)
        # self.cursor, aka, queryResult
        return self.cursor

    def insertData(self, table: str, columns : list, values: list):
        """
        Method to call easier "Insert into"
        takes two lists as imputs, columns, should have the name
        for the columns you want to insert into, and values is 
        self explanatory. 
        """
        if(len(columns) == 0):
            pass
        # Por si no coinciden los parámetros:
        elif (len(columns) != len(values)):
            # MODIFICAR PARA LEVANTAR ERROR
            # raise mysql.connector.errorcode.ER
            print("No coinciden los parámetros")
            return None

        # Para quitar los "'" de los nombres de columnas
        columnas = str(columns)[1:-1].replace("'", "")
        # El [1:-1] es para que no aparezcan los corchetes "[]"
        query = "INSERT INTO {} ({})  VALUES ({});".format(table, columnas, str(values)[1:-1])
        print(query)
        
        try:
            self.cursor.execute(query)
            # Para que los datos se guarden
            if self.save:
                self.cnx.commit()
        except mysql.connector.Error as err:
            print(err)

    def changeData(self, table: str, column: list, values: list, *whereArgs):
        """
        TODO: Complete this method
        Method to Update data.
        I believe is working, but need to test it
        """
        query = "UPDATE {} as {}".format(table,  str(whereArgs)[1:-1])
        pass

    def closeConnection(self):
        """
        TODO: Depreciate
        Aditional destructor
        """
        try:
            self.cnx.close()
        except mysql.connector.Error as err:
                print(err)

    def __del__(self):
        """
        Destructor for class database
        It only makes sure that MySQL
        gets close 
        """
        try:
            # self.cursor.close()
            print("Cerro1")
            self.cnx.close()
            print("Cerro12")
        except mysql.connector.Error as err:
                print(err)