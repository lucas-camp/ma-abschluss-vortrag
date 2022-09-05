import numpy as np
from matplotlib import pyplot as plt

TIKZ = False

N = 8
x = np.array([0.1, -0.9, 0.3, 0.8, 0.6, 0.6, -0.9, -0.8, 0.5, 0.9, -0.5, -0.6, 0.3, -0.7, 0.7, 0.9])

plt.plot(x, "o", label="$\mathcal{C}_0$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()

if TIKZ:
    import tikzplotlib
    tikzplotlib.save("tikz/dct/basis.tex")
else:
    plt.show()
    z = 0