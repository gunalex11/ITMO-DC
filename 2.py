import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt

F = np.loadtxt('34_25.csv', delimiter=',')

Ms = []
S = 0
for i in range(len(F[0])):
    for j in range(len(F)):
        S += F[j][i]
    Ms.append(S/len(F))
    S = 0

for i in range(len(F)):
    for j in range(len(F[0])):
        F[i][j] = F[i][j] - Ms[j]

COV = np.dot(np.transpose(F),F)

eig = sorted(np.linalg.eigvals(COV))[::-1]

E1 = np.linalg.eig(COV)[1][:,0]
E2 = np.linalg.eig(COV)[1][:,1]
print()
print(np.linalg.eig(COV))
print(np.dot(COV,E1)[1]/E1[1])
print(np.dot(COV,E2)[0]/E2[0])
print()
print(np.dot(F[0],E1))
print(np.dot(F[0],E2))

Xs = []
Ys = []
for i in range(len(F)):
    Xs.append(np.dot(np.transpose(F[i]),E1))
    Ys.append(np.dot(np.transpose(F[i]),E2))

plt.scatter(Xs,Ys)
plt.show()
