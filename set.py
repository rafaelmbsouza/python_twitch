import random
import time

NUMZAO = 100000000
li = [random.randint(0,NUMZAO) for i in range(int(NUMZAO/2))]

se = set(li)

tic = time.time()
9999990 in li
tac_li = time.time()
9999990 in se
tac_se = time.time()

print('A busca na lista demorou: '+str(tac_li-tic))
print('A busca no set demorou: '+str(tac_se-tac_li))