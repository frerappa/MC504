# Respostas:

## Simulação  

### Questão 1
Os valores para determinadas sequências são mostrados a seguir:
- `disk.py -a 0`
    - **Seek**: 0
    - **Rotation**: 165
    - **Transfer**: 30
- `disk.py -a 6`
    - **Seek**: 0
    - **Rotation**: 325
    - **Transfer**: 30
- `disk.py -a 30`
    - **Seek**: 80
    - **Rotation**: 265
    - **Transfer**: 30
- `disk.py -a 7,30,8`
    - **Seek**: 260
    - **Rotation**: 545
    - **Transfer**: 90
- `disk.py -a 10,11,12,13`
    - **Seek**: 40
    - **Rotation**: 425
    - **Transfer**: 120

### Questão 2
Com o aumento do seek rate, o tempo de seek diminui e, em geral, o tempo de rotação aumenta

### Questão 3
Com a diminuição da taxa de rotação o rotation time e o transfer time aumentam

### Questão 4
Com a workload `disk.py -a 7,30,8`, temos os seguintes tempos para cada política:
- FIFO:
    - inicio -> 7
        - **Seek**: 0
        - **Rotation**: 15
        - **Transfer**: 30 
    - 7 -> 30
        - **Seek**: 80
        - **Rotation**: 220
        - **Transfer**: 30 
    - 30 -> 8
        - **Seek**: 30
        - **Rotation**: 310
        - **Transfer**: 30 
- SSTF:
    - inicio -> 7
        - **Seek**: 0
        - **Rotation**: 15
        - **Transfer**: 30 
    - 7 -> 8
        - **Seek**: 0
        - **Rotation**: 0
        - **Transfer**: 30 
    - 8 -> 30
        - **Seek**: 80
        - **Rotation**: 190
        - **Transfer**: 30 
Nota-se claramente que a segunda abordagem apresentou tempos totais de seek, rotation e transfer.

### Questão 5
- SATF:
    - inicio -> 7
        - **Seek**: 0
        - **Rotation**: 15
        - **Transfer**: 30 
    - 7 -> 8
        - **Seek**: 0
        - **Rotation**: 0
        - **Transfer**: 30 
    - 8 -> 30
        - **Seek**: 80
        - **Rotation**: 190
        - **Transfer**: 30 
É possível perceber que a performance foi igual à da política SSTF. Espera que SATF seja melhor que SSTF em casos em que o tempo de seking é relativamente menor que o de rotação.

### Questão 6
Os blocos 10 e 11 estão na mesma trilha, a externa, assim como os blocos 12 e 13, na interna. O problema na execução dessa workload com as configurações padrões é que o tempo que a cabeça muda de trilha é grande demais para ler os blocos 11 e 12 em sequência na mesma rotação, de modo que é necessário esperar uma volta completa do disco para que 12 e 13 sejam acessados. Nota-se uma melhora no tempo de rptação para valores de skew maiores que 2.

O skew pode ser calculado pela fórmula skew = distancia da trilha / (taxa de seek * (graus de rotação * velocidade de rotação)) 

### Questão 7
Nesse caso o trilho externo contém os blocos 0-35, o do meio os blocos 36-53 e o interno os blocos 54-65. Os resultados são apresentados a seguir:
- `disk.py -z 10,20,30 -a -1 -A 5,-1,0 -s 0`: Acessos a blocos 45, 40, 22, 13, 27:
    - **Externo**: 3/545 = 0,0055
    - **Meio**: 2/630 = 0,0032
- `disk.py -z 10,20,30 -a -1 -A 5,-1,0 -s 1`: Acessos a blocos 7, 45, 41, 13, 26:
    - **Externo**: 3/770 = 0,0039
    - **Meio**: 2/395 = 0,0051
- `disk.py -z 10,20,30 -a -1 -A 5,-1,0 -s 2`: Acessos a blocos 51, 51, 3, 4, 45:
    - **Externo**: 2/95 = 0,021
    - **Meio**: 3/635 = 0,0047
- `disk.py -z 10,20,30 -a -1 -A 5,-1,0 -s 3`: Acessos a blocos 12, 29, 19, 32, 33:
    - **Externo**: 5/875 = 0,0057

### Questão 9
Na sequência de requests aos blocos 1, 2, 3, 4, 3, 1, 35 dada pelo comando `disk.py -a 1,2,3,4,3,1,35 -p SATF`, obtem-se um tempo total de 645. Pela política BSATF, com o comando `disk.py -a 1,2,3,4,3,1,40 -p BSATF`, obtem-se o tempo 645 também. Desse modo, nota-se que o problema de starvation não é solucionado por essa abordagem nesse caso.