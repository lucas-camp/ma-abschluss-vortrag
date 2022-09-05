import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import dct

TIKZ = True

# SORTED = True
SORTED = False

N = 8
# x = np.array([0.16820018,  0.04650225,  0.26155695, -0.18526645, -0.03249458,  0.18438391, -0.06760673,  0.22518145,  0.06334221])
x = np.array([-0.18526645, -0.06760673, 0.22518145, 0.26155695, -0.03249458,  0.04650225,  0.06334221, 0.16820018,  0.18438391])
x_sorted = np.sort(a=x)
c = dct(x=x, norm="ortho")
c_sorted = dct(x=x_sorted, norm="ortho")

if SORTED:
    plt.plot(x, marker="x", linestyle="--", label="$\mathbf{x}$")
    plt.plot(c, marker="x", linestyle="--", label="$\mathbf{c}$")
else:
    plt.plot(x_sorted, marker="x", linestyle="--", label="$\mathbf{x}$")
    plt.plot(c_sorted, marker="x", linestyle="--", label="$\mathbf{c}$")

plt.xlabel("$k$")
if SORTED:
    plt.ylabel("$x_k$; $c_k$")
else:
    plt.ylabel("$x_k$; $c_k$")
plt.legend(loc="lower right")

if TIKZ:
    import tikzplotlib
    if SORTED:
        tikzplotlib.save("grafiken/python/tikz/dct/example.tikz", axis_width="7cm")
    else:
        tikzplotlib.save("grafiken/python/tikz/dct/example_sorted.tikz", axis_width="7cm")
else:
    plt.show()
    z = 0
