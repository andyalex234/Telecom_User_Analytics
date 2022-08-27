import pandas as pd
import numpy as np

class Utility:

    def  __init__(self) -> None:
        pass

    def fix_outlier(self, df: pd.DataFrame, column:str) -> pd.Series:
        print(f'column to be filled with median values: {column}')
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
    
        return df[column]
