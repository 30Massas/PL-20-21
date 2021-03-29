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

def getYear(process):
    if year := re.search(r'<data>(\d{4})-\d{2}-\d{2}</data>',process):
        return year.group(1)

def getProcessos(lines):
    m = re.findall(r'(<processo .*>((.|\n)+?)</processo>)',lines)
    return m

def getProcessosByData(lines, date):
    proc = getProcessos(lines)
    l = []
    for p in proc:
        pr = p[0]
        y = getYear(pr)

        if y == date:

            l.append(pr)
    return l

def getId(line):
    if m:=re.search(r'<processo id="(\d+)">',line):
        return m.group(1)
    else: 
        return None