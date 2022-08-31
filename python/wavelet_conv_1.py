from matplotlib import pyplot as plt
import numpy as np

def mex_hat(x, a, b):
    return 2/(np.sqrt(3*a)*np.pi**0.25) * (1 - ((x-b)/a)**2) * np.exp(-(x-b)**2/(2*a**2))

def sin(x, a, b, c):
    return a*np.sin(np.pi*b*(x-c))

x = np.linspace(-10, 10, 250)

w_a_1 = 0.7
w_b_1 = -7
w_1 = mex_hat(x, w_a_1, w_b_1)

w_a_2 = 0.7
w_b_2 = 5
w_2 = mex_hat(x, w_a_2, w_b_2)

s_a_1 = 0.7
s_b_1 = 0.5
s_c_1 = 0
s_1 = sin(x, s_a_1, s_b_1, s_c_1)

s_a_2 = 0.3
s_b_2 = 0.2
s_c_2 = -1.2
s_2 = sin(x, s_a_2, s_b_2, s_c_2)

s_a_3 = 0.2
s_b_3 = 0.7
s_c_3 = 0.4
s_3 = sin(x, s_a_3, s_b_3, s_c_3)

s = s_1 + s_2 + s_3

plt.plot(x, s, label="$x(t)$")
plt.plot(x, w_1, label="$\psi_{0{,}7; -7}(t)$", color="red")
plt.plot(x, w_2, "--", color="red", label="$\psi_{0{,}7; 5}(t)$")

plt.xlabel("$t$")
plt.ylabel("$\psi_{a;b}(t)$")
plt.legend(loc="upper center")

import tikzplotlib
# plt.show()
tikzplotlib.save("tikz/wavelet_conv_1.tex")