import re
import generalFunctions as gf
from itertools import tee # iterators
from graphviz import Digraph

 
dot = Digraph(comment="teste")

processos_avaliados = set()
f = open('teste.xml', 'r')
processos = None

def adicionaPais(name,temp,ano, filho):
    
    for pr in processos:
        if _id_ := gf.getId(pr):
            if _id_ not in temp:
                if me := re.search(r'<nome>((.|\n)*)</nome>',pr):
                    me = me.group(1)
                    if me == name: # nome igual
                        temp.add(_id_)
                        
                        if _id_ in processos_avaliados:
                            dot.edge(filho,_id_)
                        else:
                            processos_avaliados.add(_id_)
                            dot.node(_id_,name)
                            dot.edge(filho,_id_)
                            
                            if mae := re.search(r'<mae>((.|\n)*)</mae>',pr):
                                mae = mae.group(1)
                                adicionaPais(mae,temp,ano, _id_)
                            if pai := re.search(r'<pai>((.|\n)*)</pai>',pr):
                                pai = pai.group(1)
                                adicionaPais(pai,temp,ano, _id_)
                        return
                    
def Query5():
    
    
    ano = input('Indique o ano que pretende investigar: ')
    
    global processos
    processos = gf.getProcessosByData(f.read(), ano)
    
    for pr in processos:
        if _id_ := gf.getId(pr):
            if _id_ in processos_avaliados:
                pass
            else:

                if filho := re.search(r'<nome>((.|\n)*)</nome>',pr):
                    processos_avaliados.add(_id_)
                    filho = filho.group(1)
                    dot.node(_id_,filho)
                    
                    if mae := re.search(r'<mae>((.|\n)*)</mae>',pr):
                        mae = mae.group(1)
                        temp = set()
                        temp.add(_id_)
                        adicionaPais(mae,temp,ano, _id_)
                    if pai := re.search(r'<pai>((.|\n)*)</pai>',pr):
                        pai = pai.group(1)
                        temp = set()
                        temp.add(_id_)
                        adicionaPais(pai,temp,ano, _id_)
    # idBD = 0
    
    
    """
    for p in processos:
        pr = p[0]

        if _id_ := gf.getId(pr):
            if _id_ in processos_avaliados:
                pass
            else:
                processos_avaliados.add(_id_)

                if data := re.search(r'<data>(\d{4})-\d{2}-\d{2}</data>',pr):
                    dt = data.group(1)

                    if dt == ano:
                        
                        if filho := re.search(r'<nome>((.|\n)*)</nome>',pr):
                            filho = filho.group(1)
                        
                            if pai := re.search(r'<pai>((.|\n)*)</pai>',pr):
                                pai = pai.group(1)
                            if mae := re.search(r'<mae>((.|\n)*)</mae>',pr):
                                mae = mae.group(1)
                            
                            
                            if pai and mae:
                                dot.node(filho+pai+mae,filho)
                                dot.node(pai+mae,pai)
                                dot.edge(filho+pai+mae,pai+mae)
                        
                                dot.node(mae+pai,mae+pai)
                                dot.edge(filho+pai+mae,mae+pai)
                            elif pai:
                                dot.node(filho+pai,filho)
                                dot.node(pai,pai)
                                dot.edge(filho+pai,pai)
                            elif mae:
                                dot.node(filho+mae,filho)
                                dot.node(mae,mae)
                                dot.edge(filho+mae,mae)
                        
                        
                            idBD+=1
                   """         
                                             
    g = open('test.gv','r+')
    g.write(dot.source)
    g.close()
    
    dot.render('test.gv',view=True)

    f.close()
