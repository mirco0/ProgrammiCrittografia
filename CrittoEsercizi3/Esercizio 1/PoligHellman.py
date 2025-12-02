from Shanks import algo_shanks
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

#TODO: da finire da implementare
def algo_pohlig_hellman(G,n,a,b,q,c):
    B = [ 0 for _ in range(c)]
    B[0] = b
    for j in range(c):
        delta = G.exp(B[j],n/G.exp(q,j+1))
        #Trova i tale che delta = alpha^in/q con l'algoritmo di shanks
        i = algo_shanks(G,G.exp(a,n/q),delta)

        A[j] = i
        B[j+1] = B[j] * G.exp(a,-A[j]*G.exp(q,j))
    return A

# def pohlig_algo_(G,n,a,b):
#     fattori = fattorizzazione(n)
    # for():
        