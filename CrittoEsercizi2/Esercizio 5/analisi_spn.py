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
i = [0,1,0,1]
j = [0,0,0,1]
print(cr.calcola_NL(i,j))