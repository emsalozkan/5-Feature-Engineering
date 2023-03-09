#Examine the overall picture.

import os
import sys
import numpy as np
import pandas as pd
import seaborn as sns

def check_df(df, head=5):
    print("##################### Shape #####################")
    print(df.shape)
    print("##################### Types #####################")
    print(df.dtypes)
    print("##################### Head #####################")
    print(df.head(head))
    print("##################### Tail #####################")
    print(df.tail(head))
    print("##################### NA #####################")
    print(df.isnull().sum())
    print("##################### Quantiles #####################")  #Quantiles
    print(df.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)