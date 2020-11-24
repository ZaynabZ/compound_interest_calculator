import streamlit as st
import pandas as pd

years = [2, 3, 4, 5, 6, 7, 8, 9, 10]

st.title("Compound Interest Calculator")
st.sidebar.header("User Input Values")

def user_input_features():
    
    interest_rate = st.sidebar.slider('Interest Rate %', 5.0, 50.0, 10.0)
    
    initial_amount_input = st.sidebar.text_input('Please Inter Initial Amount (MAD)', 10000)
    
    years_cb = st.sidebar.selectbox('Select number of years', years, 2)
    
    data = {
        'interest_rate': interest_rate,
        'initial_amount_input': initial_amount_input,
        'years': years_cb
        }
    
    #Index to use for resulting frame.
    features = pd.DataFrame(data, index=['values'])
    
    return features

df = user_input_features()

st.subheader('User\'s entered Parameters:')
st.write(df)
    
def interest_compound(initial, rate, years):
   return initial * (pow((1 + rate / 100), years) - 1)

int_comp = interest_compound(float(df.initial_amount_input), float(df.interest_rate), float(df.years))
st.subheader('The Computed Compound Interest is :')
st.write(int_comp)
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    