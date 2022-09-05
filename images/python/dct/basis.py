import numpy as np
from matplotlib import pyplot as plt

TIKZ = True

N = 8
x = np.linspace(0, N, 1000)

d0 = 1.0/np.sqrt(N) * np.cos(np.pi/N*0*(x+0.5))
d1 = 2.0/np.sqrt(N) * np.cos(np.pi/N*1*(x+0.5))
d2 = 2.0/np.sqrt(N) * np.cos(np.pi/N*2*(x+0.5))
d3 = 2.0/np.sqrt(N) * np.cos(np.pi/N*3*(x+0.5))

plt.plot(x, d0, label="$\mathcal{C}_0$")
plt.plot(x, d1, label="$\mathcal{C}_1$")
plt.plot(x, d2, label="$\mathcal{C}_2$")
plt.plot(x, d3, label="$\mathcal{C}_3$")

plt.xlabel("$x$")
plt.ylabel("$\mathcal{C}_k(x)$")
plt.legend()

if TIKZ:
    import tikzplotlib
    tikzplotlib.save("tikz/dct/basis.tex")
else:
    plt.show()
    z = 0