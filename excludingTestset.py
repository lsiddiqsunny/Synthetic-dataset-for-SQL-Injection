# import random
# #Generate 5 random numbers between 10 and 30
# randomlist = random.sample(range(1, 669), 100)
import pickle
# with open('listfile.data', 'wb') as filehandle:
#     # store the data as binary data stream
#     pickle.dump(randomlist, filehandle)

with open('listfile.data', 'rb') as filehandle:
    # read the data as binary data stream
    randomlist = pickle.load(filehandle)
    print(randomlist)

import os

# List all files in a directory using os.listdir
basepath = './project_Before/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        id = int(entry.split("_")[1])
        if id in randomlist:
            print(id,entry)
            try:
                os.remove(entry)
            except:
                print(id)
# List all files in a directory using os.listdir
basepath = './project_After/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        id = int(entry.split("_")[1])
        if id in randomlist:
            print(id,entry)
            try:
                os.remove(entry)
            except:
                print(id)
