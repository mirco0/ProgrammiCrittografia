#Codice per eseguire la crittoanalisi

from analisi_spn import CrittoAnalisiSPN
from perm import perm

cr = CrittoAnalisiSPN()

# Creo oggetto `perm` con la permutazione dall'esercizio 
PI_S_Primo = {
    '0':'8',
    '1':'4',
    '2':'2',
    '3':'1',
    '4':'C',
    '5':'6',
    '6':'3',
    '7':'D',
    '8':'A',
    '9':'5',
    'A':'E',
    'B':'7',
    'C':'F',
    'D':'B',
    'E':'9',
    'F':'0',
}

PS1 = {}
for a in PI_S_Primo.items():
    k = int(a[0],16)
    v = int(a[1],16)
    PS1[k] = v


PI_S = perm()
PI_S.set_key(PS1)

table = cr.genera_SBOX_table(PI_S)

# Tabella SBOX in latex
header=["$X_1$","$X_2$","$X_3$","$X_4$","$Y_1$","$Y_2$","$Y_3$","$Y_4$"]
cr.latex_table(table,name="tables/perm_table.tex",header=header)

#Tabella linear approximation in latex
linear_app = cr.calcola_NL_table(table)
header=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
side=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
cr.latex_table(linear_app,name="tables/linear_approximation.tex",header=header,side=side)


