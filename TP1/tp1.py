import re
import time
import query1 as q1
import query2 as q2
import query3 as q3
import query4 as q4
import query5 as q5
 

def switch(i):
    switcher={
        0: exit,
        1: q1.Query1,
        2: q2.Query2,
        3: q3.Query3,
        4: q4.Query4,
        5: q5.Query5
    }
    return switcher.get(i,lambda: "Invalid Query")()


def main():

    choice = -1
    
    while choice != 0:
      print('### EXERCÍCIO 2 ###')
      print('1 - Calcular o número de processos por ano; apresente a listagem por ordem cronológica e indique o intervalo de datas em que há registos bem como o número de séculos analisados.\n')
      print('2 - Calcular a frequência de nomes próprios (primeiro nome) e apelidos (último nome) global e mostre os 5 mais frequentes em cada século.\n')
      print('3 - Calcular o número de candidatos (nome principal de cada processo) que têm parentes (irmão, tio, ou primo) eclesiásticos; diga qual o tipo de parentesco mais frequente.\n')
      print('4 - Verificar se o mesmo pai ou a mesma mãe têm mais do que um filho candidato.\n')
      print('5 - Utilizando a linguagem de desenho de grafos DOT4 desenhe todas as árvores genealógicas (com base nos triplos < filho, pai, mãe >) dos candidatos referentes a um ano dado pelo utilizador.\n')
      print('0 - Sair do programa.\n')

      choice = int (input('Indique a alínea que pretende averiguar: '))
      start = time.time()
      switch(choice)

      end = time.time()
      time.sleep(3)
      print()
      print(f'Time elapsed : {end-start} seconds')

main()