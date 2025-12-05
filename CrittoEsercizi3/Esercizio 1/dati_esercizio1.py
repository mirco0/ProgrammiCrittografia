# File che genera i file latex necessari

import sys
import math
from Shanks import algo_shanks
from PohligHellman import algo_pohlig
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
    
    p = 24691
    b = 106
    y = 12375

    G = Group(p)
    variables = capture_locals(algo_shanks,G,p-1,b,y)
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

def scrivi_dati_es7_5(file):
    with open(f"{file}.tex","w") as f:
            
        p = 28703
        b = 5
        y = 8563

        G = Group(p)
        variables = capture_locals(algo_pohlig,G,p-1,b,y)

        # Punto 1 dell'esercizio
        for j,dati in enumerate(variables[1]["var"]):
            f.write(f"Test per il fattore $q = {dati[0]['exp']}$ $c = {len(dati)}$\n")
            f.write("\\begin{center}\n    \\begin{tabular}{@{}lccl@{}}\n        \\toprule\n        Step & Variabile & & Valore \\\\ \n        \\midrule\n        ")
            for index,variabili in enumerate(dati):
                f.write(f"        {index} & $\\beta_{{{index}}}$ & $=$ &${variabili['beta_0']}$\\\\\n")
                f.write(f"        &$\\delta$ & $=$ & ${{{variabili['beta_0']}^{{{variabili['n']}/{{{variabili['exp']}}}}}}}$\\\\\n")
                f.write(f"        &$a_{{{index}}}$ & $=$ & ${variabili['i']}$\\\\\n")
                f.write(f"        &$\\beta_{{{index+1}}}$ & $=$ & ${variabili['beta_1']}$\\\\\n")
                if index != len(dati)-1:
                    f.write(f"        \\midrule")
            f.write("        \\bottomrule\n    \\end{tabular}\\end{center}\n")
        
        
    # Punto 2 dell'esercizio
    with open(f"{file}_2.tex","w") as f:
        p = 31153
        b = 10
        y = 12611
        

        G = Group(p)
        variables = capture_locals(algo_pohlig,G,p-1,b,y)

        for j,dati in enumerate(variables[1]["var"]):
            f.write(f"Test per il fattore $q = {dati[0]['exp']}$ $c = {len(dati)}$\n")
            f.write("\\begin{center}\n    \\begin{tabular}{@{}lccl@{}}\n        \\toprule\n        Step & Variabile & & Valore \\\\ \n        \\midrule\n        ")
            for index,variabili in enumerate(dati):
                f.write(f"        {index} & $\\beta_{{{index}}}$ & $=$ &${variabili['beta_0']}$\\\\\n")
                f.write(f"        &$\\delta$ & $=$ & ${{{variabili['beta_0']}^{{{variabili['n']}/{{{variabili['exp']}}}}}}}$\\\\\n")
                f.write(f"        &$a_{{{index}}}$ & $=$ & ${variabili['i']}$\\\\\n")
                f.write(f"        &$\\beta_{{{index+1}}}$ & $=$ & ${variabili['beta_1']}$\\\\\n")
                if index != len(dati)-1:
                    f.write(f"        \\midrule")
            f.write("        \\bottomrule\n    \\end{tabular}\\end{center}\n")

scrivi_dati_es7_5("../latex/tables/es1_5")
# scrivi_dati_es7_1("../latex/tables/es1")