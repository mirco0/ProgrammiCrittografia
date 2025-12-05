from Shanks import algo_shanks
from PohligHellman import algo_pohlig
from Gruppi import Group

print("Esercizio 7.1 Libro")
# Array di tuple con alpha, base, risultato
problemi = [ (24691,106,12375), (458009,6,248388)]
for n,base,y in problemi:
    G = Group(n)
    log = algo_shanks(G,n-1,base,y)
    print(f"Il log_{base}({y}) mod {n} = {log}")

print("Esercizio 7.5 Libro")
problemi = [ (28703,5,8563), (31153,10,12611)]
for n,base,y in problemi:
    G = Group(n)
    log = algo_pohlig(G,n-1,base,y)
    print(f"Il log_{base}({y}) mod {n} = {log}")


