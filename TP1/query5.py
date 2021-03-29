import re
import generalFunctions as gf
from graphviz import Digraph



def Query5():
    
    f = open('processos.xml', 'r')

    processos = gf.getProcessos(f.read())

    dot = Digraph(comment="teste")

    ano = input('Indique o ano que pretende investigar: ')

    processos_avaliados = set()
    idBD = 0
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
                            
                            
                            dot.node(filho+str(idBD),filho)
                            if pai:
                                dot.node(pai+str(idBD+1),pai)
                                dot.edge(filho+str(idBD),pai+str(idBD+1))
                            if mae: 
                                dot.node(mae+str(idBD+1),mae)
                                dot.edge(filho+str(idBD),mae+str(idBD+1))
                            idBD+=1
                            
                                               
    g = open('test.gv','r+')
    g.write(dot.source)
    g.close()
    
    dot.render('test.gv',view=True)
    f.close()
