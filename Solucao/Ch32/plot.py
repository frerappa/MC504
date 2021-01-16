import numpy as np
import matplotlib.pyplot as plt

# Grafico 1
# l = 100.000
n = [0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99]
tS = [0, 0.16, 0.59, 1.2, 1.78, 2.35, 2.94, 3.53, 4.17, 4.71, 5.31, 5.78]
tP = [0, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.1, 0.11, 0.12, 0.13, 0.15]



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.title("Execução de vector-global-order com 100.000 loops")
plt.ylabel("Tempo (s)")
plt.xlabel("Número de threads")
plt.plot(n, tS)
plt.plot(n, tP)
plt.grid()
plt.legend(["Sem paralelismo", "Com paralelismo"])

plt.savefig("Ex6.png")
plt.show()

# Grafico 2
# n = 50
l = [0, 10, 100, 1000, 10000, 100000, 1000000]
tS = [0, 0, 0, 0.03, 0.31, 2.92, 29.36]
tP = [0, 0, 0, 0, 0.01, 0.08, 0.63]



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.title("Execução de vector-global-order com 50 threads")
plt.ylabel("Tempo (s)")
plt.xlabel("Número de loops")
plt.plot(l, tS)
plt.plot(l, tP)
plt.grid()
plt.legend(["Sem paralelismo", "Com paralelismo"])

plt.savefig("Ex6-2.png")
plt.show()

# Grafico 3
# n = 50
l = [0, 10, 1000, 10000]
VGO = [0, 0, 0.03, 0.31]
VTW = [0, 0, 2.66, 23.49]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.title("Execução com 50 threads")
plt.ylabel("Tempo (s)")
plt.xlabel("Número de loops")
plt.plot(l, VGO)
plt.plot(l, VTW)
plt.grid()
plt.legend(["vector-global-order", "vector-try-wait"])

plt.savefig("Ex6-3.png")
plt.show()

# Grafico 4
# l = 1000
n = [1, 5, 10, 15, 25, 30, 40, 50, 70]
retries = [0, 40296, 136585, 237928, 867581, 1120812, 1784378, 3882781, 5395153]


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.title("Execução com 1000 loops")
plt.xlabel("Número de threads")
plt.ylabel("Retries")
plt.plot(n, retries)
plt.grid()


plt.savefig("Ex6-4.png")
plt.show()

