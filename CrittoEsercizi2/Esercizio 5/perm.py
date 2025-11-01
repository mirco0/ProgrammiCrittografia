import random

# Implementazione della funzione di permutazione con inversa.
# È possibile impostare un 'dict' che definisce la permutazione 
# È possibile impostare un dominio e generare la permutazione casualmente 

class perm:

    def __init__(self, domain=[], is_identity=False):
        self._K1 = {}
        self._K2 = {}
        self.indexes = {}
        self.is_identity = is_identity
        self.apply_perm(domain)

    # funzioni di appoggio (usano l'indice degli oggetti)
    def get(self, m):
        m = self.indexes[m]
        return self._K1.get(m,None)

    def get_inverse(self,M):
        M = self.indexes[M]
        return self._K2.get(M,None)

    def get_item(self, m):
        return self.domain[self.get(m)]

    def get_inverse_item(self, M):
        return self.domain[self.get_inverse(M)]

    # crea una funzione di permutazione casuale sul dominio
    def init_random(self):
        items = range(1,self.size+1)
        random.shuffle(items)
        for i in range(1,self.size+1):
            self._K1[i] = items[i]

    def update_keys(self):
        for a in self._K1.items():
            self._K2[a[1]] = a[0]
    
    def set_key(self,perm):
        for key in perm.keys():
            self.domain.append(key)

        self.apply_perm(self.domain)

        for item in perm.items():
            self.map_item(item[0],item[1])

    def map_item(self,M,m):
        start = self.indexes[M]
        end = self.indexes[m]
        self._K1[start] = end
        self._K2[end] = start

    def apply_perm(self, domain):
        self.domain = domain
        for i,item in enumerate(domain):
            self.indexes[item] = i 
        self.domainsize = len(domain)

    def __str__(self):
        return f"{self._K1}"