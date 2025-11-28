import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./data/diamonds.csv.bz2") # read csv

df = df.sample(500, random_state = 42) # sample of dataframe with 500 datasets with consistent state

print(df.head()) # print head of dataframe

sns.set_theme() # make plot have the seaborn theme
sns.scatterplot(x = df["carat"], y = df["price"]) # create scatterplot
plt.show() # show the plo