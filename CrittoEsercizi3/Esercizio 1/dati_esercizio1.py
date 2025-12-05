# File che genera i file latex necessari

import sys
import math
from Shanks import algo_shanks
from Gruppi import Group

# Esercizio 1
# Stinson Paterson 7.1

import sys

def capture_locals(func, *args, **kwargs):
    captured = {}

    def tracer(frame, event, arg):
        # Only trace the function we care about
        if frame.f_code is func.__code__ and event == "return":
            captured.update(frame.f_locals)
        return tracer

    sys.settrace(tracer)

    try:
        result = func(*args, **kwargs)
    finally:
        sys.settrace(None)

    return result, captured



def scrivi_dati_es7_1(file):
    
    n = 24691
    b = 106
    y = 12375

    G = Group(n)
    variables = capture_locals(algo_shanks,G,n-1,b,y)
    L1 = variables[1]["L1"]
    L2 = variables[1]["L2"]
    collision = variables[1]["collision"]
    cols = min(int(math.sqrt(len(L1))),7)


    #Generazione tabella 1

    with open(f"{file}_1.tex","w") as f:
    
        f.write(f"\\begin{{center}}\n\t\\begin{{tabular}}[h]{{*{{{cols}}}{{c}}}}\n    ")
        for i,pair in enumerate(L1):
            dato = (L1[pair],pair)
            if dato[1] == collision:
                f.write(f"$\\mathbf{{{dato}}}$")
            else:
                f.write(f"{dato}")

            if (i+1) % cols == 0 and i != len(L1)-1:
                f.write("\\\\\n    ")
            else:
                f.write("&")
        f.write("\n\t\\end{tabular}\n\\end{center}")


    #Generazione secondo file per la tabella 2
    with open(f"{file}_2.tex","w") as f:
        
        f.write(f"\\begin{{center}}\n\t\\begin{{tabular}}[h]{{*{{{cols}}}{{c}}}}\n    ")
        for i,pair in enumerate(L2):
            dato = (L2[pair],pair)
            if dato[1] == collision:
                f.write(f"$\\mathbf{{{dato}}}$")
            else:
                f.write(f"{dato}")

            if (i+1) % cols == 0 and i != len(L1)-1:
                f.write("\\\\\n    ")
            else:
                f.write("&")
        f.write("\n\t\\end{tabular}\n\\end{center}")


scrivi_dati_es7_1("../latex/tables/es1")