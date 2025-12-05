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
    B = b

    #Per generare le tabelle latex relative all'esecuzione
    
    #(delta, i, a_j,B_j+1)
    #Per ogni iterazione di j si inseriscono 
    exe = []
    
    for j in range(c):

        #Variabile per tabella latex (dizionario delle variabili)
        var = {}
        
        exp = G.exp(q,j+1)
        delta = G.exp(B,n//exp)
        
        var["n"] = n
        var["exp"] = exp
        var["beta_0"] = B

        # Trova i tale che delta = alpha^in/q con l'algoritmo di shanks
        
        a_n_su_q = G.exp(a,n//q)
        i = algo_shanks(G,n,a_n_su_q,delta)
        
        var["i"] = i
        
        A.append(i)
        
        termine1 = A[j]
        termine2 = G.exp(q,j)

        B = G.mul(B, G.exp(a,-G.mul(termine1,termine2)))
        var["beta_1"] = B
        exe.append(var)
    return exe,A

# Usando il teorema cinese del resto

def algo_pohlig(G,n,a,b):
    fattori = fattorizzazione(n)
    eq = []
    var = []
    for i in fattori.items():
        v,p = algo_pohlig_hellman(G,n,a,b,i[0],i[1])
        var.append(v)
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