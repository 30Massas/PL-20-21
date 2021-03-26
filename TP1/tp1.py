import re
import time

#import ply.lex as lex

"""
  <processo id="13636">
    <pasta>581</pasta>
    <data>1908-05-20</data>
    <nome>Abilio Augusto Magalhaes</nome>
    <pai/>
    <mae>Maria Jesus Magalhaes</mae>
    <obs/>
  </processo>
"""

def getSeculo(ano):
    i = int(ano)
    if (i<100):
        cent = 1
    elif i % 100 == 0:
        cent = int(i/100)
    else:
        cent = int(i/100 + 1)
    return cent

def getProcessos(lines):
    m = re.findall(r'(<processo .*>((.|\n)+?)</processo>)',lines)
    return m

    
"""
{
    1901: set(8532,5345)
}
"""
def Query1():
    f = open('processos.xml', 'r')

    anos = {}
    seculos = set() 
    dMin = None
    dMax = None
    processos = getProcessos(f.read())
    if processos is None:
        f.close()
        return
    
    f.close()
    
    for p in processos:
        pr = p[0]
        if _id_ := re.search(r'<processo id="(\d+)">',pr).group(1):
            if data := re.search(r'<data>((\d+)-\d+-\d+)</data>',pr):
                dt = data.group(2)
                if lista := anos.get(dt):
                    lista.add(_id_)
                else:
                    aux = set()
                    aux.add(_id_)
                    anos.update({dt : aux})
                seculos.add(getSeculo(dt))
    
            if dMin is None:
                dMin = data.group(1)
            if dMax is None:
                dMax = data.group(1)
            if data.group(1) < dMin:
                dMin = data.group(1)
            if data.group(1) > dMax:
                dMax = data.group(1)
    
    anos_sorted = dict(sorted(anos.items(), key=lambda p:p[0]))

    

    for a in anos_sorted.keys():
        print(f'No ano {a} foram registados {len(anos_sorted.get(a))} processos')

    print(f'\nSéculos: {seculos}')    
    
    print(f'Data {dMin} até {dMax}')

    
    



def Query2():
    proprios = {}
    apelidos = {}
    processos_avaliados = set()

    """
    teste = {
        19:{
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
    processos = getProcessos(f.read())
    for p in processos:
        pr = p[0]
        if _id_ := re.search(r'<processo id="(\d+)">',pr).group(1):
            if _id_ in processos_avaliados:
                pass
            else:
                processos_avaliados.add(_id_)
                
            
    
    f.close()

    
"""
def Query3():
    pass

def Query4():
    pass
    
def Query5():
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


    print('### EXERCÍCIO 2 ###')
    print('1 - Calcular o número de processos por ano; apresente a listagem por ordem cronológica e indique o intervalo de datas em que há registos bem como o número de séculos analisados.\n')
    print('2 - Calcular a frequência de nomes próprios (primeiro nome) e apelidos (último nome) global e mostre os 5 mais frequentes em cada século.\n')
    print('3 - Calcular o número de candidatos (nome principal de cada processo) que têm parentes (irmão, tio, ou primo) eclesiásticos; diga qual o tipo de parentesco mais frequente.\n')
    print('4 - Verificar se o mesmo pai ou a mesma mãe têm mais do que um filho candidato.\n')
    print('5 - Utilizando a linguagem de desenho de grafos DOT4 desenhe todas as árvores genealógicas (com base nos triplos < filho, pai, mãe >) dos candidatos referentes a um ano dado pelo utilizador.\n')

    choice = int (input('Indique a alínea que pretende averiguar: '))
    start = time.time()
    switch(choice)

    end = time.time()
    print()
    print(f'Time elapsed : {end-start} seconds')

main()