import os
import pandas as pd

def load_data(url):

    df = pd.read_csv(url)
    
    return df
    

def export_data(df,datasetname):

    relative_path = os.path.join('datasets',f'{datasetname}.csv')
    
    df.to_csv(relative_path, index=False) 


def load_and_extract_data(url, datasetname):
    
    df = load_data(url)
    
    export_data(df, datasetname)

    return df






