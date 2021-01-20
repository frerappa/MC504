# Respostas:

## Simulação  

### Questão 1
- Seed 17:
    - mkdir("/u");
    - creat("/a");
    - unlink("/a");
    - mkdir("/z");
    - mkdir("/s");
    - creat("/z/x");
    - link("/z/x", "/u/b");
    - unlink("/u/b");
    - fd=open("/z/x", O_WRONLY|O_APPEND); write(fd, buf, BLOCKSIZE); close(fd);
    - creat("/u/b");
- Seed 5:
    - mkdir("/t");
    - creat("/y");
    - link("/y", "/t/c");
    - 
    - mkdir("/v");
    - mkdir("/j");
    - unlink("/t/c");
    - unlink("/y");
    - creat("/j/a");
    - mkdir("/u");

### Questão 2
- Seed 20:
    - Inicial:
        - inodes       `[d a:0 r:2][][][][][][][]`
        - data         `[(.,0) (..,0)][][][][][][][]`  
    - Estágio 1
        - inodes       `[d a:0 r:2][f a:-1 r:1][][][][][][]`
        - data         `[(.,0) (..,0) (x,1)][][][][][][][]`
    - Estágio 2
        - inodes       `[d a:0 r:2][f a:1 r:1][][][][][][]`
        - data         `[(.,0) (..,0) (x,1)][x][][][][][][]`
    - Estágio 3
        - inodes       `[d a:0 r:2][f a:1 r:1][f a:-1 r:1][][][][][]`
        - data         `[(.,0) (..,0) (x,1) (k,2)][x][][][][][][]`
    - Estágio 4
        - inodes       `[d a:0 r:2][f a:1 r:1][f a:-1 r:1][f a:-1 r:1][][][][]`
        - data         `[(.,0) (..,0) (x,1) (k,2) (y,3)][x][][][][][][]`
    - Estágio 5
        - inodes       `[d a:0 r:2][][f a:-1 r:1][f a:-1 r:1][][][][]`
        - data         `[(.,0) (..,0) (k,2) (y,3)][][][][][][][]`
    - Estágio 6
        - inodes       `[d a:0 r:2][][f a:-1 r:1][][][][][]`
        - data         `[(.,0) (..,0) (k,2)][][][][][][][]`
    - Estágio 7
        - inodes       `[d a:0 r:2][][][][][][][]`
        - data         `[(.,0) (..,0)][][][][][][][]`
    - Estágio 8
        - inodes       `[d a:0 r:2][f a:-1 r:1][][][][][][]`
        - data         `[(.,0) (..,0) (p,1)][][][][][][][]`
    - Estágio 9
        - inodes       `[d a:0 r:2][f a:1 r:1][][][][][][]`
        - data         `[(.,0) (..,0) (p,1)][e][][][][][][]`
    - Estágio 10
        - inodes       `[d a:0 r:2][f a:1 r:2][][][][][][]`
        - data         `[(.,0) (..,0) (p,1) (s,1)][e][][][][][][]`

### Questão 3
Ao executar a seed 5 com 2 discos, pelo comando `vsfs.py -d 2 -n 100 -s 5` nota-se que a operação `mkdir()` falha pela falta de blocos de dados. Se for executada a seed 20 com os mesmos parâmetros, a operação `write()` não pode ser executada.

### Questão 4
Ao executar a seed 5 com 2 inodes, pelo comando `vsfs.py -i 2 -n 100 -s 5` nota-se que a operação `mkdir()` falha. Na seed 8, a operação `create()` falha também.