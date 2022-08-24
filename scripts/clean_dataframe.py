import pandas as pd
import numpy as np

class Clean_DataFrame:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        print('initializing dataframe')
    
    #handling missing values
    # how many missing values exist or better still what is the % of missing values in the dataset?
    def precent_missing(self):
        totalCells = np.product(self.df.shape)
        missingCount = self.df.isnull().sum()

        totalMissing = missingCount.sum()
        # calculate percentage of missing values
        print('The telecom dataset contains', round(((totalMissing/totalCells) * 100 ),2), '%', 'missing values.')
    
    def missing_precentage_of_each_col(self):
        return round(100*(self.df.isnull().sum(axis=0)/len(self.df.index)), 2).sort_values(ascending = False) 
