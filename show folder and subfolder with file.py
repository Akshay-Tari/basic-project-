import os
for folderName, subfolders, filenames in os.walk('C:\\fun'):
    print('The current folder is '+ folderName)

    for subfolder in subfolders:
        print ('subfolder of '+ folderName + ':' + subfolder)

    for filename in filenames:
        print ('file inside '+ folderName +':'+ filename)

    print('')
        
