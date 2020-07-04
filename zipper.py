import datetime
from zipfile import ZipFile
import glob

#zipFileName gonna be name of file that refers current time
zipFileName = datetime.datetime.now()
zipFileName = str(zipFileName)
zipObject = ZipFile(zipFileName , 'w')

files = glob.glob('*.FDB')

for n in files:
    zipObject.write(n)