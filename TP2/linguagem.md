# Linguagem

```
int
operações aritmeticas, relacionais e logicas

atribuir expressoes a variaveis

efetuar instruções condicionais

efetuar isntruções ciclicas -> minimo - repeat-until, adicional - while-do, for-do


```

### Requisitos

#### Obrigatórios
* ler 4 números e dizer se podem formar um quadrado
    * read store x4 
    * carregar 1º carregar 2º equals not JZ invalido carregar 2º carregar 3º ...
* ler um inteiro N, e depois ler N números e retornar o menor
    * read store while (read store)
    * write min
* ler N (constante do programa) números e calcular e imprimir o somatório
    *  while N>0 read num , adicionar ao sum
* contar e imprimir os números ímpares de uma sequência de números naturais
    * while read != 0 
    * ler numeros
    * ir contando e imprimir numeros impares 

#### Opcionais
* ler e armazenar N números num array, imprimir os valores por ordem inversa
* invocar e usar num programa seu uma função 'potencia()', que começa por ler do input a base B e o expoente E e retorna o valor B^E

### Tokens
```py
tokens = ['NUM','ID','POTENCIA','EQUIV','REPEATUNTIL']

literals = ['=', '+' , '-' , '/', '*','(',',',')',';','<','>']
```