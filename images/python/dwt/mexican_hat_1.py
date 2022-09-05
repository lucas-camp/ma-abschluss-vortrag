import numpy as np
from matplotlib import pyplot as plt

TIKZ = True

x = np.linspace(-10, 10, 250)

a = 1.0
b = 0

f = 2/(np.sqrt(3*a)*np.pi**0.25) * (1 - ((x-b)/a)**2) * np.exp(-(x-b)**2/(2*a**2))

plt.plot(x, f)

plt.xlabel("$t$")
plt.ylabel("$\psi_{1;0}(t)$")
plt.legend()

if TIKZ:
    import tikzplotlib
    tikzplotlib.save("grafiken/python/tikz/dwt/mexican_hat_1.tikz")
else:
    plt.show()
    z = 0