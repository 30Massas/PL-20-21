import re
import generalFunctions as gf
from graphviz import Digraph

 
def getProcID(proc):
    proc = re.sub(r'\s+',' ',proc)
    if m := re.search(r' ?Proc\.(\d+)\.?',proc):
        return m.group(1)

def getIrmaos(obs):
    obs = re.sub(r'\s+',r' ',obs)
    l = []
    if irmaos := re.findall(r'([\w ,]*,Irmao(s)?[\w ]*\.( ?Proc\.\d+\.)?)',obs):
        for i in irmaos:
            l.append(i[0])   
    return l
    
def Query5():
    startID = 0
    dot = Digraph(comment="Gen_Trees")

    processos_avaliados = set()
    f = open('processos.xml', 'r')
        
    ano = input('Indique o ano que pretende investigar: ')
    
    processos = gf.getProcessosByData(f.read(), ano)
    
    for pr in processos:
        if _id_ := gf.getId(pr):
            if _id_ in processos_avaliados:
                pass
            else:
                auxID = str(startID)
                if nome := re.search(r'<nome>((.|\n)*)</nome>',pr):
                    nome = nome.group(1)
                    processos_avaliados.add(_id_)
                    dot.node(nome+_id_,nome)
                    
                    mae = re.search(r'<mae>((.|\n)*)</mae>',pr)
                    if mae:
                        mae = mae.group(1)
                        dot.node(mae+auxID,mae)
                        dot.edge(nome+_id_,mae+auxID)
                    pai = re.search(r'<pai>((.|\n)*)</pai>',pr)
                    if pai:
                        pai = pai.group(1)
                        dot.node(pai+auxID,pai)
                        dot.edge(nome+_id_,pai+auxID)
                        
                    if obs := re.search(r'<obs>((.|\n)*)</obs>',pr):
                        obs = obs.group(1)
                        if inf := getIrmaos(obs):
                            for i in inf:
                                i = re.split(r',Irmaos?[\w ]*\. ?',i)
                                if i[1] != '':
                                    _bid_ = getProcID(i[1])
                                    processos_avaliados.add(_bid_)
                                else :
                                    _bid_ = i[1]
                                if irmaos := re.split(r'( e |,)',i[0]):
                                    for mano in irmaos:
                                        if mano != ' e ':
                                            dot.node(mano+_bid_,mano)
                                            if pai:
                                                dot.edge(mano+_bid_,pai+auxID)
                                            if mae:
                                                dot.edge(mano+_bid_,mae+auxID)
                                
                startID += 1                         
                     
    g = open('gen_trees.gv','w+')
    g.write(dot.source)
    g.close()
    
    dot.render('gen_trees.gv',view=True)

    f.close()
