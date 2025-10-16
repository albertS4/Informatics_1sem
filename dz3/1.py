import matplotlib.pyplot as plt
import numpy as np

v20a = [200,252,308,372,404,504,592]
v20b = [532,476,404,324,220]
i20a = [98.5,122.3,151.3,182.6,196.4,247.3,289.4]
i20b = [257.1,231.6,196.3,157.3,107.8]

v30a = [220,284,364,420,480,580]
v30b = [540,480,404,344,284,220]
i30a = [70.4,90.6,116.3,134.8,154.9,185.4]
i30b = [172.9,153.6,128.8,110.2,90.5,70.5]

v50a = [340,380,420,480,536,600]
v50b = [560,500,440,400,360,340]

i50a = [66.3,74.2,81.6,93.3,104.6,116.5]
i50b = [108.9,97.0,86.0,78.1,70.1,66.3]

fig, ax = plt.subplots()
ax.axline((0, 0), slope=2.050837776, color="black", linestyle="-", linewidth = 0.3)
ax.axline((0, 0), slope=3.123217956, color="black", linestyle="-", linewidth = 0.3)
ax.axline((0, 0), slope=5.13684407, color="black", linestyle="-", linewidth = 0.3)
ax.set(xlim=(0, 300), ylim = (0, 650), xlabel='I, мА', ylabel = 'V, мВ')
#ax.legend(fontsize=14)
#ax.plot(i20a, v20a,  marker='o', markersize=10, markerfacecolor='green', markeredgecolor='black', linewidth = 0)
ax.plot(i20a, v20a,  marker='+', linewidth = 0, color = "black")
ax.plot(i20b, v20b,  marker='o', linewidth = 0, markerfacecolor='none', color = "black")
ax.plot(i30a, v30a, marker='+', linewidth = 0, color = "black")
ax.plot(i30b, v30b, marker='o', linewidth = 0, markerfacecolor='none', color = "black")
ax.plot(i50a, v50a, marker='+', linewidth = 0, color = "black")
ax.plot(i50b, v50b, marker='o', linewidth = 0, markerfacecolor='none', color = "black")

plt.text(141, 287, r'$l$ = 20 см', fontsize=12, horizontalalignment = "left", verticalalignment = "top")
plt.text(143, 442, r'30', fontsize=12, horizontalalignment = "left", verticalalignment = "top")
plt.text(117, 573, r'50', fontsize=12, horizontalalignment = "left", verticalalignment = "top")
plt.show()
