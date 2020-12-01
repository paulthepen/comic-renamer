import re
import shutil, os
import publisher, variation, subjecter
from pathlib import Path

#set path variables for original file location, the new file location, and setup the log file
downloadFolder = Path('mnt','onePool','Spidey','Downloads')
basePath = Path('mnt','onePool','Spidey','Comics')
logFile=open(Path('mnt','onePool','Spidey','log.txt'), 'w')
logFile.write("New Import:\n")
logFile.close()

#iterate through the root folders
for weeklyPack in os.listdir(downloadFolder):
    pathName=downloadFolder/weeklyPack
    publisher.deleteTxt(pathName)   #clears extraneous files
    print(pathName)

    #iterates through publisher folders, matches to existing, and modifies the publisher folder files will be moved to
    for folder in os.listdir(pathName):
        filePathName=pathName/folder
        publishedPath=publisher.findPublisher(basePath, folder)


        #gets each comic file, matches the name, formats, searches for subjects and copies to proper path
        for filename in os.listdir(pathName/folder):
            finalPath=publishedPath
            newName=variation.variationFinder(filename)
            if newName==None:
                continue
            reName = newName.group(3)+' '+newName.group(1)+' '+newName.group(5)+newName.group(7)
            subject=subjecter.subjFinder(newName.group(1))
            if subject is not None:
                finalPath=publishedPath/subject
            if not os.path.exists(finalPath/newName.group(1)):
                os.mkdir(finalPath/newName.group(1))
            shutil.move(pathName/folder/filename, finalPath/newName.group(1)/reName)
            finalFolder=newName.group(1)
            publisher.printLog(filename, finalPath, reName, finalFolder)
