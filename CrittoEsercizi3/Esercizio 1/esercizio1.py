from Shanks import algo_shanks
from Gruppi import Group

n = 24691
base = 106
y = 12375

G = Group(n)
log = algo_shanks(G,n,base,y)

print(log)

# È un po' lento (15 secondi) ma sembra funzionare
n = 458009
base = 6
y = 248388

G = Group(n)
log = algo_shanks(G,n,base,y)

print(log)