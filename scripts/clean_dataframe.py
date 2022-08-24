import pandas as pd
import numpy as np

class Clean_DataFrame:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        print('initializing dataframe')
    
    #handling missing values
    # how many missing values exist or better still what is the % of missing values in the dataset?
    def precent_missing(self, df: pd.DataFrame) -> None:
        totalCells = np.product(df.shape)
        missingCount = df.isnull().sum()

        totalMissing = missingCount.sum()
        # calculate percentage of missing values
        print('The telecom dataset contains', round(((totalMissing/totalCells) * 100 ),2), '%', 'missing values.')
    
    def missing_precentage_of_each_col(self, df: pd.DataFrame):
        return round(100*(df.isnull().sum(axis=0)/len(df.index)), 2).sort_values(ascending = False) 
    
    # fill missing with ffill method for columns

    def fix_missing_ffill(df, col):
        df[col] = df[col].fillna(method='ffill')
    
    def convert_bytes_to_megabytes(self, df:pd.DataFrame, bytes_data):
        """
            This function takes the dataframe and the column which has the bytes values
            returns the megabytesof that value
            
            Args:
            -----
            df: dataframe
            bytes_data: column with bytes values
            
            Returns:
            --------
            A series
        """
        megabyte = 1*10e+5
        df[bytes_data] = df[bytes_data] / megabyte
        return df[bytes_data]

    def fix_outlier(self, df, column):
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
        
        return df[column]
    
    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        # convert datetime column to datetime
        self.df['Start'] = pd.to_datetime(self.df['Start'], errors='coerce')
        self.df['End'] = pd.to_datetime(self.df['End'], errors='coerce')
        return self.df

    def fill_by_mean(self, df: pd.DataFrame, cols: list) -> pd.DataFrame:
        self.df[cols] =  df[cols].fillna(df[cols].mean())
        return self.df
    
    def fill_by_median(self, df: pd.DataFrame, cols: list) -> pd.DataFrame:
        self.df[cols] =  df[cols].fillna(df[cols].median())
        return self.df
    
    def fill_by_mode(self, df: pd.DataFrame, cols: list) -> pd.DataFrame:
        self.df[cols] =  df[cols].fillna(df[cols].mode())
        return self.df