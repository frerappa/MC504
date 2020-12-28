import subprocess
import numpy as np
import matplotlib.pyplot as plt

limits = np.linspace(0, 1000, 1001)
percentages = np.ones(1001)

for limit in range(1001):
    result = subprocess.run(['python', 'relocation.py', '-s', '1', '-l', str(limit),'-n', '100', '-c'], shell=True, stdout=subprocess.PIPE, cwd='../../ostep-homework/vm-mechanism')
    output = result.stdout
    output_lines = output.split(b'\n')
    answers = output_lines[11:111]
    valid_percentage = 1 - (len(list(filter(lambda x: "SEGMENTATION VIOLATION" in x.decode('ascii'), answers)))/len(answers))
    percentages[limit] = valid_percentage


plt.title("Porcentagem de endereços válidos em função do limite")
plt.ylabel("Freação de endereços válidos")
plt.xlabel("Limite")
plt.plot(limits, limits/1000)
plt.plot(limits, percentages, marker='o', ms=2)
plt.grid(ls='--')
plt.legend(["Reta", "Valores obtidos"])
plt.savefig("graph.png")
plt.show()

