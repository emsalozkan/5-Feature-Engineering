#Feature Extraction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter(action="ignore")


# İnsulin Değeri ile Kategorik değişken türetmek
def set_insulin(dataframe, col_name="Insulin"):
    
    if 16 <= dataframe[col_name] <= 166:
        
        return "Normal"

    else:

        return "Abnormal"
    

# Yaş değişkenini kategorilere ayırıp yeni yaş değişkeni oluşturulması
def set_age(dataframe, col_name="Age"):

    if 21 <= dataframe[col_name] < 50:

        return "mature"
    
    else:

        return "senior"


# BMI 18,5 aşağısı underweight, 18.5 ile 24.9 arası normal, 24.9 ile 29.9 arası Overweight ve 30 üstü obez
def set_BMI(df, colname):
    
    bin_edges = [0, 18.5, 24.9, 29.9, 100]
    
    bin_labels = ["Underweight", "Healthy", "Overweight", "Obese"]
    
    df['NEW_BMI'] = pd.cut(x=df[colname], bins=bin_edges, labels=bin_labels)
    
    return df

# Glukoz degerini kategorik değişkene çevirme
def set_Glucose(df, colname):
    
    bin_edges = [0, 140, 200, 300]
    
    bin_labels = ["Normal", "Prediabetes", "Diabetes"]
    
    df['NEW_GLUCOSE'] = pd.cut(x=df[colname], bins=bin_edges, labels=bin_labels)
    
    return df


# # Yaş ve beden kitle indeksini bir arada düşünerek kategorik değişken oluşturma 3 kırılım yakalandı
def set_age_BMI(df, colname1="Age", colname2="BMI"):

    if (df[colname2] < 18.5) & ((df[colname1] >= 21) & (df[colname1] < 50)):

        return "underweightmature"

    elif (df[colname2] < 18.5) & (df[colname1] >= 50):
        
        return "underweightmature"

    elif ((df[colname2] >= 18.5) & (df[colname2] < 25)) & ((df[colname1] >= 21) & (df[colname1] < 50)):
        
        return "healthymature" 

    elif ((df[colname2] >= 18.5) & (df[colname2] < 25)) & (df[colname1] >= 50):
        
        return "healthysenior"   

    elif ((df[colname2] >= 25) & (df[colname2] < 30)) & ((df[colname1] >= 21) & (df[colname1] < 50)):
        
        return "overweightmature" 

    elif ((df[colname2] >= 25) & (df[colname2] < 30)) & (df[colname1] >= 50):
        
        return "overweightsenior" 

    elif (df[colname2] > 18.5) & ((df[colname1] >= 21) & (df[colname1] < 50)) :
        
        return "obesemature" 
    
    elif (df[colname2] > 18.5) & (df[colname1] >= 50):
        
        return "obesesenior" 


# Yaş ve Glikoz değerlerini bir arada düşünerek kategorik değişken oluşturma
def set_age_Glucose(df, colname1="Age", colname2="Glucose"):

    if (df[colname2] < 70) & ((df[colname1] >= 21) & (df[colname1] < 50)):

        return "lowmature"

    elif (df[colname2] < 70) & (df[colname1] >= 50):

        return "lowsenior"

    elif (df[colname2] < 70) & (df[colname1] >= 50):

        return "lowsenior"

    elif ((df[colname2] >= 70) & (df[colname2] < 100)) & ((df[colname1] >= 21) & (df[colname1] < 50)):

        return "normalmature"

    elif ((df[colname2] >= 70) & (df[colname2] < 100)) & (df[colname1] >= 50):

        return "normalsenior"
    
    elif ((df[colname2] >= 100) & (df[colname2] <= 125)) & ((df[colname1] >= 21) & (df[colname1] < 50)):

        return "hiddenmature"

    elif ((df[colname2] >= 100) & (df[colname2] <= 125)) & (df[colname1] >= 50):

        return "hiddensenior"

    elif (df[colname2] > 125) & ((df[colname1] >= 21) & (df[colname1] < 50)):

        return "highmature"

    elif (df[colname2] > 125) & (df[colname1] >= 50):

        return "highsenior"


