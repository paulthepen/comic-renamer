import re
import shutil, os


#lists variations of each filename and creates pattern matches for each
def variationFinder(fileName):
    pattern3Digit=re.compile(r'(.*)(\s)(\d{3})(\s)*(\(\d{4}\))(.*)(.cbz|.cbr)')
    pattern4Digit=re.compile(r'(.*)(\s)(\d{4})(\s)*(\(\d{4}\))(.*)(.cbz|.cbr)')
    pattern2Digit=re.compile(r'(.*)(\s)(\d{2})(\s)*(\(\d{4}\))(.*)(.cbz|.cbr)')
    patternOfNum=re.compile(r'(.*)(\s)(\d{2})\s*(\(of.*\))\s*(\(\d{4}\))(.*)(.cbz|.cbr)')
    patternNoNum=re.compile(r'(.*)(\s)()()(\(\d{4}\))(.*)(.cbz|.cbr)')
    if pattern4Digit.search(fileName) is not None:
        newName=pattern4Digit.search(fileName)
        return newName
    elif pattern3Digit.search(fileName) is not None:
        newName=pattern3Digit.search(fileName)
        return newName
    elif pattern2Digit.search(fileName) is not None:
        newName=pattern2Digit.search(fileName) 
        return newName
    elif patternOfNum.search(fileName) is not None:
        newName=patternOfNum.search(fileName)
        return newName
    elif patternNoNum.search(fileName) is not None:
        newName=patternNoNum.search(fileName)
        return newName    
    else:
        return None
        
    
