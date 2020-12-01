import re
import shutil, os
from pathlib import Path

#creates a publisher folder if it doesn't exist and returns the path
def findPublisher(pathName, folder):
    publishPattern=re.compile(r'(.*)(DC|Marvel|Image|INDIE)(.*)')
    publisherFound=publishPattern.search(folder)
    if not os.path.exists('/mnt/onePool/Spidey/Comics/'+publisherFound.group(2)):        
        os.mkdir(publisherPathName)
    publisherPathName=(pathName/publisherFound.group(2))
    return publisherPathName

#deletes extraneous .txt files from folder
def deleteTxt(folder):
    fullPath=Path(folder)
    for foundTxt in fullPath.glob('*.txt'):
        os.unlink(foundTxt)
    return

#writes results to log file
def printLog(filename, finalPath, reName, finalFolder):
    path=Path('/', 'mnt', 'onePool', 'Spidey', 'log.txt')
    pathFile=open(path, 'a')
    pathFile.write("The file "+reName+" was created in "+finalPath+'/'+finalFolder+" from "+filename+'\n')
    pathFile.close()
