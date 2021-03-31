import re
import generalFunctions as gf


def turnToSingular(g):
    final = ''
    words = g.split(' ')
    for word in words:
        sing = word.rstrip(r's|s ')
        final += sing + ' '
    last = list(final)[-1]
    list(final).remove(last)
    return final

def Query3():
    f = open('processos.xml', 'r')

    processos = gf.getProcessos(f.read())

    processos_avaliados = set()

    contCandidatos = 0
    accountedFor = False
    graus = {}

    for p in processos:
        pr = p[0]

        if _id_ := gf.getId(pr):
            if _id_ in processos_avaliados:
                pass
            else:
                processos_avaliados.add(_id_)

                if _obs_ := re.search(r'<obs>((.|\n)+?)</obs>',pr):

                    obsConteudo = _obs_.group(1)
                    obsConteudo = re.sub(r'\s+',r' ',obsConteudo)

                    obsConteudo_splited = re.split(r'. ?Proc.\d+. ?',obsConteudo)

                    accountedFor = False

                    for element in obsConteudo_splited:
                        obsConteudo_splited2 = re.split(r'\.',element)
                        

                        for elem in obsConteudo_splited2:
                            if m:= re.search(r'(([A-Z]\w+( e | |,)?)+) ?,((([A-Z]\w+) ?)*)',elem):
                                g = m.group(4)
                                
                                if re.search(r'(?i:(sao|san|nos))',g):
                                    pass

                                elif g == '':
                                    pass

                                else:
                                    if not accountedFor:
                                        contCandidatos += 1
                                        accountedFor = True

                                    g_sing = turnToSingular(g)

                                    if count := graus.get(g_sing):
                                        graus.update({g_sing : count+1})
                                        
                                    else:
                                        graus.update({g_sing : 1})

    f.close()

    graus = dict(sorted(graus.items(), key=lambda p:p[1],reverse=True))

    for grau in graus.keys():
        print(f'{grau}:> {graus.get(grau)}')

    print(f'\nTotal de candidatos : {contCandidatos}')
    print(f'\nO grau de parentesco mais frequente é {list(graus.keys())[0]}')

