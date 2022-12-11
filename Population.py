# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:22:39 2022

@author: Adithya O
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#A function to plot the bar graph  
def barGraph(df,columns, xlabel, ylabel, title):
    """
    The function bargraph() is used to plot a bar graph representing the percentage of people
    living in the urban area in each selected country,and the effect of urbanisation in the agricultural 
    land during the period of 1965 to 2015.
    """    
    labels = df["Country Name"]
    x = np.arange(len(labels))
    w = 0.12
    plt.figure()
    fig, ax = plt.subplots()
    i=0
    for y in columns:
        ax.bar(x+(i*w),df[y],width=w,label=y,edgecolor='k', align='center')
        i=i+1   
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.set_xticks(x, labels)
    ax.legend()    
    fig.tight_layout()  
    plt.show()
    
#reading the data set    
dataloc="Dataset.csv"
Data = pd.read_csv("Dataset.csv",sep='\t',skiprows=4,engine='python')
df_Data = pd.DataFrame(Data)
#Choosing indicator (Urban population (% of total population)) and updating dataframe according to that
urbanPopulation = df_Data.loc[df_Data['Indicator Name'].isin(["Urban population (% of total population)"])]
df_urbanPopulation = urbanPopulation.dropna()
df_urbanPopulationSelected = df_urbanPopulation.loc[df_urbanPopulation['Country Code'].isin(['ABW','BRA','IND','ARG','HRV','CHN'])]
df_population = df_urbanPopulationSelected.loc[:, ['Country Name','1965', '1975', '1985', '1995', '2005', '2015']].reset_index(drop=True)

#Choosing indicator (Agricultural land (% of land area)) and updating dataframe according to that
df_agriculturalLand = df_Data.loc[df_Data['Indicator Name'].isin(["Agricultural land (% of land area)"])]
df_agriculturalLandSelected = df_agriculturalLand.loc[df_agriculturalLand['Country Code'].isin(['ABW','BRA','IND','ARG','HRV','CHN'])]
df_agriculturalLand = df_agriculturalLandSelected.loc[:, ['Country Name','1965', '1975', '1985', '1995', '2005', '2015']].reset_index(drop=True)
print(df_agriculturalLand)
years=['1965','1975','1985','1995','2005','2015']


#Calling functions to plot the grpahs
barGraph(df_population,years,'Country','Population Percentage','Urban population (% of total population)')
barGraph(df_agriculturalLand,years,'Country','Agricultural land Area Percentage','Agricultural land (% of land area)')











