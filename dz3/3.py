import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris_data.csv")
#print(df.head())

fig = plt.figure(figsize = (16, 9), dpi = 100)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#print(set(df["Species"]))
#{'Iris-versicolor', 'Iris-virginica', 'Iris-setosa'}
#print(df[df["SepalLengthCm"] > 5].count())

ax1.set_title("Распределение по видам")
ax1.pie([len(df[df["Species"] == "Iris-versicolor"]), len(df[df["Species"] == "Iris-virginica"]), len(df[df["Species"] == "Iris-setosa"])], labels = ['Iris-versicolor', 'Iris-virginica', 'Iris-setosa'])
ax2.set_title("Распределение по длине лепестков")
ax2.pie([len(df[df["PetalLengthCm"] < 1.2]), len(df[(df["PetalLengthCm"] > 1.2) & (df["PetalLengthCm"] < 1.5)]), len(df[df["PetalLengthCm"] > 1.5])], labels = ["< 1.2 см", "> 1.2 см и < 1.5 см", "> 1.5 см"])

plt.savefig("3.png")
plt.show()
