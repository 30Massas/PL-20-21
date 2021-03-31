import re
import generalFunctions as gf

def Query2():

    """
    
    proprios = {
        "Maria": {
            19:4
            18:3
            17:0
        }
        "Paulo" : {
            
        }
          
    }
    apelidos = {
        
    }
    
    """

    processos_avaliados = set()
    proprios = {}
    apelidos = {}
    
    maxSec = 0
    minSec = 30

    f = open('processos.xml','r')
    processos = gf.getProcessos(f.read())
    for p in processos:
        pr = p[0]
        if _id_ := gf.getId(pr):
            if _id_ in processos_avaliados:
                #Já foi avaliado, caso de datasets repetidos
                pass
            else:
                #Processo ainda não foi avaliado
                processos_avaliados.add(_id_)
                if _data_ := re.search(r'<data>((\d{4})-\d{2}-\d{2})</data>',pr):
                    ano = _data_.group(2)
                    sec = gf.getSeculo(ano)
                    if sec < minSec:
                        minSec = sec
                    if sec > maxSec:
                        maxSec = sec
                    
                    if _nomeComp_ := re.search(r'<nome>(((\w+)[ .\t]*)+)</nome>',pr):
                        _nomeComp_ = _nomeComp_.group(1)
                        _proprio_ = _nomeComp_.split(r' ')[0]
                        _apelido_ = _nomeComp_.split(r' ')[-1]         
                        
                        #Atualizar Dicionário de Nomes Próprios
                        if p := proprios.get(_proprio_):
                            #Se já estiver registado
                            if p_dict_sec := p.get(sec):
                                #Se já existir século registado
                                p.update({sec:p_dict_sec+1})
                            else:
                                #Caso o século ainda não tenha sido registado
                                p.update({sec:1})
                        else:
                            #Caso o nome ainda não tenha sido registado
                            proprios.update({_proprio_: {sec:1}})
                        
                        #Atualizar Dicionários de Apelidos
                        if a := apelidos.get(_apelido_):
                            #Se já estiver registado
                            if a_dict_sec := a.get(sec):
                                #Se já existir século registado
                                a.update({sec : a_dict_sec+1})
                            else:
                                #Caso o século ainda não tenha sido registado
                                a.update({sec : 1})
                        else:
                            #Caso o apelido ainda não tenha sido registado
                            apelidos.update({_apelido_: {sec:1}})
                    
    proprios = dict(sorted(proprios.items(), key=lambda p:p[0]))
    apelidos = dict(sorted(apelidos.items(), key=lambda p:p[0]))    

    print("### Frequência de nomes próprios GLOBAL ###")
    # Print de Nomes Próprios
    for n in proprios:
        count = 0
        for sec in proprios.get(n):
            count += int(proprios.get(n).get(sec))
        print(f'{n} :> {count}')
    
    print('\n#####################\n')
    
    print("### Frequência de apelidos GLOBAL ###")
    # Print de Apelidos
    for n in apelidos:
        count = 0
        for sec in apelidos.get(n):
            count += int(apelidos.get(n).get(sec))
        print(f'{n} :> {count}')

    print('\n#####################\n')
    
    print("$$$ Frequência de nomes próprios $$$")
    for sec in range(minSec,maxSec+1):
        listProprios = []
        for nome in proprios:
        # print de nomes próprios
            if count := proprios.get(nome).get(sec):
                listProprios.append((nome,count))
                
        listProprios = sorted(listProprios,key = lambda x : x[1],reverse=True)
        print(f'\nTOP 5 Nomes Próprios | Século {sec}\n')
        for a in range(5):
            print(f'{listProprios[a][0]} : {listProprios[a][1]}')
        
               

    print('\n#####################\n')

    
    print("$$$ Frequência de apelidos $$$")
    # print de apelidos
    for sec in range(minSec,maxSec+1):
        listApelidos = []
        for nome in apelidos:
        # print de nomes próprios
            if count := apelidos.get(nome).get(sec):
                listApelidos.append((nome,count))
                
        listApelidos = sorted(listApelidos,key = lambda x : x[1],reverse=True)
        print(f'\nTOP 5 Apelidos | Século {sec}\n')
        for a in range(5):
            print(f'{listApelidos[a][0]} : {listApelidos[a][1]}')
        
    
    
    f.close()