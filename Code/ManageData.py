import random

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
    pass

def inserReading_SaO2(db: object, data: list):
    db.insertData("SaO2_Readings", ["User", "Time", "SaO2"], data)
    pass

def sampleData_HR(db: object, data: list):
    return random.randint(60, 100)

def sampleData_Time():
    return

def sampleData_SaO2():
    return random.randint(85, 100)
    

