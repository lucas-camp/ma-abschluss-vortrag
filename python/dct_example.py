import numpy as np
from scipy.fft import dct, idct

x = np.array([8,16,24,32,40,48,56,64])
x = np.array([0,1,1,2,3,5,8,13])
x = np.array([0.1, -0.9, 0.3, 0.8, 0.6, 0.6, -0.9, -0.8, 0.5, 0.9, -0.5, -0.6, 0.3, -0.7, 0.7, 0.9])

d = dct(x)
r = idct(d)

coeffs = []
for k in range(8):
    s = 0
    for i in range(8):
        x_n = x[i]
        f_n = np.cos(np.pi/8*k*(i+0.5))
        s += x_n * f_n
    coeffs.append(2*s)

rec = []
for k in range(8):
    s = coeffs[0]/2
    for i in range(1, 8):
        if i >= 8:
            x_n = 0
        else:
            x_n = coeffs[i]
        f_n = np.cos(np.pi/8*i*(k+0.5))
        s += x_n * f_n
    rec.append(1/8*s)

print(d)
print(r)
print(coeffs)
print(rec)
z = 0