#Feature Importance

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


def feature_importance_plot(model, features, num=None, save=False):
    
    if num is None:
        
        num = len(features.columns)

    feature_imp = pd.DataFrame({'Value': model.feature_importances_, 'Feature': features.columns})
    
    print(feature_imp.sort_values("Value",ascending=False))
    
    plt.figure(figsize=(10, 10))
    
    sns.set(font_scale=1)
    
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value",
                                                                     ascending=False)[0:num])
    plt.title('Features')
    
    plt.tight_layout()
    
    plt.show()
    
    if save:
        
        plt.savefig('importances.png')