import os 
import shutil

FILE_TYPE_MAP = {
    'jpg': 'Bilder',
    'png': 'Bilder',
    'txt': 'Dokumente',
    'docx': 'Dokumente',
    'php': 'Code',
    'py': 'Code',
    'cpp': 'Code',
    'mp4': 'Videos'
}

folder = os.path.join(os.path.dirname(__file__), "dateien")

for _, dir in FILE_TYPE_MAP.items():
    tmp = os.path.join(folder, dir)
    if not os.path.isdir(tmp):
        os.mkdir(tmp)
    
other = os.path.join(folder, "Sonstiges")
if not os.path.isdir(other):
    os.mkdir(other)


for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isdir(path):
        continue

    splitted = file.rsplit('.', 1)
    if len(splitted) == 2:
        extension = splitted[-1].lower()

        if extension in FILE_TYPE_MAP: 
            target = FILE_TYPE_MAP[extension]

            dest = os.path.join(folder, target, file)
            shutil.move(path, dest)

            continue
    
    shutil.move(path, os.path.join(other, file))
    # print(f"Konnte Datei nicht zuordnen: {file}")
