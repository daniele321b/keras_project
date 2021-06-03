import shutil, os
import random

def create_list(path):
    list = os.listdir(path)
    return list

def classification_random(input_f):        
    list_images = create_list(input_f)
    if os.path.exists(input_f+'0')==False:
        os.makedirs(input_f+'/0')
        
    if os.path.exists(input_f+'1')==False:   
        os.makedirs(input_f+'1')
        
    for img in list_images:
        n = random.randint(0,1)
        if n==0:
            shutil.move(input_f+img, input_f+str(0))
        else:
            shutil.move(input_f+img, input_f+str(1))
    
    

input_f = './test_images/'
classification_random(input_f)

#fail_list = create_list("./test_images/")
#for file in fail_list:
#    if file.endswith(".jpg"):
#        print(file)
#        shutil.move('./test_images/'+file, './test_images/fail')


