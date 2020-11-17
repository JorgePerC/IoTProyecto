import random
from MySQLCnnt import DB


def createUser(db: object, name: str, lastName: str, age: int, 
                excercise: int, profilePic: str, avergage_SaO2: int):
    if excercise not in ["Few", "Ocasional", "Proffesional"]:
        print("Datos inválidos. Excercise")
        return -1
    # Ver cómo hacer lo de la imagen
    if not 0 < avergage_SaO2 < 100:
        print("Datos inválidos. Average SaO2")
        return -1
    
    insert_User(db, [name, lastName, age, excercise, profilePic, avergage_SaO2])

def insert_User(db: object, data: list):
    db.insertData("users", ["name","last_name", "age", "excersice", "Profile_Img", "average_SaO2"],
                     data)

def inserReading_HR(db: object, data: list):
    db.insertData("HR_Readings", ["id_user", "time", "hr_reading"], data)

def inserReading_SaO2(db: object, data: list):
    db.insertData("SaO2_Readings", ["id_user", "time", "sao2_reading"], data)

def sampleData_HR():
    return [ random.randint(1, 5), sampleData_Time(), random.randint(60, 100)]

def sampleData_Time():
    return "2020/"+ str(random.randint(1, 12)) + "/" + str(random.randint(1, 28))

def sampleData_SaO2():
    return [ random.randint(1, 5), sampleData_Time(), random.randint(75, 100)]

def createUsers(db):
    createUser(db, "Jorge", "Pérez", 19, "Few", "imagen.jpg", 93)
    print("Data insertado correctamente")
    createUser(db, "Luis", "Fdz", 19, "Few", "imagen2.jpg", 95)
    createUser(db, "Josue", "Mojica", 19, "Ocasional", "imagen3.jpg", 90)
    createUser(db, "Mickey", "Mouse", 80, "Few", "imagen4.jpg", 92)
    createUser(db, "Dr", "García", 39, "Proffesional", "imagen5.jpg", 97)  

db =  DB("IoT_proyecto", save = True)

# createUsers(db)

# print("Acabo")
# for _ in range(1000):
#     inserReading_HR(db, sampleData_HR())
#     inserReading_SaO2(db, sampleData_SaO2())
print("Terminó")