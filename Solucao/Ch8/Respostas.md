# Respostas:

## Simulação

### Questão 2
- Exemplo 1:
    python mlfq.py -l 0,200,0 -q 10 -c
- Exemplo 2:
    python mlfq.py -l 0,200,0:100,20,0 -q 10 -c
- Exemplo 3:
    python mlfq.py -l 0,200,0:100,20,1 -q 10 -S -c 
- Exemplo 4a (sem boost de prioridade):
    python mlfq.py -l 0,200,0:100,20,1:100,20,1 -q 10 -S -c 
- Exemplo 4b (com boost de prioridade):
    python mlfq.py -l 0,200,0:100,20,1:100,20,1 -q 10 -S -B 50 -c
- Exemplo 1:
    python mlfq.py -l 0,200,0:100,20,1:100,20,1 -q 10 -B 50 -c
- Exemplo 1:
    python mlfq.py -l 0,800,0 -q 10 -c

### Questão 3
Para se comportar como um Round Robin, o scheduler poderia ter somente uma fila de prioridade, o que faria com que cada processo fosse executado pelo tempo fixo do time quantum e parasse, momento em que seria iniciado o próximo processo da fila pela mesma quantidade de tempo, até que todos estivessem concluidos.

### Questão 4
O simulador poderia se comportar dessa maneira se fosse rodado com o comando `python mlfq.py -l 0,200,0:100,20,1 -q 10 -S -i 5 -c`. Nele, considerando um time slice de 10 ms, um processo longo sem I/O se inicia em 0 ms e tem 200 ms de duração é executado em conjunto com outro, que se inicia em 100 ms, dura 20 ms e tem uma instrução de I/O a cada 1 ms que dura 5 ms. Dado que tem instruções de I/O, o segundo processo não perde prioridade, de modo que tem um tempo de CPU "injusto" se comparado ao outro processo. 

### Questão 5
O processador deve aumentar a prioridade dos processos a cada 50 ms para que um processo de longa execução tenha ao menos 5% de tempo de CPU.