import os
import pandas as pd


def load_data(url):

    df = pd.read_csv(url)
    return df

def export_data(df,path):

    df.to_csv(path, index=False)

def load_and_extract_data(url,path):

    df = load_data(url)
    export_data(df,path)

    return df






