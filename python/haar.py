from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-1, 2, 250)

a = 1.0
b = 0

f = 2/(np.sqrt(3*a)*np.pi**0.25) * (1 - ((x-b)/a)**2) * np.exp(-(x-b)**2/(2*a**2))
f = np.piecewise(x, [x < 0, x>=1, np.logical_and(0<=x, x<0.5), np.logical_and(0.5<=x, x<1)], [0, 0, 1, -1])

plt.plot(x, f)

plt.xlabel("$t$")
plt.ylabel("$\psi(t)$")
plt.legend()

import tikzplotlib
# plt.show()
tikzplotlib.save("tikz/haar.tex")