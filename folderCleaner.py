import os 
import shutil

folder = os.path.join(os.path.dirname(__file__), "dateien")

imageFolder = os.path.join(folder, "Bilder")
docFolder = os.path.join(folder, "Dokumente")
codeFolder = os.path.join(folder, "Code")
miscFolder = os.path.join(folder, "Sonstiges")

def checkAndMkdir(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)

checkAndMkdir(imageFolder)
checkAndMkdir(docFolder)
checkAndMkdir(codeFolder)
checkAndMkdir(miscFolder)

def filenameAndMove(destination):
    fileNameWithPath = os.path.join(folder, filename)
    outFileNameWithPath = os.path.join(destination, filename)
    shutil.move(fileNameWithPath, outFileNameWithPath)
    print(fileNameWithPath, f"<--moved to {destination}-->")
    print(outFileNameWithPath)
    print("---------")

for filename in os.listdir(folder): 
    fileNameWithPath = os.path.join(folder, filename)

    if os.path.isdir(fileNameWithPath):
        continue
    
    elif filename.lower().endswith('.jpg'):
        filenameAndMove(imageFolder)

    elif filename.lower().endswith((".txt", ".docx")):
        filenameAndMove(docFolder)
        
    elif filename.lower().endswith((".php", ".py", ".cpp")):
        filenameAndMove(codeFolder)
    
    else:
        filenameAndMove(miscFolder)
    
