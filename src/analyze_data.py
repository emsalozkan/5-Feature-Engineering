#Analyze numeric and categorical variables.

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def cat_summary(dataframe, col_name, plot=False):
    
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    
    print("##########################################")
    
    if plot:
        
        sns.countplot(x=dataframe[col_name], data=dataframe)
        
        plt.show()


def num_summary(dataframe, numerical_col, plot=False):
    
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        
        dataframe[numerical_col].hist(bins=20)
        
        plt.xlabel(numerical_col)
        
        plt.title(numerical_col)
        
        plt.show()


def target_summary_with_num(dataframe, target, numerical_col): #for numerical variables

    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")