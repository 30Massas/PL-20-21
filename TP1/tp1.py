import re
import time

start = time.time()
f = open('TP1/processos.xml', 'r')

print(f.read())

end = time.time()
print(f'Time elapsed : {end-start} seconds')