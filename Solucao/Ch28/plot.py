import subprocess
import numpy as np
import matplotlib.pyplot as plt
import random

MAX = 100
THREADS = 2
loops = 100

freq = np.linspace(1, MAX, MAX)
values = np.zeros(MAX)
test_and_set = np.zeros(MAX)
peterson = np.zeros(MAX)
ticket = np.zeros(MAX)
yieldv = np.zeros(MAX)
test_and_test_and_set = np.zeros(MAX)

expected = loops*THREADS

policies = ["flag.s", "test-and-set.s"]
# policies = ["flag.s", "test-and-set.s","ticket.s", "yield.s", "test-and-test-and-set.s"]

for interrupt_freq in range(1, MAX + 1):
    for policy in policies:
        result = subprocess.run(['python', 'x86.py', '-p', policy, '-a', 'bx=' + str(loops) + ",bx=" + str(loops), '-M', 'count', '-i', str(interrupt_freq), '-c'], shell=True, stdout=subprocess.PIPE, cwd='../../ostep-homework/threads-locks')
        output = result.stdout
        output_lines = output.split(b'\n')
        line = output_lines[len(output_lines) - 2].decode("ascii").split(' ')
        # print(policy)
        # print(line)
        final_value = int(line[2])
        if policy == "flag.s":
            values[interrupt_freq - 1] = final_value
        elif policy == "test-and-set.s":
            test_and_set[interrupt_freq - 1] = final_value
        elif policy == "peterson.s":
            peterson[interrupt_freq - 1] = final_value
        elif policy == "ticket.s":
            ticket[interrupt_freq - 1] = final_value
        elif policy == "yield.s":
            yieldv[interrupt_freq - 1] = final_value
        elif policy == "test-and-test-and-set.s":
            test_and_test_and_set[interrupt_freq - 1] = final_value
    print("Freqencia completa: " + str(interrupt_freq))
    




fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.ylabel("Valor da variavel")
plt.xlabel("Instruções até interrupção")
plt.axhline(y=expected, color='r', linestyle='-')
plt.plot(freq, values)
plt.grid(ls='-', which="major", color="black")
plt.grid(b=True, which='minor', color='gray', linestyle='--')
plt.savefig("graph1.png")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.ylabel("Valor da variavel")
plt.xlabel("Instruções até interrupção")
plt.axhline(y=expected, color='r', linestyle='-')
plt.plot(freq, test_and_set)
plt.grid(ls='-', which="major", color="black")
plt.grid(b=True, which='minor', color='gray', linestyle='--')
plt.savefig("graph2.png")
plt.show()






fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.ylabel("Valor da variavel")
plt.xlabel("Instruções até interrupção")
# plt.axhline(y=expected, color='r', linestyle='-')
plt.plot(freq, values)
plt.plot(freq, test_and_set)
# plt.plot(freq, peterson)
# plt.plot(freq, ticket)
# plt.plot(freq, yieldv)
# plt.plot(freq, test_and_test_and_set)
plt.grid(ls='-', which="major", color="black")
plt.grid(b=True, which='minor', color='gray', linestyle='--')
plt.legend(policies)
plt.savefig("graph3.png")
plt.show()