# imports
import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
plt.style.use('ggplot')

class VisualizeDataframe: 
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def plot_multiple_histograms(self, df: pd.DataFrame, cols:list) -> None:
        num_plots = len(cols)
        num_cols = 4
        num_rows = math.ceil(num_plots/num_cols)
        
        fig, axs = plt.subplots(num_rows, num_cols, figsize=(18, 30))
        fig.tight_layout()
        
        for ind, col in enumerate(cols):
            i = math.floor(ind/num_cols)
            j = ind - i*num_cols
                
            if num_rows == 1:
                if num_cols == 1:
                    sns.distplot(df[col], kde=True, ax=axs)
                else:
                    sns.distplot(df[col], kde=True, ax=axs[j])
            else:
                sns.distplot(df[col], kde=True, ax=axs[i, j])
        
    def plot_count(self, df:pd.DataFrame, column:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()

    def plot_bar(self, df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
        plt.figure(figsize=(12, 7))
        sns.barplot(data = df, x=x_col, y=y_col)
        plt.title(title, size=20, fontweight='bold')
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks( fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.show() 

    def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data = df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks( fontsize=14)
        plt.show() 