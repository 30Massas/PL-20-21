import re
import generalFunctions as gf


def Query1():
    f = open('processos.xml', 'r')

    anos = {}
    seculos = set() 
    dMin = None
    dMax = None
    processos = gf.getProcessos(f.read())
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
                seculos.add(gf.getSeculo(dt))
    
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

    print(f'\nExiste registo em {len(seculos)} séculos.')    
    
    print(f'Data {dMin} até {dMax}')


   