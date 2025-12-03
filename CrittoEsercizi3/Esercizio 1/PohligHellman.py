from Shanks import algo_shanks
from Gruppi import Group

#Prende un intero n e restituisce un dizionario con 
# chiave = fattore primo    (q)
# valore = esponente        (c)

N = {}
def fattorizzazione(n):
    if n == 1:
        return {}
    
    if n in N:
        return dict(N[n])
    else:
        fattori = None
        for i in range(2,int(n**(1/2))+1):
            if n % i == 0:
                fattori = fattorizzazione(n//i)

                f = fattorizzazione(i)
                for k in f.items():
                    fattori[k[0]] = fattori.get(k[0],0) + k[1]
                # fattori[i] = fattori.get(i,0) + 1
        if fattori == None:
            fattori = {n:1}
        
        N[n] = dict(fattori)
        return fattori

def algo_pohlig_hellman(G,n,a,b,q,c):
    A = []
    B = [ 0 for _ in range(c+1)]
    B[0] = b
    for j in range(c):
        exp = G.exp(q,j+1)
        delta = G.exp(B[j],n//exp)
        # print(f"delta:{delta} = (Bj){B[j]}^({n-1}/{exp})")

        #Trova i tale che delta = alpha^in/q con l'algoritmo di shanks

        a_n_su_q = G.exp(a,n//q)
        
        # print(f"Calcolando log_{a_n_su_q}({delta}) = ")
        i = algo_shanks(G,n,a_n_su_q,delta)
        # print(f"i:{i} =  al{a}^i({n-1}/{q})")

        A.append(i)

        termine1 = A[j]
        termine2 = G.exp(q,j)

        B[j+1] = G.mul(B[j], G.exp(a,-G.mul(termine1,termine2)))

    return A

# Usando il teorema cinese del resto

def algo_pohlig(G,n,a,b):
    fattori = fattorizzazione(n)
    eq = []
    for i in fattori.items():
        p  = algo_pohlig_hellman(G,n,a,b,i[0],i[1])
        a_ = 0
        for j in range(i[1]):
            a_+= G.mul( p[j], G.exp(i[0],j)) + i[0]**i[1]

        eq.append((a_,i[0]**i[1]))

    x = 0
    for r, m in eq:
        Mi = n // m
        G = Group(m)
        inv = G.inverse(Mi)
        x += r * Mi * inv
    return x % n