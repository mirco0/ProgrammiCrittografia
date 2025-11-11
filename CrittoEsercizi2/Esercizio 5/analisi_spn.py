from perm import perm

#TODO: Cambiare implementazione per lavorare con stringhe binarie
class CrittoAnalisiSPN:

    def genera_SBOX_table(self,perm):
        table = []
        size = len(perm.domain)
        for i in range(size):
            line = []
            start = [int(x) for x in list(f'{i:0{4}b}')]
            c = perm.get_item(i)
            end = [int(x) for x in list(f'{c:0{4}b}')]
            line.extend(start)
            line.extend(end)
            table.append(line)
        return table
    
    def calcola_NL_table(self, sbox):
        table = []
        variables = len(sbox[0]) // 2
        for a in range(2**variables):
            a_arr = [int(x) for x in list(f'{a:0{variables}b}')]
            line = []
            for b in range(2**variables):
                # Workaround prende la rappresentazione binaria e la trasforma in array
                b_arr = [int(x) for x in list(f'{b:0{variables}b}')]
                line.append(self.calcola_NL(a_arr,b_arr,sbox))
            table.append(line)
        return table

    def calcola_NL(self,i,j,sbox_table):
        NL = 0
        for line in sbox_table:
            m = 1
            for index in range(len(i)):
                m += i[index] * line[index]
                m+= j[index] * line[index+len(i)]
            NL += (m % 2)
        return NL
    
    def latex_table(self, table, header=[], side=[], name="table.tex"):

        n = len(table)
        cols = len(table[0]) if table else 0
        try:
            with open(f"../latex/{name}", "x",encoding="utf-8") as f:

                total_cols = cols + (1 if side else 0)
                f.write(f"\\begin{{table}}[h]\n\t\\centering\n")
                
                f.write(f"\t\\begin{{tabular}}{{|*{{{total_cols}}}{{c|}}}}\n")
                f.write("\t\t\\hline\n")

                # Scrivi titoli
                if header:
                    if side:
                        f.write("\t\t & " + " & ".join(header) + " \\\\\n")
                    else:
                        f.write("\t\t"+"& ".join(header) + " \\\\\n")
                    f.write("\t\t\\hline\n")

                #Scrivi contenuto
                for i, row in enumerate(table):
                    if side:
                        f.write(f"\t\t{side[i]} & " + " & ".join(str(x) for x in row) + " \\\\\n")
                    else:
                        f.write("\t\t" + "& ".join(str(x) for x in row) + " \\\\\n")
                    f.write("\t\t\\hline\n")

                f.write("\t\\end{tabular}\n")
                f.write("\\end{table}\n")
        except:
            print(f"File '/latex/{name}' esistente")
