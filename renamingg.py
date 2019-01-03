import os
import sys
import glob

def search(path):
    result = 0
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            result += search(file_path)
        file_r = file.replace('\\','')
        file_r = file_r.replace('/','')
        file_r = file_r.replace('*','')
        file_r = file_r.replace('?','')
        file_r = file_r.replace('\"','\'')
        file_r = file_r.replace('<','[')
        file_r = file_r.replace('>',']')
        file_r = file_r.replace('|','')
        if file!=file_r:
            file = os.path.join(path,file)
            file_r = os.path.join(path,file_r)
            print(file, file_r)
            os.rename(file, file_r)
            result+=1
    return result

if len(sys.argv) is 1:
    print(str(search(".")) + " files changed!")
elif len(sys.argv) is 2:
    print(str(search(sys.argv[1])) + " files changed!")
else:
    print("illegal argument")
