import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./data/diamonds.csv.bz2") # read csv

df = df.sample(500, random_state = 42) # sample of dataframe with 500 datasets with consistent state

print(df.head()) # print head of dataframe

sns.set_theme() # set theme to seaborn

sns.histplot(data = df, x = "price", binwidth = 2500, binrange = (0, df["price"].max())) # create histogram with bin width and range
plt.show() # show plot