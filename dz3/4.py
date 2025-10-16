import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools

def LS(x, y):
    k = (np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x*x) - np.mean(x)**2)
    b = np.mean(y) - k*np.mean(x)
    return (k, b)

df = pd.read_csv("iris_data.csv")

fig = plt.figure(figsize=(16, 9), dpi = 100)
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

print("Результаты МНК")
axs = [ax1, ax2, ax3, ax4, ax5, ax6]
##{'Iris-versicolor', 'Iris-virginica', 'Iris-setosa'}
for e in zip(axs, itertools.combinations(["SepalLengthCm",  "SepalWidthCm",  "PetalLengthCm",  "PetalWidthCm"], 2)):
    e[0].set_xlabel(e[1][0])
    e[0].set_ylabel(e[1][1])
    for a in [["Iris-versicolor", "magenta"], ["Iris-virginica", "cyan"], ["Iris-setosa", "yellow"]]:
        Xs = df[df["Species"] == a[0]][e[1][0]].to_numpy()
        Ys = df[df["Species"] == a[0]][e[1][1]].to_numpy()
        e[0].scatter(Xs, Ys, color = a[1], s = 5)
        k, b = LS(Xs, Ys)
        e[0].axline((0, b), slope = k, color = a[1], alpha = 0.23, linewidth = 1.5)
        print("{}({})".format(e[1][1], e[1][0]), a[0], "k = {}, b = {}".format(k, b))


#print(set(df["Species"]))
#{'Iris-versicolor', 'Iris-virginica', 'Iris-setosa'}
#print(df[df["SepalLengthCm"] > 5].count())

plt.savefig("4.png")
plt.show()
