import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./data/diamonds.csv.bz2")

df = df.sample(500, random_state = 42)

print(df.head())

sns.set_theme()
sns.scatterplot(x = df["carat"], y = df["price"])
plt.show()