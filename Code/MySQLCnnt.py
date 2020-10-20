# Librería descargada desde MySQL // NO desde pip 
import mysql.connector

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
    def __init__(self, dbName : str, usr = "root", psw = "password"):
        try:
            self.cnx = mysql.connector.connect(user = usr, password = psw, host='127.0.0.1', database= dbName)
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    
    def getQuerryRes(self, query: str, param: tuple):
        # Objeto para ejecutar queries
        cursor = self.cnx.cursor()

        # If there are no parameters, we skip that param
        if (len(param) == 0):
            cursor.execute(query)
        else:
            cursor.execute(query, param) # (query, query_data) 
        # cursor, aka, queryResult
        return cursor

    def __del__(self, name):
        """
        Destructor for class database
        It only makes sure that MySQL
        gets close 
        """
        self.cnx.close()
        print("Finalizó :^D xdxdxd")