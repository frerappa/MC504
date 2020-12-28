# Respostas:

## Simulação

### Questão 1 
SJF:
- Response time: 200 s
- Turnaround time: 400 s

FIFO:
- Response time: 200 s
- Turnaround time: 400 s

Como ambos os "jobs" chegam simultaneamente e têm a mesma duração, os dois schedulers têm o mesmo comportamento.

### Questão 2
Se a ordem de chegada dos processos por tempo de execução é 200-100-300, temos o seguinte resultado:
SJF:
- Response time: 133.33 s
- Turnaround time: 333.33 s

FIFO:
- Response time: 166.67 s
- Turnaround time: 366.67 s

Uma vez que o processo mais curto não é o primeiro a chegar, a política de FIFO é pior que a SJF

### Questão 3
Se a ordem dos jobs for a mesma que no exercício anterior, temos o seguinte resultado:
RR:
- Response time: 1 s
- Turnaround time: 466 s

Claramente, o response time é inferior, uma vez que o Round Robin divide o tempo de execução dos processos o que, no entanto, aumenta o tempo de turnaround, dado que o tempo de conclusão também é aumentado.

### Questão 4
SJF tem mesmos tempos de turnaround que a política de FIFO quando todos os processos chegam simultaneamente e em ordem crescente de duração

### Questão 5
Uma política de RR tem o mesmo tempo de turnaround que uma de SJF se a ordem de seus processos for a crescente de tempo de execução e se seu time slice for igual ao tempo médio de execução dos processos.

### Questão 6
À medida que os tempos de execução aumentam, o tempo de resposta também aumenta.

### Questão 7
Se o time slice for inferior ao tempo de execução mais curto, o tempo de resposta será igual ao time slice. Caso contrário, será igual à media dos tempos de resposta de cada um dos N processos, que dependerá de suas durações e ordem de início. Por fim, se o time slice for igual ou superior ao maior tempo de execução e os processos executarem em ordem decrescente de tempo, o response time de pior caso será igual ao somatorio de 1 a N-1 da soma de todos os tempos de execução dos j processis anteriores dividido por N.  
