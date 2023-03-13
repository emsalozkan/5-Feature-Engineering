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
def set_BMI(dataframe, col_name="BMI"):

    bin_edges = [0, 18.5, 24.9, 29.9, 100],
    bin_labels = ["Underweight", "Healthy", "Overweight", "Obese"]

    # apply the cut function to the "Height (cm)" column and create a new column "Height Category"
    dataframe['NEW_BMI'] = dataframe[col_name].apply(lambda x: pd.cut(x, bins=bin_edges, labels=bin_labels))

    return dataframe

