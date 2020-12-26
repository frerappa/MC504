# Respostas:

## Simulação

### Questão 1 
Estágio 0  
a  
  
Estágio 1  
a - b  
  
Estágio 2  
a - b/c  
  
Estágio 3  
a - b  
  
Estágio 4  
a - b/d  
  
Estágio 5  
a - b/d/e  

### Questão 4 
Se o processo f termina, os seus processos filhos passam a ser filhos do processo mais ao topo, no caso, a.  
Com a flag -R, eles passam a ser filhos do processo de que c era filho, b.

### Questão 5
Processos:  
Action: a forks b  
Action: b forks c  
Action: c forks d  
Action: d forks e  
Action: c forks f  

Árvore:  
Estágio 0  
a  
  
Estágio 1  
a - b  
  
Estágio 2  
a - b - c  
  
Estágio 3  
a - b - c - d  
  
Estágio 4  
a - b - c - d - e     
  
Estágio 5  
a - b - c - (d - e) / f  

  
