import random
from MySQLCnnt import DB


def createUser(db: object, name: str, lastName: str, age: int, 
                excercise: int, profilePic: str, avergage_SaO2: int):
    if excercise not in ["Few", "Ocasional", "Proffesional"]:
        print("Datos inválidos. Excercise")
        return -1
    # Ver cómo hacer lo de la imagen
    if not 0 < avergage_SaO2 < 100:
        print("Datos inválidos. average SaO2")
        return -1
    
    insert_User(db, [name, lastName, age, excercise, profilePic, avergage_SaO2])

def insert_User(db: object, data: list):
    db.insertData("Users", ["Name","Last_Name", "Age", "Excersice", "Profile_Img", "Average_SaO2"],
                     data)

def inserReading_HR(db: object, data: list):
    db.insertData("HR_Readings", ["User", "Time", "HR"], data)

def inserReading_SaO2(db: object, data: list):
    db.insertData("SaO2_Readings", ["User", "Time", "SaO2"], data)

def sampleData_HR():
    return [ random.randint(0, 5), sampleData_Time(), random.randint(60, 100)]

def sampleData_Time():
    return "2020/"+ random.randint(1, 12)+ "/" + random.randint(1, 28)

def sampleData_SaO2():
    return [ random.randint(0, 5), sampleData_Time(), random.randint(75, 100)]
    

db =  DB("IoT", save = True)

for _ in range(0,1000):
    inserReading_HR(db, sampleData_HR())
    inserReading_SaO2(db, sampleData_SaO2())