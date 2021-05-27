

import cv2
import os


def extractImages(pathIn, pathOut, name):
    if os.path.exists(pathOut)==False:
        os.makedirs(pathOut)
        
    len_input = len(name)
    name_file = name[0:len_input-5]
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*100))   
        success,image = vidcap.read()
        #print ('Read a new frame: ', success)
        cv2.imwrite( pathOut +name_file+ "_%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1 

def create_list(path):
    list = os.listdir(path)
    return list


if __name__=="__main__":
    #cartelle
    input_folder = './video_test/'
    output_folder = './test_images/'
    #Creo una lista di video
    video_list = create_list(input_folder)
    #iterative operation called to extract frames from video
    count = 0
    for video in video_list:
        #name = 'train_'+str(count)
        print(input_folder+video,output_folder, video)
        print(input_folder + 'extraction..'+str(count))
        count= count+1
        extractImages(input_folder+video,output_folder, video)
    print('Fine-1')
 
#cartelle
    input_folder = './video_train/'
    output_folder = './train_images/'
    #Creo una lista di video
    video_list = create_list(input_folder)
    #iterative operation called to extract frames from video
    count = 0
    for video in video_list:
        #name = 'train_'+str(count)
        print(input_folder+video,output_folder, video)
        print(input_folder + 'extraction..'+str(count))
        count= count+1
        extractImages(input_folder+video,output_folder, video)
    print('Fine-2')
 




