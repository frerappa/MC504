# Respostas:

## Simulação

### Questão 1
Para localizar tabelas de páginas de 2 e 3 níveis, são necessários, respectivamente, 2 e 3 registradores.
### Questão 2 
- Seed 0:
    - 0x611c -> Pagina 0x18 VALIDA -> Pagina 0x8 VALIDA -> Endereço 0x6bc / Valor 0x8
    - 0x3da8 -> Pagina 0xF VALIDA -> Pagina 0xd INVALIDA -> ENDERECO INVALIDO
    - 0x17f5 -> Pagina 0x5 VALIDA -> Pagina 0x1f VALIDA -> Endereço 0x9da / Valor 0x1c
    - 0x7f6c -> Pagina 0x1f VALIDA -> Pagina 0x1b INVALIDA -> ENDERECO INVALIDO
    - 0x0bad -> Pagina 0x2 VALIDA -> Pagina 0x1d INVALIDA -> ENDERECO INVALIDO
    - 0x6d60 -> Pagina 0x1b VALIDA -> Pagina 0xb INVALIDA -> ENDERECO INVALIDO
    - 0x2a5b -> Pagina 0xA VALIDA -> Pagina 0x12 INVALIDA -> ENDERECO INVALIDO  
    - 0x4c5e -> Pagina 0x13 VALIDA -> Pagina 0x2 INVALIDA -> ENDERECO INVALIDO  
    - 0x2592 -> Pagina 0x9 VALIDA -> Pagina 0xC VALIDA -> Endereço 0x7b2 / Valor 1b
    - 0x3e99 -> Pagina 0xF VALIDA -> Pagina 0x14 VALIDA -> Endereço 0x959 / Valor 1e

Para cada acesso à memória são necessários 3 referências.

### Questão 3
Como paginação hierárquica regquer muitos níveis de acesso à memória há mais chances de *misses* no acesso a uma posição de memória, dado que para que o conteúdo seja efetivamente acessado, devem ser feitas N consultas anteriores à memória se houver N níveis, que não necessariamente estaráo no cache, o que pode implicar em maior tempo de aesso.  