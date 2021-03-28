import re
import generalFunctions as gf


def Query3():
    processos_avaliados = set()

    """
    {
    tio paterno:4
    tio materno:6
    tio avô:
    irmao
    primo

    }
    """
    graus = {}

    f=open('processos.xml','r')
    processos = gf.getProcessos(f.read())

    countCandidatos = 0


    for p in processos:

        pr = p[0]

        if _id_ := gf.getId(pr):

            if _id_ in processos_avaliados:
                pass
            else:
                processos_avaliados.add(_id_)

                if m:= re.search(r'<obs>((.|\n)+?)</obs>',pr):
                    parentesco = m.group(1)
                    
                    if re.search(r'(?i:((tio|irmao|primo|sobrinho)(s)? ?(avo)?) ?(materno|paterno)?\3?)',parentesco):
                        l_partida = m.group(1).split(".")
                        
                        countCandidatos += 1
                        
                        
                        for p in l_partida:
                            p = p.strip()
                            p = re.sub(r'\s+',r' ',p)
                            a = p.split(",")

                            if len(a) >= 2: # a[-1] -> parentesco
                                
                                if w := re.match(r'(?i:((tio|irmao|primo|sobrinho)(s)? ?(avo)?) ?(materno|paterno)?\3?)',a[-1]):
                                    # 0 -> tio|irmao|primo + avo + materno|paterno
                                    # 1 -> tio|irmao|primo + avo plural -> não usar
                                    # 2 -> tio|irmao|primo singular
                                    # 3 -> s
                                    # 4 -> avo
                                    # 5 -> paterno|materno 
                                    # usar 2 3 4 e 5
                                    

                                    if w.group(3):
                                        # parse no a[-2] "joao e andré"

                                        x = re.split(r' e | e',a[-2])
                                        aux = a[-1]
                                        a.remove(a[-2])
                                        a.remove(a[-1])
                                        for item in x:
                                            a.append(item)
                                        a.append(aux)

                                    if w.group(4) and w.group(5):
                                        _key_ = w.group(2).strip() + " " + w.group(4).strip() + " " + w.group(5).strip()

                                    elif w.group(5):
                                        _key_ = w.group(2).strip() + " " + w.group(5).strip()
    
                                    elif w.group(4):
                                        _key_ = w.group(2).strip() + " " + w.group(4).strip()

                                    else:
                                        _key_ = w.group(2).strip()

                                    
                                    if count:=graus.get(_key_):
                                        graus.update({_key_: count+(len(a)-1)})
                                    else:
                                        graus.update({_key_: len(a)-1})

    graus = dict(sorted(graus.items(), key=lambda p:p[1], reverse=True))

    for grau in graus.keys():
        print(f'{grau} :> {graus.get(grau)}')

    print(f'\nTotal de candidatos avaliados: {countCandidatos}')
    print(f'\nO grau de parentesco mais frequente é {list(graus.keys())[0]}')

