from fileinput import filename
import os
import shutil

from_dir = 'C:/Users/ANSHIKA TYAGI/Downloads'
to_dir = 'C:/Users/ANSHIKA TYAGI/Desktop'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for fileName in list_of_files:
    name, extn = os.path.splitext(fileName)
    print(name)
    print(extn)

    if extn == '':
       continue
    if extn in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir + '/' + fileName
        path2 = to_dir +'/'+ 'Image_Files'
        path3 = to_dir + '/' + "Image_Files" + '/' + fileName
        print('path1', path1)
        print('path3', path3)

if os.path.exists (path2):
    print('Moving' + fileName + '.....') 

    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print('Moving' + fileName + '.....')
    shutil.move(path1, path3)           
