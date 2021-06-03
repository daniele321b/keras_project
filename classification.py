
 

import csv
import shutil, os
import glob 

def create_list(path):
    list = os.listdir(path)
    return list

def classification(input_f, labels_f): 
    if os.path.exists(input_f+'0')==False:
        os.makedirs(input_f+'/0')
        
    if os.path.exists(input_f+'1')==False:   
        os.makedirs(input_f+'1')
    
        
    f = open(labels_f, newline='')
    reader = csv.reader(f, delimiter=',')
    count = 0
    for row in reader:
        if count !=0:
            file = row[0]
            label = row[1]
            if label == '0':
                try:
                    shutil.move(input_f+file, input_f+str(0))
                except:
                    print("Folder alreay exits")
            else:
 
                try:
                    shutil.move(input_f+file, input_f+str(1))
                except:
                    print("Folder alreay exits")
        count = count +1

input_f = './video_input/'
labels_f = './labels.csv'
classification(input_f,labels_f)

