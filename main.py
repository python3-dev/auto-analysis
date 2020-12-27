import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns

df = pd.read_csv('cars_ds_final_cleaned.csv', header=0, index_col=0, engine='c', sep=',', memory_map=True)

#sns.set_theme(style="white")

def processSelectedOption(input_label):
    output_label = input_label.replace('_', ' ').title()
    return(output_label) 

st.title("Automobiles of India")
st.header("A price-performance analysis of selected automobiles")
st.subheader("5 performance parameters of 853 Indian automobiles are compared with their ex-showroom price.")

link  = "Source data: [Indian Cars Dataset, Abhinav Medhekar] (https://www.kaggle.com/medhekarabhinav5/indian-cars-dataset)"
st.markdown(link, unsafe_allow_html=True)

option_list_1 = ['Displacement', 'max_power', 'max_torque', 'ARAI_Certified_Mileage']


selected_option_1 = st.selectbox("Select the parameter to compare", option_list_1, index=0, format_func=processSelectedOption) #key=None

if selected_option_1 == 'Displacement':
    size_param = 'max_power'
else:
    size_param = 'Displacement'

min_size = 40
scale_factor = (df[size_param].max()/df[size_param].min())**(1/1.75)
max_size = min_size*scale_factor

st.write(f"Selected option: {selected_option_1}")
fig, ax = plt.subplots(figsize = (7,5))

sns.scatterplot(x=selected_option_1, y="Ex-Showroom_Price", size=size_param, sizes = (min_size, max_size), data=df, hue="Fuel_Type", alpha=.5, palette="muted")
st.pyplot(fig)
