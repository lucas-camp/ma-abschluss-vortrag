from matplotlib import pyplot as plt
import numpy as np

def mex_hat(x, a, b):
    return 2/(np.sqrt(3*a)*np.pi**0.25) * (1 - ((x-b)/a)**2) * np.exp(-(x-b)**2/(2*a**2))

x = np.linspace(-10, 10, 250)

a = 1.0
b = 0

f1 = mex_hat(x, 1.0, 0)
f2 = mex_hat(x, 2, 5)
f3 = mex_hat(x, 0.5, -5)

plt.plot(x, f1, label="$\psi_{1; 0}$")
plt.plot(x, f2, label="$\psi_{2; -5}$")
plt.plot(x, f3, label="$\psi_{0{,}5; 5}$")

plt.xlabel("$t$")
plt.ylabel("$\psi_{a;b}(t)$")
plt.legend()

import tikzplotlib
# plt.show()
tikzplotlib.save("tikz/mexican_hat_2.tex")