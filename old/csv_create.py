#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:23:44 2021

@author: danielecioffi
"""

import csv
import os 

def row_count(filename):
    with open(filename) as in_file:
        return sum(1 for _ in in_file)


def create_csv(f_old, f_new, count, total, flag):
    reader = csv.reader(f_old, delimiter=',')
    count = 0
    writer = csv.writer(f_new)
    if flag == 0:
        writer.writerow(['filename','label'])
    
    for row in reader:
            if count !=0:
                for i in range(total):
                    name = row[0]
                    l = len(name)
                    name_file = name[0:l-5]
                    line = [name_file+'_'+str(i)+'.jpg', row[1]]
                    writer.writerow(line)
            count = count +1
              
            

#f_old = open("labels_test.csv", newline='')
#flag = 0
#if os.path.exists('labels_test_images.csv') == True:
#     flag=1
#f_new = open('labels_test_images.csv', 'a',encoding='UTF8')
#count = row_count('labels_test.csv')
#create_csv(f_old,f_new,count,100, flag)
#f_old.close()
#f_new.close()

f_old = open("labels_train.csv", newline='')
flag = 0
if os.path.exists('labels_train_images.csv') == True:
     flag=1
f_new = open('labels_train_images.csv', 'a',encoding='UTF8')
count = row_count('labels_train.csv')
create_csv(f_old,f_new,count,100, flag)
f_old.close()
f_new.close()



