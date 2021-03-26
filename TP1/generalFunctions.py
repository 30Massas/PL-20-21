import re

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