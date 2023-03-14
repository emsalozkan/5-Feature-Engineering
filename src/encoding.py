#Encoding

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


#Eğer bir kategorik değişkenin 2 sınıfı varsa ve bu 1-0 olarak kodlanırsa buna binary encoding denir. 
#2 den fazla sınıfı varsa ve sınıflar arasında ordinallik var ise label encodingtir. Label encoding>Binary encoding


def label_encoding(dataframe, binary_col):

    labelencoder = LabelEncoder()

    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    
    return dataframe

def one_hot_encoding(dataframe, categorical_cols, drop_first=False):
    
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    
    return dataframe