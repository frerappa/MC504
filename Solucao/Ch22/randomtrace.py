import subprocess
import numpy as np
import matplotlib.pyplot as plt
import random

sizes = np.linspace(1, 100, 100)
hit_rate_FIFO = np.ones(100)
hit_rate_LRU = np.ones(100)

hit_rate_OPT = np.ones(100)
hit_rate_UNOPT= np.ones(100)
hit_rate_RAND= np.ones(100)
hit_rate_CLOCK = np.ones(100)

policies = ['FIFO', 'LRU','OPT', 'UNOPT', 'RAND', 'CLOCK']

trace = []
for i in range(100):
    trace.append(random.randint(1,100))
trace_string = [str(x) + "," for x in trace[0:99]]
trace_string.append(str(trace[99]))
trace_string = "".join(trace_string)

for size in range(1,101):
    for policy in policies:
        result = subprocess.run(['python','paging-policy.py', '-p', policy, '-a', trace_string, '-C', str(size), '-c'], shell=True, stdout=subprocess.PIPE, cwd='../../ostep-homework/vm-beyondphys-policy')
        output = result.stdout
        output_lines = output.split(b'\n')
        # answers = output_lines[11:111]
        tam_linha=len(output_lines[111])
        linha = output_lines[111][tam_linha-18:tam_linha-2].decode('ascii')
        linhaLista = linha.replace(' ', ':').split(':')
        hits = int(linhaLista[1])
        if policy == 'FIFO':
            hit_rate_FIFO[size - 1] = hits
        elif policy == 'LRU':
            hit_rate_LRU[size - 1] = hits

        elif policy == 'OPT':
            hit_rate_OPT[size - 1] = hits
        elif policy == 'UNOPT':
            hit_rate_UNOPT[size - 1] = hits
        elif policy == 'RAND':
            hit_rate_RAND[size - 1] = hits
        elif policy == 'CLOCK':
            hit_rate_CLOCK[size - 1] = hits
    
    print("Tamanho ok - " + str(size))


plt.ylabel("Hit rate (%)")
plt.xlabel("Cache size")
plt.plot(sizes, hit_rate_FIFO)
plt.plot(sizes, hit_rate_LRU)

plt.plot(sizes, hit_rate_OPT)
plt.plot(sizes, hit_rate_UNOPT)
plt.plot(sizes, hit_rate_RAND)
plt.plot(sizes, hit_rate_CLOCK)
plt.grid(ls='--')
plt.legend(policies)
plt.savefig("graph1.png")
plt.show()

trace = []
for i in range(100):
    chance = random.randint(1, 10)
    if chance <= 5 and len(trace) > 0:
        novo = trace[i - 1]
    else:
        novo = random.randint(1,100)
    trace.append(novo)
trace_string = [str(x) + "," for x in trace[0:99]]
trace_string.append(str(trace[99]))
trace_string = "".join(trace_string)


for size in range(1,101):
    for policy in policies:
        result = subprocess.run(['python','paging-policy.py', '-p', policy, '-a', trace_string, '-C', str(size), '-c'], shell=True, stdout=subprocess.PIPE, cwd='../../ostep-homework/vm-beyondphys-policy')
        output = result.stdout
        output_lines = output.split(b'\n')
        # answers = output_lines[11:111]
        tam_linha=len(output_lines[111])
        linha = output_lines[111][tam_linha-18:tam_linha-2].decode('ascii')
        linhaLista = linha.replace(' ', ':').split(':')
        hits = int(linhaLista[1])
        if policy == 'FIFO':
            hit_rate_FIFO[size - 1] = hits
        elif policy == 'LRU':
            hit_rate_LRU[size - 1] = hits

        elif policy == 'OPT':
            hit_rate_OPT[size - 1] = hits
        elif policy == 'UNOPT':
            hit_rate_UNOPT[size - 1] = hits
        elif policy == 'RAND':
            hit_rate_RAND[size - 1] = hits
        elif policy == 'CLOCK':
            hit_rate_CLOCK[size - 1] = hits
    
    print("Tamanho ok - " + str(size))


plt.ylabel("Hit rate (%)")
plt.xlabel("Cache size")
plt.plot(sizes, hit_rate_FIFO)
plt.plot(sizes, hit_rate_LRU)

plt.plot(sizes, hit_rate_OPT)
plt.plot(sizes, hit_rate_UNOPT)
plt.plot(sizes, hit_rate_RAND)
plt.plot(sizes, hit_rate_CLOCK)
plt.grid(ls='--')
plt.legend(policies)
plt.savefig("graph2.png")
plt.show()

