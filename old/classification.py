
 

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
    
    if os.path.exists(input_f+'fail')==False:   
        os.makedirs(input_f+'fail')    
        
    f = open(labels_f, newline='')
    reader = csv.reader(f, delimiter=',')
    count = 0
    for row in reader:
        if count !=0:
            file = row[0]
            label = row[1]
            if label == '0':
                #print('./0/'+label)
                #print(os.path.exists(input_f+'0/'+label))
                #if (os.path.exists(input_f+'0/'+label) == False): 
                try:
                    shutil.move(input_f+file, input_f+str(0))
                except:
                    print("Folder alreay exits")
            else:
                #print(os.path.exists(input_f+'0/'+label))
                ##print('./1/'+label)
                #if (os.path.exists(input_f+'1/'+label) == False):
                try:
                    shutil.move(input_f+file, input_f+str(1))
                except:
                    print("Folder alreay exits")
        count = count +1


#input_f = './test_images/'
#labels_f = './labels_test_images.csv'
#classification(input_f,labels_f)
#
#fail_list = create_list("./test_images/")
#for file in fail_list:
#    if file.endswith(".jpg"):
#        print(file)
#        shutil.move('./test_images/'+file, './test_images/fail')

input_f = './train_images/'
labels_f = './labels_train_images.csv'
classification(input_f,labels_f)

#fail_list = create_list("./train_images/")
#for file in fail_list:
#    if file.endswith(".jpg"):
#        print(file)
#        shutil.move('./train_images/'+file, './train_images/fail')

