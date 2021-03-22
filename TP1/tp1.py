import re
import time


def Query1():
    f = open('TP1/processos.xml', 'r')

    anos = {}
    seculos = set() 

    for line in f:
        if (m := re.search(r'<data>(([1-9]{1}[0-9]{0,3}))-\d{2}-\d{2}</data>',line)) is not None:
            ano = m.group(1)
            if ano in anos:
                anos[ano] += 1
            else:
                anos[ano] = 1
            i = int(ano)
            if (i<100):
                cent = 1
            elif i % 100 == 0:
                cent = int(i/100)
            else:
                cent = int(i/100 + 1)
            seculos.add(cent)
            
    anos_sorted = dict(sorted(anos.items(), key=lambda p:p[0]))

    for a in anos_sorted.keys():
        print(f'No ano {a} foram registados {anos_sorted.get(a)} processos')

    print(f'\nSéculos: {seculos}')
        
    f.close()
    



def Query2():
    proprios = {}
    apelidos = {}
    """
    teste = {
        1900:{
            prorios{
                 maria:4
                }
            apelidos{
                 almeida:5
                }
            }
    }
    
    """
    teste = {}

    f = open('TP1/processos.xml','r')
    lines = f.read()

    if (m := re.findall(r'<processo .*>((.|\n))?</processo>',lines)) is not None:
        print(m[1])
    else:
        print('A puta nao entra')

                
            
    
    f.close()

    
"""
def Query3():
    pass

def Query4():
    pass
    
    """

def switch(i):
    switcher={
        1: Query1,
        2: Query2
        #3: Query3,
        #4: Query4
        #5: Query5
    }
    return switcher.get(i,lambda: "Invalid Query")()


def main():
    start = time.time()


    print('### EXERCÍCIO 2 ###')
    print('1 - Calcular o número de processos por ano; apresente a listagem por ordem cronológica e indique o intervalo de datas em que há registos bem como o número de séculos analisados.\n')
    print('2 - Calcular a frequência de nomes próprios (primeiro nome) e apelidos (último nome) global e mostre os 5 mais frequentes em cada século.\n')
    print('3 - Calcular o número de candidatos (nome principal de cada processo) que têm parentes (irmão, tio, ou primo) eclesiásticos; diga qual o tipo de parentesco mais frequente.\n')
    print('4 - Verificar se o mesmo pai ou a mesma mãe têm mais do que um filho candidato.\n')
    print('5 - Utilizando a linguagem de desenho de grafos DOT4 desenhe todas as árvores genealógicas (com base nos triplos < filho, pai, mãe >) dos candidatos referentes a um ano dado pelo utilizador.\n')

    choice = int (input('Indique a alínea que pretende averiguar: '))

    switch(choice)

    end = time.time()
    print(f'Time elapsed : {end-start} seconds')

main()