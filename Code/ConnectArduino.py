import serial as ard
import serial.tools.list_ports as portInterface
from datetime import date, datetime

from MySQLCnnt import DB

def findArduino():
    port = "COM5"
    bitsPerSecond = 9600

    for p in portInterface.comports():
        if "Arduino" in p.description or not("Bluetooth" in p.description):
            port = p.device
            print("Using port: ", port)
    
    # Serial port connection 
    return ard.Serial(port, bitsPerSecond)

def readSerialPort(SP: object):
    append = False
    readingsList = []
    while (True):
        reading = SP.readline()
        # Para que lo pase a un string entendible
        line = reading.decode("ascii")
        # Otro de limpieza 
        line=line.rstrip();
        print(line)


        if reading == "Transmit":
            append = True
        elif reading == "Endtrans":
            append = False
            break
        if append:
            readingsList.append(reading)
        # print(reading)
    return readingsList

def getRawData_HR():
    pass


def processData_HR(data: list):
    user = ""
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    todayDate = date.today()

    hearRate = 0
    # Do something
    
    return [user, str(todayDate + " " + time), hearRate]

def processData_Ox(data: list):
    user = ""
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    todayDate = date.today()

    oxigenLevel = 0
    # Do something
    
    return [user, str(todayDate + " " + time), oxigenLevel]

def realMain():
    
    serialPort = findArduino()
    
    rawDataHR = readSerialPort(serialPort)
    dataHR = processData_HR(rawDataHR)
    
    rawDataSaO2 = readSerialPort(serialPort)
    dataSaO2 = processData_Ox(rawDataSaO2)

    db =   DB("IoT_Proyecto", save = True)

    db.insertData("HR_Readings", ["User", "Time", "HR"], dataHR)

    db.insertData("SaO2_Readings", ["User", "Time", "SaO2"], dataSaO2)



if __name__ == "__main__":
    # realMain()

    serialPort = findArduino()
    
    rawDataHR = readSerialPort(serialPort)

