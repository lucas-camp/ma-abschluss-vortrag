import imp
from matplotlib import pyplot as plt
import numpy as np

s = 1.0

x = s*0
y = s*-1

a_1 = 2./3. * np.pi
a_2 = 4./3. * np.pi
a_3 = 1./3. * np.pi
a_4 = 1./2. * np.pi

mu_1 = np.array([x*np.cos(a_1) - y*np.sin(a_1), x*np.sin(a_1) + y*np.cos(a_1)])
mu_2 = np.array([x*np.cos(a_2) - y*np.sin(a_2), x*np.sin(a_2) + y*np.cos(a_2)])
mu_3 = np.array([x, y])
cov = np.array([[0.08, 0.0], [0.0, 0.08]])

plt.plot(mu_1[0], mu_1[1], marker="x", color="black", markersize=15, markeredgewidth=5)
plt.plot(mu_2[0], mu_2[1], marker="x", color="black", markersize=15, markeredgewidth=5)
plt.plot(mu_3[0], mu_3[1], marker="x", color="black", markersize=15, markeredgewidth=5)

e_1 = np.array([0, 1.5])
e_2 = np.array([0*np.cos(a_1) - 1.5*np.sin(a_1), 0*np.sin(a_1) + 1.5*np.cos(a_1)])
e_3 = np.array([0*np.cos(a_2) - 1.5*np.sin(a_2), 0*np.sin(a_2) + 1.5*np.cos(a_2)])

plt.plot([0, e_1[0]], [0, e_1[1]], color="black")
plt.plot([0, e_2[0]], [0, e_2[1]], color="black")
plt.plot([0, e_3[0]], [0, e_3[1]], color="black")

x_1, y_1 = np.random.multivariate_normal(mu_1, cov, size=20).T
x_2, y_2 = np.random.multivariate_normal(mu_2, cov, size=20).T
x_3, y_3 = np.random.multivariate_normal(mu_3, cov, size=20).T

plt.plot(x_1, y_1, color="blue", marker="x", linestyle='None')
plt.plot(x_2, y_2, color="red", marker="x", linestyle='None')
plt.plot(x_3, y_3, color="green", marker="x", linestyle='None')

plt.xlim(-2, 2)
plt.ylim(-2, 2)

import tikzplotlib
# plt.show()
tikzplotlib.save("tikz/k_means.tex")