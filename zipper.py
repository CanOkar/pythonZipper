from datetime import date
from zipfile import ZipFile, ZIP_DEFLATED
import glob, datetime, os

doesLogFileExist = glob.glob("*.txt")
doesLogFileExist = str(doesLogFileExist)
logFile = open("log.txt", "a") #create a file named "log.txt" if it does not exist
    
zipFileName = date.today() #zipFileName gonna be name of file that refers current time
zipFileName = zipFileName.strftime("%d-%m-%Y")
zipObject = ZipFile(zipFileName, compression=ZIP_DEFLATED, compresslevel=9, mode='w')

files = glob.glob('*.FDB')
logFile = open("log.txt", "a")
logFile.write("Sıkıştırma işlemi " + str(datetime.datetime.now()) + "itibariyle başladı.\n")
logFile.close()
print("Sıkıştırma işlemi " , str(datetime.datetime.now()) , "itibariyle başladı.")

for n in files:
    zipObject.write(n)

os.rename(zipFileName , zipFileName + ".zip") #add .zip extension to file
logFile = open("log.txt", "a")
logFile.write("Sıkıştırma işlemi " + str(datetime.datetime.now()) + "itibariyle tamamlandı.\n")
logFile.close()
print("Sıkıştırma işlemi " + str(datetime.datetime.now()) + "itibariyle tamamlandı.")


