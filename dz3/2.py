import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (16, 8), dpi = 100)

#Xs = np.arange(-4, 4, 0.001)
#Ys = (2 * 3.14)**(-0.5)*np.exp(-0.5*Xs*Xs)

r1 = np.random.normal(0, 1, 500)
print(len(r1))
r2 = np.random.normal(0, 1, 1000)
r3 = np.random.normal(0, 1, 5000)
r4 = np.random.normal(0, 1, 50000)

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.set_xlim(-4, 4)
ax2.set_xlim(-4, 4)
ax3.set_xlim(-4, 4)
ax4.set_xlim(-4, 4)

ax1.hist(r1, bins = 100)
#ax1.plot(Xs, 500*Ys)
ax2.hist(r2, bins = 100)
#ax2.plot(Xs, 1000*Ys)
ax3.hist(r3, bins = 100)
#ax3.plot(Xs, 5000*Ys)
ax4.hist(r4, bins = 100)
#ax4.plot(Xs, 50000*Ys)

plt.savefig("2.png", dpi = 100)

plt.show()
