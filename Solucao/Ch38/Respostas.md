# Respostas:

## Simulação  

### Questão 2
Variar o chunk size modifica o mapeamento ao permitir mais blocos e reordena-los.

### Questão 3
Para o problema dado por `raid.py -L 5 -5 LS -c -W seq -C 8K -n 12 -r`, tem-se o seguinte mapeamento:
```
0 2  4  p
1 3  5  p
8 10 p  6
9 11 p  7
```
Nota-se que o resultado obtido foi o mesmo para o caso não invertido.

### Questão 5
Para o comando `raid.py -L [nivel] -t -n 100`, são obtidos os seguintes resultados para diferentes níveis:
- **Nível 0**: 275,7
- **Nível 1**: 278,7
- **Nível 4**: 386,1
- **Nível 5**: 276,7

### Questão 6
Para o comando `raid.py -L [nivel] -t -n 100 -D 20`, com 20 discos, são obtidos os seguintes resultados para diferentes níveis:
- **Nível 0**: 77,1
- **Nível 1**: 84,6
- **Nível 4**: 93,6
- **Nível 5**: 77,9
Portanto com um número de discos 5 vezes maior, obteve-se uma melhora média de 3,64 vezes.