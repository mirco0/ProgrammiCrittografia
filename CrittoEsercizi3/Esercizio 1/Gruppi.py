# Implementazione semplice per esponenziazione e inversa moltiplicativa
class Group:
    def __init__(self, n):
        self.n = n

    def exp(self, base, power):
        if (power < 0):
            return self.inverse(self.exp(base,-power))
        return (base ** power) % self.n
    
    def inverse(self, a):
    # Algoritmo euclideo
        n = self.n
        y = 0
        x = 1

        while (a > 1): 
            q = a // n
            t = n

            n = a % n
            a = t
            t = y

            y = x - q * y
            x = t

        if (x < 0):
            x += self.n

        return x;