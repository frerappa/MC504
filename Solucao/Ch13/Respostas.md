# Respostas:

## Código

### Questão 2
Há cerca de 7,9 GB de memória no sistema, com aproximadamente 2,5 GB livres, o que é de se esperar pela configuração da máquina e pelo uso atual. A memória de swap, no entanto, de 14 GB no total, é maior que a capacidade de memória física do sistema, indicando que hjá algum tipo de virtualização, como é esperado.

### Questão 3
O programa `memory-user.c` é mostrado a seguir, e recebe um parâmetro da linha de comando que especificaa o número de MB que o proframa deve utilizar, alocados dinâmicamente.
```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


int main(int argc, char *argv[]){
    if (argc == 2){
        int mb = atoi(argv[1]);
        int n_elem = (mb*1000000)/4;
        int *v;
        v = malloc(mb*1000000);
        for (int i = 0; i < n_elem; i++){
            v[i] = i;
            if (i == n_elem - 1){
                i = 0;
            }
        }
    }
    else{
        printf("E necessario indicar o numero de MB utilizados\n");
    }
    return 0;
}
```

### Questão 4
Inicialmente, o uso de `free` indicava que havia 3123 MB livres. Durante a execução do programa acima para utilzar 2 GB, ou 2000 MB de memória, o uso de `free` mostrou que havia somente 1226 MB disponíveis, o que indica que foram utilizados 1886 MB pelo programa, valor próximo do esperado. Ao finalizar o programa, quantidade de memória livre se aproxima do valor inicial. Se tentarmos executar o programa com um valor muito grande de MB, ele não executa. Se o programa for modificado para que o vetor seja alocado estáticamente com um número grande de MB, sua execução gera um Segmentation Fault, que indica que foi acessada uma poosição de memória inválida. 

### Questão 7
No caso, foram mostradas 18 entidades durante a execução de `memory-user.c`, que incluiam a stack e o heap.

### Questão 8   
Se executado com 2000 MB de memória, `pmap` indica a utilização de 1953336 KB, ou 1953,336 MB, que se aproxima do que se espera. Analogamente, se for utilizado como parâmetro 1 MB, `pmap` mostra que foram usados 1188 KB, 1,188 MB, também próximo ao valor esperado.