from perm import perm

class Cifrario_SPN:
    
    class Key:
        pass
    
    def generate_key_schedule(self):
        pass
    
    # pag 106
    def SPN(self,x,pS,Pp,keys):
        w_0 = x
        pass

    def __init__(self,N,l,m):
        self.key_schedule = []
        self.Pp = perm()
        self.Ps = perm()
        self.N = N
        self.l = l
        self.m = m