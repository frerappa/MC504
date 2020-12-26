# Respostas:

## Questão 1 
Todas as respostas devem ser CPU, uma vez que ambos os processos tem 100% de chance de não terem I/O

## Questão 2 
O tempo será igual ao tempo das 4 instruções do primeiro processo executarem na CPU, seguido pelo tempo de espera que a intrução de IO do segundo processo ocorra por completo

## Questão 3
Nesse caso, enquanto o processo com a instrução de IO espeera que ela seja completa, o processador roda o outro processo, de modo que o tempo total da execução de ambos diminui

## Questão 4 
O processo 1 irá esperar o término da instrução de IO do processo 0 antes de iniciar sua execução

## Questão 5 
Nessa situação, o processo 1 se inicia assim que o processo 0 começa a esperar a conclusão da instrução de IO

## Questão 6
Nesse caso, a fila segue sua ordem "normal" (processo 0-1-2-3) e executa cada processo até seu término ou uma interrupção de I/O. Nesse caso, essa abordagem ão é a ideal, por o processo 0 tem várias intruções e Io em sequência, que poderiam ser "esperadas" em paralelo com as execuções em CPU dos outros, o que não ocorre no exemplo, e há periodos os que a somente se espera o IO e nada mais é feito.

## Questão 7
Nesse caso,os processos executam suas instruções de CPU enquanto o primeeiro processo espera a conclusão de seu IO, o que é mais eficiente que o anterior. Executar um processo que acabou de finalizar um I/O pode ser eficiente caso haja mais instruções de I/O em sequência.