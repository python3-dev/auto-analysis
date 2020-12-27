import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns

df = pd.read_csv('cars_ds_final_cleaned.csv', header=0, index_col=0, engine='c', sep=',', memory_map=True)

def processSelectedOption(input_label):
    output_label = input_label.replace('_', ' ').title()
    return(output_label) 

st.title("Automobiles of India")
st.header("A price-performance analysis of selected automobiles")
st.subheader("853 Indian automobiles are compared to establish a logical relationship between the performance parameters and price.")

link  = "[Source data: Indian Cars Dataset, Abhinav Medhekar] (https://www.kaggle.com/medhekarabhinav5/indian-cars-dataset)"
st.markdown(link, unsafe_allow_html=True)

option_list_1 = ['Displacement', 'max_power', 'max_torque', 'ARAI_Certified_Mileage']

selected_option_1 = st.selectbox("Select the parameter to compare", option_list_1, index=0, format_func=processSelectedOption) #key=None
st.write(f"Selected option: {selected_option_1}")
fig, ax = plt.subplots()
sns.scatterplot(x=selected_option_1, y="Ex-Showroom_Price", data=df, hue="Fuel_Type", alpha=.5, palette="muted")
st.pyplot(fig)
