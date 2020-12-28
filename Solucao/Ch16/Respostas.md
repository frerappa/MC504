# Respostas:

## Simulação

### Questão 1
- **Caso 1** - comando `segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 0`
    - 0x6C -> SEG1 (0x1EC)
    - 0x61 -> SEG1 (ENDEREÇO INVALIDO)
    - 0x35 -> SEG0 (ENDEREÇO INVALIDO)
    - 0x21 -> SEG0 (ENDEREÇO INVALIDO)
    - 0x41 -> SEG1 (ENDEREÇO INVALIDO)   

- **Caso 2** - comando `segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 1`
    - 0x11 -> SEG0 (0x11)
    - 0x6C -> SEG1 (0x1EC)
    - 0x61 -> SEG1 (ENDEREÇO INVALIDO)
    - 0x20 -> SEG0 (ENDEREÇO INVALIDO)
    - 0x3F -> SEG0 (ENDEREÇO INVALIDO)

- **Caso 3** - comando `segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 2`
    - 0x7A -> SEG1 (0x1FA)
    - 0x79 -> SEG1 (0x1F9)
    - 0x07 -> SEG0 (0x7)
    - 0x0A -> SEG0 (0xA)
    - 0x6A -> SEG1 (ENDEREÇO INVALIDO)   

### Questão 2
O endereço virtual máximo do segmento 0 é 19, enquanto o endereço virtual mínimo do segmento 1 é 108. Na memória física, isso indica que as posições de memória entre os valores 20 e 491 são inválidas. O valor máximo do segmento 0 pode ser conferido executando os comandos `segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 2 -A 19 -c` e `segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 2 -A 20 -c`, e os mínimos do segmento 1 pelos comandos `segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 2 -A 108 -c` e `segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 2 -A 107 -c`. 

### Questão 3
Considerando o comando modelo `segmentation.py -a 16 -p 128 -A 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 --b0 ? --l0 ? --b1 ? --l1 ?` e a restrição de endereços "válido-válido-inválido-...-inválido-válido-válido", temos que a base b0 deve ser 0 e a base b1 deve ser 128, de modo que os limites devam ser l0 = l1 = 2. Assim, o comando será `segmentation.py -a 16 -p 128 -A 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 --b0 0 --l0 2 --b1 128 --l1 2`.

### Questão 4


### Questão 5
Se for setado um limite de 0 para ambos os segmentos, não haverá endereços válidos. Senão, se os endereços base forem subsequentes, os segmentos serão sobrepostos, de modo que também não haverá endereços válidos.
