import streamlit as st
import pandas as pd
import numpy as np

#To run this file, cd into the folder Application where this file represented and run: streamlit run [the py name]
# This file displays in localhost a map of the different places where these companies are located, with a red dot
addresses = {
    "Generatorvej 21": [55.72993, 12.4648], 
    "Lille Veksøvej 11": [55.757949, 12.228728], 
    "Lautrupvang 1": [55.733204, 12.391164], 
    "Novo Alle 1": [55.754555, 12.455185], 
    "Sundkrogsgade 4": [55.708655, 12.591288], 
    "Borupvang 4": [55.734142, 12.380579], 
    "Lautrupparken 40": [55.73613, 12.393105], 
    "Wildersgade 51": [55.674321, 12.591612], 
    "Gothersgade 14": [55.682038, 12.583964], 
    "Suderbovej 22-24": [57.4455297, 10.4937435],
    "Teglholmsgade 1": [55.653577, 12.544796], 
    "Grønningen 17": [54.788356, 11.688986],
    "Dynamovej 11": [55.730673, 12.463418], 
    "Købmagergade 11": [55.679721, 12.579087], 
    "Holmbladsgade 133": [55.667802, 12.618812], 
    "Brøndby Stadion 30": [55.649056, 12.417581], 
    "Overgaden Neden Vandet 9A": [55.672023, 12.588964], 
    "Skovmarken 3B": [55.789076, 12.540873], 
    "Bryggeristræde 2": [55.274825, 14.800772], 
    "Gråbrødrepassagen 9": [55.395903, 10.384222], 
    "Gearhalsvej 1": [55.660184, 12.514151], 
    "Tangen 6": [58.9274614, 11.6516802], 
    "Trollesmindealle 25": [55.924279, 12.283561], 
    "Jagtvej 157": [55.702334, 12.557268], 
    "Ryesgade 74": [55.694991, 12.571624]
}

# Create a DataFrame from the dictionary of addresses and their corresponding latitudes and longitudes
df = pd.DataFrame.from_dict(addresses, orient='index', columns=['lat', 'lon'])

# Display the DataFrame on a map using Streamlit
st.map(df)