from datetime import date
from zipfile import ZipFile
import glob

#zipFileName gonna be name of file that refers current time
zipFileName = date.today()
zipFileName = zipFileName.strftime("%b-%d-%Y")
zipObject = ZipFile(zipFileName , 'w')

files = glob.glob('*.FDB')

for n in files:
    zipObject.write(n)
