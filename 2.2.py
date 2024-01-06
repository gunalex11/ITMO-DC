import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt

Z = np.loadtxt('sch.csv', delimiter=';')
Phi = np.loadtxt('ves.csv', delimiter=';')

F = np.dot(Z,np.transpose(Phi))

xs = []
ys = []

for i in range(len(F)):
    for j in range(len(F[0])):
        if F[i][j] < 1e-14:
            ys.append(len(F)-i)
            xs.append(j)

plt.scatter(xs,ys, s=1, c = 'black')
plt.show()
