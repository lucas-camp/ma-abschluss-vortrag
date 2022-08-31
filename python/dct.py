import numpy as np
from matplotlib import pyplot as plt

N = 8
x = np.linspace(0, N, 1000)

d0 = np.cos(np.pi/N*0*(x+0.5))
d1 = np.cos(np.pi/N*1*(x+0.5))
d2 = np.cos(np.pi/N*2*(x+0.5))
d3 = np.cos(np.pi/N*3*(x+0.5))

plt.plot(x, d0, label="$d_0$")
plt.plot(x, d1, label="$d_1$")
plt.plot(x, d2, label="$d_2$")
plt.plot(x, d3, label="$d_3$")

plt.xlabel("$x$")
plt.ylabel("$d_k(x)$")
plt.legend()

import tikzplotlib

tikzplotlib.save("tikz/dct_basis.tex")