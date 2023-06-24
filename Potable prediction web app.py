# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 00:44:04 2023

@author: prabh
"""
import numpy as np

import pickle
import streamlit as st


loaded_model = pickle.load(open('trained_model2.sav', 'rb'))

#creating   a function for prediction
def water_pediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The water is not potable '
    else:
     return 'The water is  potable'

    
def main():
     
     #giving a title
     st.title('Water Potable Check App')
     
     
     ph=st.text_input('Enter the  ph value') 
     hardness =st.text_input('Enter  Hardness  value')
     solids=st.text_input('Enter the solids   value')
     chlora=st.text_input('Enter the chlora  value')
     sulfate=st.text_input('Enter  the sulfate value')
     conductivity=st.text_input('Enter  the  conductivity value')
     organic_carbon=st.text_input('Enter   the  organic  value')
     trihalomethane=st.text_input('Enter  the  trihalomethane  value')
     turbidity=st.text_input(' Enter the  turbitdity  value')
     
     #code for prediction
     potabale=''
     
     #creating anutton for prediction
     
     if st.button('Water Potability Test Results'):
             potabale =water_pediction([ph,hardness,solids,chlora,sulfate,conductivity,organic_carbon,trihalomethane,turbidity])
         
     st.success(potabale)  
    
if __name__=='__main__':
    main()
