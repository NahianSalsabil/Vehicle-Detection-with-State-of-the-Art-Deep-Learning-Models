import os, shutil

# First, create a list and populate it with the files
# you want to find (1 file per row in myfiles.txt)
files_to_find = []

arr = os.listdir('test/img/')

for files in arr:
    filename,ext = files.split('.')
    filename = filename+'.txt'
    files_to_find.append(filename)

# Then we recursively traverse through each folder
# and match each file against our list of files to find.
for root, dirs, files in os.walk('D:\\atikul\\train\\txt\\txt3\\'):
    for _file in files:
        if _file in files_to_find:
            print ('Found file in: ' + str(root))
            src = 'test/label/'
            shutil.copy(os.path.abspath(root + '/' + _file), os.path.join(src, _file))
            #shutil.copy(os.path.abspath(root + '/' + _file), os.path.join(src, "cpy5" + _file))
