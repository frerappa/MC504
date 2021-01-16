import subprocess
import numpy as np
import matplotlib.pyplot as plt
import random

MAX = 100
THREADS = 2
loops = 100

freq = np.linspace(1, MAX, MAX)
values = np.zeros(MAX)
expected = loops*THREADS

for interrupt_freq in range(1, MAX + 1):
    result = subprocess.run(['python', 'x86.py', '-p', 'looping-race-nolock.s', '-a', 'bx=' + str(loops), '-t', '2', '-M', '2000', '-i', str(interrupt_freq), '-c'], shell=True, stdout=subprocess.PIPE, cwd='../../ostep-homework/threads-intro')
    output = result.stdout
    output_lines = output.split(b'\n')
    line = output_lines[len(output_lines) - 2].decode("ascii").split(' ')
    final_value = int(line[2])
    values[interrupt_freq - 1] = final_value



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.ylabel("Valor de value")
plt.xlabel("Instruções até interrupção")
plt.axhline(y=expected, color='r', linestyle='-')
plt.plot(freq, values)
plt.grid(ls='-', which="major", color="black")
minor_ticks = np.arange(0, 101, 3)
ax.set_xticks(minor_ticks, minor=True)
plt.grid(b=True, which='minor', color='gray', linestyle='--')

plt.savefig("graph.png")
plt.show()

