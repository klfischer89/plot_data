import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./data/diamonds.csv.bz2") # read csv

df = df.sample(500, random_state = 42) # sample of dataframe with 500 datasets with consistent state

print(df.head()) # print head of dataframe

# df_color = df.groupby("color").agg(count=("cut", len)) # group by color and count by cut

# sns.set_theme()
# ax = sns.barplot(x = df_color.index, y = df_color["count"]) # barplot that counts the colors

# df_grouped = df\
#     .groupby(["cut", "color"])\
#     .agg(avgP = ("price", "mean"))\
#     .reset_index() # group by cut and color considering the average price, and convert cut and color from index to columns and set a new ascending index

# df_color = df.groupby("color").agg(count=("cut", len)) # group by color counted by length of cut

# sns.set_theme() # set theme to seaborn

# sns.barplot(x = df_grouped["cut"],
#             y = df_grouped["avgP"],
#             hue = df_grouped["color"]) # showing barplot showing cut with avarage price, and colored bars'

df_grouped = df\
    .groupby("color")\
    .agg(avgX = ("x", "mean"), avgY = ("y", "mean"), avgZ = ("z", "mean"))\
    .reset_index()\
    .melt(id_vars = ["color"]) # use color as index and make avgX,Y,Z to one column variable and one column value

sns.barplot(x = df_grouped["color"], y = df_grouped["value"], hue = df_grouped["variable"]) # create bar plot showing three bars for color/value

plt.show() # show bars