import numpy as np
from matplotlib import pyplot as plt

TIKZ = True

def mex_hat(x, a, b):
    return 2/(np.sqrt(3*a)*np.pi**0.25) * (1 - ((x-b)/a)**2) * np.exp(-(x-b)**2/(2*a**2))

x = np.linspace(-10, 10, 250)

f1 = mex_hat(x, 1.0, 0)
f2 = mex_hat(x, 2, 5)
f3 = mex_hat(x, 0.5, -5)

plt.plot(x, f1, label="$\psi_{1; 0}$")
plt.plot(x, f2, label="$\psi_{2; -5}$")
plt.plot(x, f3, label="$\psi_{0{,}5; 5}$")

plt.xlabel("$t$")
plt.ylabel("$\psi_{a;b}(t)$")
plt.legend()

if TIKZ:
    import tikzplotlib
    tikzplotlib.save("grafiken/python/tikz/dwt/mexican_hat_3.tikz")
else:
    plt.show()
    z = 0