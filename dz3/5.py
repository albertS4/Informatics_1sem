import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BTC_data.csv")
#print(df.head())

fig = plt.figure(figsize = (16, 9), dpi = 100)
ax1 = fig.add_subplot(111)

#print(set(df["Species"]))
#{'Iris-versicolor', 'Iris-virginica', 'Iris-setosa'}
#print(df[df["SepalLengthCm"] > 5].count())

ax1.set_title("Цена на биткоин")
data = list(map((lambda s: s[8:10] + "-" + s[5:7] + "-" + s[0:4]),list(df["time"])))
ax1.plot(range(len(data)), df["close"])
print(len(data))
ax1.set_xticks(ticks = list(range(0, len(data), 120)), labels = data[::120])

plt.savefig("5.png")
plt.show()
