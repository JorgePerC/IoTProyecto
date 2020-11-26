import serial as ard
import serial.tools.list_ports as portInterface
from datetime import date, datetime
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

from MySQLCnnt import DB

def findArduino():
    """
    Automatically search for the Arduino port
    Default bauRate and port are 9600 and COM5
    """
    port = "COM5"
    bitsPerSecond = 9600

    for p in portInterface.comports():
        if "Arduino" in p.description or not("Bluetooth" in p.description):
            port = p.device
            print("Using port: ", port)
    
    # Serial port connection 
    return ard.Serial(port, bitsPerSecond)

def readSerialPort(SP: object):
    """
    Takes the input from the SP and waits for
    the beggining and end of the transmission.
    Returing a list with all the readings necesary
    to give reliabale measurements 
    """
    append = False
    readingsList = []
    print("Oprime el botón")
    while (True):
        reading = SP.readline()
        # Para que lo pase a un string entendible
        line = reading.decode("ascii")
        # Otro de limpieza 
        line = line.rstrip()
        # print(line)

        if "Transmit" in line:
            append = True
            print("Inicio")
            continue
        elif "Endtrans" in line:
            append = False
            print("Ya no recibe")
            break
        if append:
            readingsList.append(line)

    return readingsList

def processRawData (data: list):
    """
    Divide all the incoming data into separate lists
    to be processed with its especific algorithm
    """
    listHR = []
    listSaO2 = []

    # Sólo apendea los números
    for d in data:
        nums = getOnlyInts(d)
        listHR.append((nums["Hr"], nums["Milis"]))
        listSaO2.append((nums["RedB"], nums["IrB"], nums["Milis"]))

    return (listHR, listSaO2)

def getOnlyInts(s: str):
    """
    Process the string reading from the serialPort
    and returns a list only with the data we are
    interested in.
    """
    stringList = s.split()
    intHr = int(stringList[1])
    intRed = int(stringList[3])
    intIrB = int(stringList[5])
    intMs = int(stringList[7])
    return {"Hr": intHr, "RedB": intRed, "IrB": intIrB, "Milis": intMs}
    # return [intHr, intRed, intIrB, intMs]

def smooth_curve_average(points, sample_size):
    """
    Takes a list as an input an process it to have
    a -saple_size- point moving average.
    """
    smoothed_points = []
    sample_size
    for i in range (0, len(points), sample_size):
        avg = sum(points[i:i+sample_size])
        avg = avg/sample_size
        smoothed_points.append(avg)

    return smoothed_points

def processData_HR(data: list):
    """
    Takes a list as an input and gives back 
    a list ready to be inserted into the DB
    with the final HR reading
    """
    user = ""
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    todayDate = date.today()

    hearRate = 0
    readingsValue = [i[0] for i in data]
    milisValue = [i[1] for i in data]

    nuevosValores= smooth_curve_average(readingsValue, 3)# UTIL

    peaks = find_peaks(nuevosValores)[0] # UTIL POR SKIKIT

    plt.plot(nuevosValores)
    #print(peaks)
    plt.scatter(peaks, [nuevosValores[j] for j in peaks], marker='+', c='Red')
    
    hearRate = (60000 * len(peaks)) / (milisValue[-1] - milisValue[0])# UTIL
    print("HeartR", hearRate)
    plt.show()
    # Do something
    return [user, str(todayDate) + " " + time, hearRate]

def processData_Ox(data: list):
    """
    Takes a list as an input and gives back 
    a list ready to be inserted into the DB
    with the final SaO2 reading
    """
    user = ""
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    todayDate = date.today()

    oxigenLevel = 0
    # Do something
    
    return [user, str(todayDate) + " " + time, oxigenLevel]

def realMain():
    
    serialPort = findArduino()
    
    inputData = readSerialPort(serialPort)
    rawDataHR, rawDataSaO2 = processRawData(inputData)

    # dataSaO2 = processData_Ox(rawDataSaO2)

    dataHR = processData_HR(rawDataHR)

    print("----------")
    print(dataHR)

    # db =   DB("IoT_Proyecto", save = True)

    # db.insertData("HR_Readings", ["User", "Time", "HR"], dataHR)

    # db.insertData("SaO2_Readings", ["User", "Time", "SaO2"], dataSaO2)



if __name__ == "__main__":
    realMain()

    # serialPort = findArduino()
    
    # rawDataHR = readSerialPort(serialPort)

