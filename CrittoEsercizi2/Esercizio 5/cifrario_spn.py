from perm import perm

class Cifrario_SPN:
    
    @staticmethod
    def xor(a,b):
        return a ^ b

    def generate_key_schedule(self):
        pass
    
    def get_value(self, v):
        bits = f'{v:0{self.l * self.m}b}'
        return ' '.join(bits[i:i+self.l] for i in range(0, len(bits), self.l))

    # pag 106
    def SPN(self,x):
        w = x
        
        for r in range(0,self.N-1):
            print(f"w_{r} {self.get_value(w)}")
            print(f"K_{r+1} {self.get_value(self.K[r])}")
            
            u = self.xor(w,self.K[r])
            
            print(f"u_{r+1} {self.get_value(u)}")

            # Sostituzione
            v = 0
            for i in range(0,self.m):
                block = (u >> (i*self.l) ) & ((1 << self.l) - 1)
                subst = self.Ps.get_item(block)
                v |= (subst << (self.l * i))    

            # Permutazione
            w = 0
            for i in range(self.l * self.m):
                bit = (v >> i) & 1
                j = self.Pp.get_item(i)
                w |= (bit << j)
            
            print(f"v_{r+1} {self.get_value(v)}")
        
        u = self.xor(w,self.K[self.N-1])
        print(f"K_{self.N} {self.get_value(self.K[self.N-1])}")

        v = 0
        for i in range(0,self.m):
            block = (u >> (i*self.l) ) & ((1 << self.l) - 1)
            subst = self.Ps.get_item(block)
            v |= (subst << (self.l * i))

        print(f"v_{self.N} {self.get_value(v)}")
        print(f"K_{self.N+1} {self.get_value(self.K[self.N])}")

        return self.xor(v,self.K[self.N])


    def __init__(self,N,l,m):
        self.key_schedule = []
        self.Pp = perm()
        self.Ps = perm()
        self.N = N
        self.l = l
        self.m = m 