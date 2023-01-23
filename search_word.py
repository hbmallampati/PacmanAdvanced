import os
from os import listdir
from os.path import isfile, join
mypath = os.getcwd()
list_of_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in list_of_files:
    count = 0
    with open(i, 'r') as f:
        a = f.readline()
        count += 1
        if 'getGhostPositions()' in a:
            print(i, ':', count)
        while a != '':
        #    print(a, end='')
            a = f.readline()
            count += 1
            if 'getGhostPositions()' in a:
                print(i, ':', count)