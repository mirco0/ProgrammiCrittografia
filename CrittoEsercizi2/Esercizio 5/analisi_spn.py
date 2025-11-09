class CrittoAnalisiSPN:
    inp = [
        [0,0,0,0,1,1,1,0],
        [0,0,0,1,0,1,0,0],
        [0,0,1,0,1,1,0,1],
        [0,0,1,1,0,0,0,1],
        [0,1,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1],
        [0,1,1,0,1,0,1,1],
        [0,1,1,1,1,0,0,0],
        [1,0,0,0,0,0,1,1],
        [1,0,0,1,1,0,1,0],
        [1,0,1,0,0,1,1,0],
        [1,0,1,1,1,1,0,0],
        [1,1,0,0,0,1,0,1],
        [1,1,0,1,1,0,0,1],
        [1,1,1,0,0,0,0,0],
        [1,1,1,1,0,1,1,1]
    ]

    def calcola_NL_table(self, sbox):
        table = []
        variables = len(sbox[0]) // 2
        for a in range(2**variables):
            a_arr = [int(x) for x in list(f'{a:0{variables}b}')]
            line = []
            for b in range(2**variables):
                # Workaround prende la rappresentazione binaria e la trasforma in array
                b_arr = [int(x) for x in list(f'{b:0{variables}b}')]
                line.append(self.calcola_NL(a_arr,b_arr))
            table.append(line)
        return table

    def calcola_NL(self,i,j):
        NL = 0
        for line in self.inp:
            m = 1
            for index in range(len(i)):
                m += i[index] * line[index]
                m+= j[index] * line[index+len(i)]
            NL += (m % 2)
        return NL

cr = CrittoAnalisiSPN()
print(cr.calcola_NL_table(cr.inp))