import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./data/diamonds.csv.bz2") # read csv

df = df.sample(500, random_state = 42) # sample of dataframe with 500 datasets with consistent state

print(df.head()) # print head of dataframe

sns.set_theme() # make plot have the seaborn theme
sns.scatterplot(data = df,
                x = "carat", 
                y = "price", 
                hue = "cut",
                s = 150,
                palette = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff"],
                style = "cut", 
                style_order = ["Fair", "Good", "Very Good", "Premium", "Ideal"],
                markers = ["o", "v", "8", "X", "*"])# create scatterplot
plt.show() # show the plot