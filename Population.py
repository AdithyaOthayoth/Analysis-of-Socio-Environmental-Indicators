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
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),fancybox=True, shadow=True, ncol=6)    
    fig.tight_layout()  
    plt.show()


#A function to plot the line graph
def linegraph(df,columns, xlabel, ylabel, title): 
    """
    The linegraph function used to plot line grpah.
    The plot represents the total percentage of Co2 emissions from solid fuel consumption
    in each selected contries   
    """
    df = df.loc[:, ['Country Name','1965', '1975', '1985', '1995', '2005', '2015']].reset_index(drop=True).fillna(0.0)
    df=df.set_index('Country Name').transpose()
    df['Years'] = df.index
    temp_cols=df.columns.tolist()
    new_cols=temp_cols[-1:] + temp_cols[:-1]
    df=df[new_cols]
    df=df.reset_index(drop=True)
    df= df.rename_axis(None, axis=1)

    labels = df['Years']
    print(columns)
    x=df['Years']
    i=0
    plt.figure()
    for y in columns:
        plt.plot(x,df[y],linestyle='dashed',label=y)
        i=i+1   
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),fancybox=True, shadow=True, ncol=6)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()    




#reading the data set    
dataloc="Dataset.csv"
Data = pd.read_csv("Dataset.csv",sep='\t',skiprows=4,engine='python')
df_Data = pd.DataFrame(Data)

#Choosing indicator (Urban population (% of total population)) and updating dataframe according to that
urbanPopulation = df_Data.loc[df_Data['Indicator Name'].isin(["Urban population (% of total population)"])]
df_urbanPopulation = urbanPopulation.dropna()
df_urbanPopulationSelected = df_urbanPopulation.loc[df_urbanPopulation['Country Code'].isin(['HUN','BRA','IND','ARG','HRV','CHN'])]
df_population = df_urbanPopulationSelected.loc[:, ['Country Name','1965', '1975', '1985', '1995', '2005', '2015']].reset_index(drop=True)

#Choosing indicator (Agricultural land (% of land area)) and updating dataframe according to that
df_agriculturalLand = df_Data.loc[df_Data['Indicator Name'].isin(["Agricultural land (% of land area)"])]
df_agriculturalLandSelected = df_agriculturalLand.loc[df_agriculturalLand['Country Code'].isin(['HUN','BRA','IND','ARG','HRV','CHN'])]
df_agriculturalLand = df_agriculturalLandSelected.loc[:, ['Country Name','1965', '1975', '1985', '1995', '2005', '2015']].reset_index(drop=True)
years=['1965','1975','1985','1995','2005','2015']


#Choosing indicator (Agricultural land (% of land area)) and updating dataframe according to that
df_Co2emmission = df_Data.loc[df_Data['Indicator Name'].isin(["CO2 emissions from solid fuel consumption (% of total)"])]
df_Co2emmission = df_Co2emmission.loc[df_Co2emmission['Country Code'].isin(['HUN','BRA','IND','ARG','HRV','CHN'])]
Countries=['Hungary','Argentina','Brazil','China','Croatia','India']

#Choosing indicator (Agricultural land (% of land area)) and updating dataframe according to that
df_Arable = df_Data.loc[df_Data['Indicator Name'].isin(["Arable land (% of land area)"])]
df_Arable = df_Arable.loc[df_Arable['Country Code'].isin(['HUN','BRA','IND','ARG','HRV','CHN'])]
Countries=['Hungary','Argentina','Brazil','China','Croatia','India']

#Calling functions to plot the grpahs
barGraph(df_population,years,'Country','Population Percentage','Urban population (% of total population)')
barGraph(df_agriculturalLand,years,'Country','Agricultural land Area Percentage','Agricultural land (% of land area)')
linegraph(df_Co2emmission,Countries,'Year','CO2 Emission Percentage','CO2 emissions from solid fuel consumption (% of total)')
linegraph(df_Arable,Countries,'Year','Arable land Percentage','Arable land (% of land area)')











