import math
from Gruppi import Group

def algo_shanks(G: Group,n,a,b):
    m = int(math.ceil(math.sqrt(n)))
    # Modifico il codice del libro per usare i dizionari per un accesso più rapido
    L1 = {}
    L2 = {}
    
    for j in range(m):
        val = G.exp(a,m*j)
        if val not in L1:
            L1[val] = j

    for i in range(m):
        val = G.mul(b,G.exp(a,-i))
        l = (i,val)
        if val not in L2:
            L2[val] = i

    for l in L1.items():
        if l[0] in L2:
            j = l[1]
            i = L2[l[0]]
            return (m*j + i) % n
