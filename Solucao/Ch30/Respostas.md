# Respostas:

## Código  

### Questão 1
A execução desse programa cria threads consumidoras e produtoras, que são utilizadas na função main

### Questão 2
Com um buffer de tamanho 1, não há como os ponteiros de fill e use se moverem, de modo que permanecem na mesma posição durante a execução. Se o buffer aumenta mas a quantidade de itens produzidos permanece, o consumidor passa a levar sempre o mesmo tempo para consumir o que é produzido. O número NF também aumenta quando o produtor produz algo, como é esperado, e diminui quando é consumido, de modo que sempre se inicia e termina em 0. 

### Questão 4
O script `./main-two-cvs-while -p 1 -c 3 -m 1 -C 0,0,0,1,0,0,0:0,0,0,1,0,0,0:0,0,0,1,0,0,0 -l 10 -v -t` indica que todos os consumidores devem dormir por 1 segundo em c3. Como c0 é o primeiro a pegar a lock e não dorme antes disso, sempre terá a lock, o que faz com que os outros consumidores durmam e, portanto, que c0 tenha todos os produtos. Como há 10 produtos, haverá 10 sleeps de 9 segundos até que c0 consuma tudo + 3 segundos até que todos terminem o loop, num total de 12 segundos.

### Questão 5
No script `./main-two-cvs-while -p 1 -c 3 -m 3 -C 0,0,0,1,0,0,0:0,0,0,1,0,0,0:0,0,0,1,0,0,0 -l 10 -v -t`, como a frequência de sleeps não muda, o tempo será o mesmo, o que pode ser mostrado pela execução do programa, que retorna um tempo de 12,03 segundos

### Questão 6
No script `./main-two-cvs-while -p 1 -c 3 -m 1 -C 0,0,0,0,0,0,1:0,0,0,0,0,0,1:0,0,0,0,0,0,1 -l 10 -v -t`, o fato de que o sleep ocorre após o unlock indica que o produtor poderá produzir mais até que seja consumido, e os consumidores podem consumir mais.

### Questão 7
No script `./main-two-cvs-while -p 1 -c 3 -m 3 -C 0,0,0,0,0,0,1:0,0,0,0,0,0,1:0,0,0,0,0,0,1 -l 10 -v -t`, não é esperada uma mudança no tempo até que os consumidores terminem de consumir.

### Questão 8
Não é possível com um consumidor e um produtor gerar uma sequência que cause um problema; 

### Questão 9
O código apresenta problemas se não há threads dormindo, como em `./main-one-cv-while -p 1 -c 2 -m 1 -v`. 

### Questão 10
O código não epresenta um problema para um consumidor, ms caso haja mais, é possível que um consumidor tente consumir quando não há nenhum dado no buffer.
