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
    The linegraph function is used to plot line grpah.
    The plot represents the total percentage of Co2 emissions from solid fuel consumption
    percentage and the Arable land Percentage in each selected contries   
    """
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


def piegraph(df):
    
    """
    The piegraph function is used to plot pie chart. 
    The pie graph represents the mean of population growth in each selected
    countries.
    """ 
    plt.figure()
    df.groupby(['Country Name']).sum().plot(
    kind='pie', y='Population', autopct='%1.0f%%',startangle=180)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=6)
    plt.title('Mean population growth')
    plt.show()

#A function to create a dataframe with average of population growth in each country
def FindAverage(df):
    
    """
    The FindAverage function is used to find the mean of population growth
    in each countries.
    """
    Countries = df["Country Name"]
    for c in Countries:
        df['Population']=df.mean(axis=1)
    df=df.loc[:, ['Country Name','Population']].reset_index(drop=True)
    print(df)
    piegraph(df)

#reading the data set 
def ReadandReturnData(filename,indicatorName):
    
    """
    The ReadandReturnData function is used to read the filename and 
    indicator name to return two dataframe df1 and df2, one with 
    countries as column(df1) and the other with years as column(df2).
    """
    Data = pd.read_csv(filename,sep='\t',skiprows=4,engine='python')
    df_Data = pd.DataFrame(Data)
    df1= df_Data.loc[df_Data['Indicator Name'].isin([indicatorName])]
    df1 = df1.loc[df1['Country Code'].isin(['CUB','BRA','IND','ARG','DZA','CHN'])]
    df1 = df1.loc[:, ['Country Name','1965', '1975', '1985', '1995', '2005', '2015']].reset_index(drop=True).fillna(0.0)
    df2=df1.set_index('Country Name').transpose()
    df2['Years'] = df2.index
    temp_cols=df2.columns.tolist()
    new_cols=temp_cols[-1:] + temp_cols[:-1]
    df2=df2[new_cols]
    df2=df2.reset_index(drop=True)
    df2= df2.rename_axis(None, axis=1)
    return df1,df2    


#reading data set
filename = "Dataset.csv"
years=['1965','1975','1985','1995','2005','2015']
Countries=['Cuba','Argentina','Brazil','China','Algeria','India']

#Calling function to create dataframe according to the indicators
df_urbanPopulation,df_urbanPopTrans=ReadandReturnData(filename,"Urban population (% of total population)")
df_AgriculturalLand,df_AgriculturalLandTrans=ReadandReturnData(filename,"Agricultural land (% of land area)")
df_CO2Emissions,df_CO2EmissionsTrans=ReadandReturnData(filename,"CO2 emissions from solid fuel consumption (% of total)")
df_ArableLand,df_ArableLandTrans=ReadandReturnData(filename,"Arable land (% of land area)")
df_Population,df_PopulationTrans=ReadandReturnData(filename,"Population growth (annual %)")

#Calling functions to plot the grpahs
barGraph(df_urbanPopulation,years,'Country','Population Percentage','Urban population (% of total population)')
barGraph(df_AgriculturalLand,years,'Country','Agricultural land Area Percentage','Agricultural land (% of land area)')
linegraph(df_CO2EmissionsTrans,Countries,'Year','CO2 Emission Percentage','CO2 emissions from solid fuel consumption (% of total)')
linegraph(df_ArableLandTrans,Countries,'Year','Arable land Percentage','Arable land (% of land area)')

#Calling function find the mean of population growth
FindAverage(df_Population)







