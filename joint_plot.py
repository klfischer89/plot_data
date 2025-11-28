import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./data/diamonds.csv.bz2") # read csv

sns.jointplot(x = df["carat"], y = df["price"], kind = "hex", xlim = (0, 3), ylim = (0, 15000), gridsize = 15, color = "k")
# joint plot showing relation from carat to price, using hexagons, the darker the more diamonds, kind makes easier handling for lots of data
# x is limited from 0 to 3 carat and y is limited to a price of 150000, size for grids increased and color changed for better visibility,
# k is for black and white

plt.show() # show plot