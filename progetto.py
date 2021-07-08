import tensorflow as tf
import pandas as pd
import cv2
import os
import numpy as np
import keras
import sys
from keras.models import Sequential
from keras.layers import Dense, Conv2D , Activation, MaxPool2D , Flatten , Dropout, TimeDistributed, MaxPooling2D, LSTM 

def temporalize2(X,lookback):
    output_X = []
    for i in range(len(X)-lookback):
        t = []
        for j in range(0,lookback):
            # Gather past records upto the lookback period
            #t.append(X[[(i+j)], :])
            t.append(X[(i+j), :])
            #print("t di ", i,j)
        output_X.append(t)
    return output_X

def extraction(input_dir):
    n_video = 0
    X = []
    Y = []
    x1 = []
    y1 = []
    img_height , img_width = 64, 64
    seq_len = 250
    classes = ["0","1"]
    classes_list = os.listdir(input_dir)
     
    for c in classes_list:
        print("extracting class:",c)
        files_list = os.listdir(os.path.join(input_dir, c))
        for f in files_list:
            vidObj = cv2.VideoCapture(os.path.join(os.path.join(input_dir, c), f))
            count = 1
            out = []
            x1 = []
            while count <= seq_len: 
                success, image = vidObj.read() 
                if success:
                    image = cv2.resize(image, (img_height, img_width))
                    x1.append(image)
                    count += 1
                else:
                    break        
            if count-1 == seq_len :
                n_video = n_video +1
                out = temporalize2(np.array(x1),50)    
                for i in range(len(out)):
                    X.append(out[i])
                    y = [0]*len(classes)
                    y[classes.index(c)] = 1
                    Y.append(y)
            
    print("Num videos:",n_video)
    X = np.asarray(X)
    Y = np.asarray(Y)
    return X, Y    
 

def main():
    print("..START...")
    X, Y = extraction("video_input/")
    print("...END EXTRACTION...")
    print("Numero di block frames:",len(X))

    print("...RESHAPE...")
    # Normalizzazione
    X = np.array(X) / 255
    X.reshape(-1, 64, 64, 1)
    print("...END RESHAPE...")
   
    print("..CREATE MODEL...")
    img_height , img_width = 64, 64
    seq_len = 50
    classes = ["0","1"]  
    model = Sequential()
    model.add(TimeDistributed(Conv2D(32, 3, activation='relu', padding='same'), input_shape=(seq_len, img_height, img_width, 3)))
    model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2),  padding='same')))
    model.add(TimeDistributed(Conv2D(64, 3, activation='relu')))
    model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2),  padding='same' )))
    model.add(TimeDistributed(Conv2D(128, 3, activation='relu')))
    model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2),  padding='same' )))
    model.add(TimeDistributed(Flatten()))
    model.add(LSTM(256, return_sequences=True, dropout=0.5))
    model.add(LSTM(64, return_sequences=False ))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=["accuracy"])
    model.summary()
    
    print("..START FIT...")
    history = model.fit(x = X, y = Y, epochs = 10 ,batch_size=50)
    print("...END FIT..." )

    print("..START CREATION TEST...")
    X_test, y_test = extraction("video_input4/")
    print("...END EXTRACTION...")

    print("...RESHAPE TEST...")
    # Normalizzazione
    X_test = np.array(X_test) / 255
    X_test.reshape(-1, 64, 64, 1)
    print("...END RESHAPE TEST...") 
    
    print("...START EVALUATION...")
    score = model.evaluate(X_test, y_test, verbose=0, batch_size=50)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1]) 
    print("...END EVALUATION...")
    
    print("...START PREDICTION...")
    predicted = model.predict(X_test)
    print(predicted)
    print("...END PREDICTION...")
    

if __name__ == "__main__":
    sys.stdout = open("report.txt","w")
    main()
    sys.stdout.close()
