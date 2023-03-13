#Analyze numeric and categorical variables, target variable, missing values.

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

#3. Analyze numeric and categorical variables.
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

#4. Analyze target variable.
def target_summary_with_num(dataframe, target, numerical_col): #for numerical variables

    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


def target_summary_with_cat(dataframe, target, categorical_col): #for categoric variables

    print(pd.DataFrame({"OUTCOME_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")

#5. Analyze missing values.

def missing_value(dataframe, na_name=False):

    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]

    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)

    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)

    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])

    print(missing_df, end="\n")

    if na_name:

        return na_columns

def missing_value_and_target(dataframe, target, na_columns):

    temp_df = dataframe.copy()

    for col in na_columns:

        temp_df[col + '_NA_FLAG'] = np.where(temp_df[col].isnull(), 1, 0)

    na_flags = temp_df.loc[:, temp_df.columns.str.contains("_NA_")].columns#bütün satırları seç ama içinde NA geçen sütunları getir.

    for col in na_flags:

        print(pd.DataFrame({"TARGET_MEAN": temp_df.groupby(col)[target].mean(),
                            "Count": temp_df.groupby(col)[target].count()}), end="\n\n\n")

#6. Analyze outliers.

def outlier_thr(dataframe, col_name, q1=0.05, q3=0.95): #üst limit alt limit belirlenir

    quartile1 = dataframe[col_name].quantile(q1)

    quartile3 = dataframe[col_name].quantile(q3)

    interquantile_range = quartile3 - quartile1

    up_limit = quartile3 + 1.5 * interquantile_range

    low_limit = quartile1 - 1.5 * interquantile_range

    return low_limit, up_limit

def check_outlier(dataframe, col_name): #outlier olup olmadığının kontrolü yapılır

    low_limit, up_limit = outlier_thr(dataframe, col_name)

    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):

        return True

    else:

        return False

#BASKILAMA YÖNTEMİ ile aykırı değerler üst limit ve alt limit değerleri ile güncellenir.
def replace_with_thresholds(dataframe, variable, q1=0.05, q3=0.95):

    low_limit, up_limit = outlier_thr(dataframe, variable, q1=0.05, q3=0.95)

    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit

    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

def corr_variable(dataframe):

    sns.set(rc={'figure.figsize': (12, 12)})

    sns.heatmap(dataframe.corr(),annot=True, fmt=".2f", cmap="RdBu")

    plt.show()


