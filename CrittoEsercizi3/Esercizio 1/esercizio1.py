from Shanks import algo_shanks
from PohligHellman import algo_pohlig
from Gruppi import Group

# 7.1
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
# log = algo_shanks(G,n,base,y)

print(log)
print("7.5")


# 7.5

n = 28703
base = 5
y = 8563

G = Group(n)
log = algo_pohlig(G,n-1,base,y)

print(log)


n = 31153
base = 10
y = 12611

G = Group(n)
log = algo_pohlig(G,n-1,base,y)

print(log)

