from perm import perm

#TODO: creare implementazione che lavora con dati in binario (più efficiente)
class Cifrario_SPN:
    
    K = [
        [0,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0],
        [1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1],
        [1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0],
        [0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1],
        [1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1]
    ]
    
    class Key:
        pass
    
    def xor(self,a,b):
        c = []
        for i in range(len(a)):
            v = 0 if str(a[i]) == str(b[i]) else 1 
            c.append(v)
        return c

    def generate_key_schedule(self):
        pass
    
    # pag 106
    def s(self,x):
        s = []
        for i,c in enumerate(x):
            if(i % 4 == 0):
                s.append(' ')
            s.append(str(c))
        return ''.join(s)

    def SPN(self,x):
        N = self.N
        w = x
        
        for r in range(0,self.N-1):
            v = []
            print(f"w_{r} {self.s(w)}")
            print(f"K_{r+1} {self.s(self.K[r])}")
            u = self.xor(w,self.K[r])
            print(f"u_{r+1} {self.s(u)}")

            for i in range(0,self.m):
                sottolista = u[(i*self.l):(i+1)*self.l]
                stringa = ''.join(map(str,sottolista))
                sost = self.Ps.get_item(stringa)
                v.extend(list(sost))
            
            w = []
            for index in range(len(v)):
                # Sistema sfasamento tra la funzione di permutazione 1-16 e gli indici python 0-15
                j = self.Pp.get_item(index) 
                w.append(v[j])

            print(f"v_{r+1} {self.s(v)}")
        
        v = []
        u = self.xor(w,self.K[N-1])
        print(f"K_{N} {self.s(self.K[N-1])}")
        # exit(0)


        for i in range(0,self.m):
            sottolista = u[(i*self.l):(i+1)*self.l]
            stringa = ''.join(map(str,sottolista))
            sost = self.Ps.get_item(stringa)
            v.extend(list(sost))
        
        print(f"v_{N} {self.s(v)}")

        # print(v)
        print(f"K_{N+1} {self.s(self.K[N])}")
        return self.xor(v,self.K[N])
            # print()
            # for j in range(1,self.l * self.m +1):
            #     w[r].append(self.Pp.get(v[r])) 


    def __init__(self,N,l,m):
        self.key_schedule = []
        self.Pp = perm()
        self.Ps = perm()
        self.N = N
        self.l = l
        self.m = m