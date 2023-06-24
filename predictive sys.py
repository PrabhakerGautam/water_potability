# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 00:31:18 2023

@author: prabh
"""

import numpy as np

import pickle
loaded_model = pickle.load(open('C:/Users/prabh/Downloads/Deploy/trained_model.sav', 'rb'))


input_data = (9.445130,145.805402,13168.52915,9.444471,310.583374,592.659021,8.606397,77.577460,3.875165)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The water is not potable ')
else:
  print('The water is  potable')