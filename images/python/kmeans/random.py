from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

TIKZ = True
RANDOM = False
PLOT_CENTERS = False

SEED = 9001

np.random.seed(SEED)

s = 2.0

LIM = 3.5

x = s*0
y = s*-1

a_1 = 2./3. * np.pi
a_2 = 4./3. * np.pi
a_3 = 1./3. * np.pi
a_4 = 1./2. * np.pi

mu_1 = np.array([x*np.cos(a_1) - y*np.sin(a_1), x*np.sin(a_1) + y*np.cos(a_1)])
mu_2 = np.array([x*np.cos(a_2) - y*np.sin(a_2), x*np.sin(a_2) + y*np.cos(a_2)])
mu_3 = np.array([x, y])
cov = np.array([[0.15, 0.0], [0.0, 0.15]])

# plt.plot(mu_1[0], mu_1[1], marker="x", color="black", markersize=15, markeredgewidth=5)
# plt.plot(mu_2[0], mu_2[1], marker="x", color="black", markersize=15, markeredgewidth=5)
# plt.plot(mu_3[0], mu_3[1], marker="x", color="black", markersize=15, markeredgewidth=5)

# e_1 = np.array([0, 1.5])
# e_2 = np.array([0*np.cos(a_1) - 1.5*np.sin(a_1), 0*np.sin(a_1) + 1.5*np.cos(a_1)])
# e_3 = np.array([0*np.cos(a_2) - 1.5*np.sin(a_2), 0*np.sin(a_2) + 1.5*np.cos(a_2)])

# plt.plot([0, e_1[0]], [0, e_1[1]], color="black")
# plt.plot([0, e_2[0]], [0, e_2[1]], color="black")
# plt.plot([0, e_3[0]], [0, e_3[1]], color="black")

d_1 = np.random.multivariate_normal(mu_1, cov, size=20)
d_2 = np.random.multivariate_normal(mu_2, cov, size=20)
d_3 = np.random.multivariate_normal(mu_3, cov, size=20)

d = np.vstack((d_1, d_2, d_3))

if RANDOM:
    i=np.vstack((d_1[0,:], d_1[3,:], d_2[4,:]))

    k_means = KMeans(n_clusters=3, init=i, random_state=SEED).fit(d)
else:
    k_means = KMeans(n_clusters=3, init="k-means++", random_state=SEED).fit(d)

c_0 = d[np.where(k_means.labels_ == 0)]
c_1 = d[np.where(k_means.labels_ == 1)]
c_2 = d[np.where(k_means.labels_ == 2)]

plt.plot(c_0[:, 0], c_0[:, 1], color="blue", marker="x", linestyle='None')
plt.plot(c_1[:, 0], c_1[:, 1], color="red", marker="x", linestyle='None')
plt.plot(c_2[:, 0], c_2[:, 1], color="green", marker="x", linestyle='None')

if PLOT_CENTERS:
    plt.plot(k_means.cluster_centers_[0, 0], k_means.cluster_centers_[0, 1], color="blue", marker="o", linestyle="None", markersize=8)
    plt.plot(k_means.cluster_centers_[1, 0], k_means.cluster_centers_[1, 1], color="red", marker="o", linestyle="None", markersize=8)
    plt.plot(k_means.cluster_centers_[2, 0], k_means.cluster_centers_[2, 1], color="green", marker="o", linestyle="None", markersize=8)

plt.xlim(-1*LIM, LIM)
plt.ylim(-1*LIM, LIM)

if TIKZ:
    import tikzplotlib
    if RANDOM:
        tikzplotlib.save("grafiken/python/tikz/kmeans/random.tikz", axis_width="7cm")
    else:
        tikzplotlib.save("grafiken/python/tikz/kmeans/kmeans_pp.tikz", axis_width="7cm")
else:
    plt.show()

