from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 250)

a = 1.0
b = 0

f = 2/(np.sqrt(3*a)*np.pi**0.25) * (1 - ((x-b)/a)**2) * np.exp(-(x-b)**2/(2*a**2))

plt.plot(x, f)

plt.xlabel("$t$")
plt.ylabel("$\psi_{1;0}(t)$")
plt.legend()

import tikzplotlib

tikzplotlib.save("tikz/mexican_hat.tex")