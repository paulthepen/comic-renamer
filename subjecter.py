import re
import shutil, os

#Searches for several subjects/characters and adds an additional subfolder to the final path
def subjFinder(baseName):
    patternBatman=re.compile(r'(.*)(Batman)(.*)')
    patternSuperman=re.compile(r'(.*)(Superman)(.*)')
    patternAvengers=re.compile(r'(.*)(Avengers)(.*)')
    patternSpiderMan=re.compile(r'(.*)(Spider-Man)(.*)')
    patternXMen=re.compile(r'(.*)(X-Men)(.*)')
    patternCap=re.compile(r'(.*)(Captain America)(.*)')
    patternFlash=re.compile(r'(.*)(Flash)(.*)')
    patternHarley=re.compile(r'(.*)(Harley Quinn)(.*)')
    patternWonder=re.compile(r'(.*)(Wonder Woman)(.*)')
    patternIron=re.compile(r'(.*)(Iron Man)(.*)')

    if patternBatman.search(baseName) is not None:
        subFolder="Batman"
        return subFolder
    elif patternSuperman.search(baseName) is not None:
        subFolder="Superman"
        return subFolder
    elif patternAvengers.search(baseName) is not None:
        subFolder="Avengers"
        return subFolder
    elif patternSpiderMan.search(baseName) is not None:
        subFolder="Spider-Man"
        return subFolder
    elif patternXMen.search(baseName) is not None:
        subFolder="X-Men"
        return subFolder
    elif patternCap.search(baseName) is not None:
        subFolder="Captain America"
        return subFolder
    elif patternFlash.search(baseName) is not None:
        subFolder="Flash"
        return subFolder
    elif patternHarley.search(baseName) is not None:
        subFolder="Harley Quinn"
        return subFolder
    elif patternWonder.search(baseName) is not None:
        subFolder="Wonder Woman"
        return subFolder
    elif patternIron.search(baseName) is not None:
        subFolder="Iron Man"
        return subFolder
    else:
        return None
    #TODO: Make comics with no number go directly into publisher or into subject TPB
