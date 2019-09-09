import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random
import pickle

DATADIR = "/Users/roskor/Downloads/TODAS_LETRAS"
CATEGORIES = ["O","S","T","Y","R","AMIGO"]


training_data = []

def create_training_data():
    
    width = 500
    heigth = 350
    for category in CATEGORIES:  # all categories

        path = os.path.join(DATADIR,category)  # create path 
        class_num = CATEGORIES.index(category)  # get the classification  0 = "0", 1 = "S" ...

        for img in tqdm(os.listdir(path)):  # iterate over each image per categories
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (width, heigth))  # resize to normalize data size
                training_data.append([new_array, class_num])  # add this to our training_data
            except Exception as e:  # in the interest in keeping the output clean...
                pass

create_training_data()

random.shuffle(training_data)



X = []
y = []
def separete_features_label(data):
    for features,label in tqdm(data):
    X.append(features)
    y.append(label)
    X = np.array(X).reshape(-1, width, heigth, 1)
    return X,y

separete_features_label(training_data)


pickle_out = open("final_x.pickle","wb")  # save features as pickle
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("final_y.pickle","wb")  # save labels as pickle
pickle.dump(y, pickle_out)
pickle_out.close()