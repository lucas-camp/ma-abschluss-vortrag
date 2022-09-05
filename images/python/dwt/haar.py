import numpy as np
from matplotlib import pyplot as plt
import pywt

TIKZ = True

WAVELET = "db2"

wavelet = pywt.Wavelet(WAVELET)
[phi, psi, x] = wavelet.wavefun(level=10)

# wavelet function
plt.plot(x, psi)

if TIKZ:
    import tikzplotlib
    tikzplotlib.save(f"grafiken/python/tikz/dwt/{WAVELET}_wavelet.tikz", axis_width="7cm")
    plt.close()
else:
    plt.show()
    z = 0

# scaling function
plt.plot(x, phi)

if TIKZ:
    import tikzplotlib
    tikzplotlib.save(f"grafiken/python/tikz/dwt/{WAVELET}_scaling.tikz", axis_width="7cm")
    plt.close()
else:
    plt.show()
    z = 0