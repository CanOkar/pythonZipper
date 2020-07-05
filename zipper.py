from datetime import date
from zipfile import ZipFile, ZIP_LZMA
import glob, datetime, os, time

logFile = open("log.txt", "a") #create a file named "log.txt" if it does not exist
    
zipFileName = date.today() #zipFileName gonna be name of file that refers current time
zipFileName = zipFileName.strftime("%d-%m-%Y")

zipObject = ZipFile(zipFileName, compression=ZIP_LZMA, mode='w')

files = glob.glob('*.exe')
logFile = open("log.txt", "a")
logFile.write("Compression process has started on " + str(datetime.datetime.now()) + "\n")
logFile.close()

print("-------------------------------------------------------------------------------")
print("Compression process has started on " + str(datetime.datetime.now()))
print("-------------------------------------------------------------------------------")

for n in files:
    zipObject.write(n)
zipObject.close()

os.rename(zipFileName , zipFileName + ".zip") #add .zip extension to file

logFile = open("log.txt", "a")
logFile.write("Compression process has finished on " + str(datetime.datetime.now()) + "\n")
logFile.close()

print("-------------------------------------------------------------------------------")
print("Compression process has finished on " +str(datetime.datetime.now()))
print("-------------------------------------------------------------------------------")
