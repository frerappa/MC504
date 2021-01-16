# Respostas:

## Simulação

### Questão 1
É esperado que o tamanho da tabela de páginas aumente à medida que o espaço de endereçamento aumente, uma vez que um espaço de endereçamento maior permite o endereçamento de um maior número de páginas e, portanto, uma *page table* maior. Por outro lado, se for aumentado o tamanho das páginas e mantido o espaço de endereçamneto, a tabela de páginas irá diminuir pois o número de páginas que podem ser endereçadas nesse espaço é menor.

### Questão 2
- **Caso 1** - comando `python paging-linear-translate.py -P 1k -a 16k -p 32k -v -u 0`:
    - 0x3a39 -> VPN 14 (ENDEREÇO INVÁLIDO)
    - 0x3ee5 -> VPN 15 (ENDEREÇO INVÁLIDO)
    - 0x33da -> VPN 12 (ENDEREÇO INVÁLIDO)
    - 0x39bd -> VPN 14 (ENDEREÇO INVÁLIDO)
    - 0x13d9 -> VPN 04 (ENDEREÇO INVÁLIDO)

- **Caso 2** - comando `python paging-linear-translate.py -P 1k -a 16k -p 32k -v -u 25`:
    - 0x3986 -> VPN 14 (ENDEREÇO INVÁLIDO)
    - 0x2bc6 -> VPN 10 (0x4FC6)
    - 0x1e37 -> VPN 07 (ENDEREÇO INVÁLIDO)
    - 0x0671 -> VPN 01 (ENDEREÇO INVÁLIDO)
    - 0x1bc9 -> VPN 06 (ENDEREÇO INVÁLIDO)

- **Caso 3** - comando `python paging-linear-translate.py -P 1k -a 16k -p 32k -v -u 50`:
    - 0x3385 -> VPN 12 (0x3F85)
    - 0x231d -> VPN 08 (ENDEREÇO INVÁLIDO)
    - 0x00e6 -> VPN 00 (0x60E4)
    - 0x2e0f -> VPN 11 (ENDEREÇO INVÁLIDO)
    - 0x1986 -> VPN 06 (0x7586)

- **Caso 4** - comando `python paging-linear-translate.py -P 1k -a 16k -p 32k -v -u 75`:
    - 0x2e0f -> VPN 11 (0x4E0F)
    - 0x1986 -> VPN 06 (0x7D86) 
    - 0x34ca -> VPN 13 (0x6CCA)
    - 0x2ac3 -> VPN 10 (0x0EC3)
    - 0x0012 -> VPN 00 (0x6012) 

- **Caso 5** - comando `python paging-linear-translate.py -P 1k -a 16k -p 32k -v -u 100`:
    - 0x2e0f -> VPN 11 (0x4E0F)
    - 0x1986 -> VPN 06 (0x7D86) 
    - 0x34ca -> VPN 13 (0x6CCA)
    - 0x2ac3 -> VPN 10 (0x0EC3)
    - 0x0012 -> VPN 00 (0x6012) 

### Questão 3
A combinação dos parâmetros do comando `python paging-linear-translate.py -P 8 -a 32 -p 1024 -v -s 1` é irrealista, uma vez que o espaço de endereçamento de 32 bits somente possibilita 4 páginas de 8 bits, o que inviabiliza o armazenamento de dados 

