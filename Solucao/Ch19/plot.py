import numpy as np
import matplotlib.pyplot as plt

x = [2,4,8,16, 32, 64, 128,256,512,1024, 2048, 4096]  
y = [2.80200,2.24300,2.39062,5.62869,7.97750,7.64545,8.10037,8.13061,8.12453,8.06013,8.95210,16.05156]       

fig, ax = plt.subplots()
plt.title("TLB Size Measurement")
plt.ylabel("Tempo por acesso (ns)")
plt.xlabel("Páginas")
ax.set_xscale('log', basex=2)
plt.xticks([1,2,4,8,16,32,64,128,256,512,1024,2048,4096], ["1","2","4","8","16","32","64","128","256","512","1024","2048","4096"])
plt.plot(x, y)
plt.grid(ls='--')
plt.savefig("graph.png")
plt.show()

