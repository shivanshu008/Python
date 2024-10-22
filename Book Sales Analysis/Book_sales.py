import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/shivanshu gaurav/OneDrive/Desktop/Programs/Python/Book Sales Analysis/best-selling-books.csv')
print(df.head())
print(df.info())
print(df.describe())
df.fillna(0, inplace=True)
