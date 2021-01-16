import numpy as np
import matplotlib.pyplot as plt

x = [1000,2000,4000,8000,10000,12000, 15000, 16000]  
y = [7608.38,7852.51,7892.13,7927.46,7903,7896, 1565.47, 712.66]       

fig, ax = plt.subplots()
plt.title("Bandwidth na execução de mem.c")
plt.ylabel("Bandwidth (MB/s)")
plt.xlabel("Quantidade de memória (MB)")
plt.axvline(12809.116,ls="-",label="adas",color="r")
plt.plot(x, y)
plt.grid(ls='--')
plt.savefig("graph.png")
plt.show()

