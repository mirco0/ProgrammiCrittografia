from math import gcd
from functools import reduce

class Cifrario_Viginere:
    class K:
        value = ""
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def __init__(self,value):
            self.value = value.upper()

        def get(self, m, index):
            K_i = index % len(self.value)
            c_value = (ord(m) + ord(self.value[K_i])) % 26
            return self.a[c_value]

        def get_inverse(self, M, index):
            K_i = index % len(self.value)
            c_value = (ord(M) - ord(self.value[K_i])) % 26
            return self.a[c_value].lower()


    K = K("VERME")

    def E(self,m):
        R = []
        for i,m_ in enumerate(m):
            R.append(self.K.get(m_,i))
        return "".join(R)

    def D(self,c):
        R = []
        for i,c_ in enumerate(c):
            R.append(self.K.get_inverse(c_,i))
        return "".join(R)
    
class CrittoAnalisi:

    _a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def count_freq(self, M):
        freq = {}
        for a in self._a:
            freq[a] = 0
        for m in M:
            freq[m] = freq.get(m,0) + 1
        return freq

    #Test di Kasiski, data una sottosequenza cerca numero di occorrenze, e restituisce le posizioni
    def search_count(self,sub, M):
        count = 0
        pos = []
        n, m = len(sub), len(M)
        for i in range(m - n + 1):
            if M[i:i + n] == sub:
                pos.append(i)
        return pos

    
    def kasiski_test(self,M):
        freq = {}
        for i in range(len(M)):
            for j in range(0,i-1):
                count = self.search_count(M[j:i],M)
                if len(count) > 2 or ( j - i > 3 and len(count) > 1):
                    freq[M[j:i]] = count

        #Ordino gli elementi trovati per lunghezza
        # print(freq.items()[0])
        ret = list(sorted(list(freq.items()), key=lambda x: len(x[0]), reverse=True))
        
        # Prendiamo le posizioni dei tesi, e calcoliamo MCD con le distanze 

        MCDs = []
        for i in range(len(ret)):
            e = ret[i][1]
            nums = []
            for j in e[1:]:
                nums.append(j - e[0])
            MCDs.append(reduce(gcd,nums))

        return ret

    # divide una stringa in d sottostringhe con gli elementi
    # y1 = y1ym+1y2m+1··· 
    def modulo_substring(self,M,d):
        substrings = [[] for _ in range(d)]
        for i in range(len(M)):
            substrings[i % d].append(M[i])
        
        for i in range(len(substrings)):
            substrings[i] = "".join(substrings[i])
        return substrings

    def best_index_of_coincidence(self,M,min_len,max_len):
        totale = []
        for i in range(min_len,max_len):
            substrings = self.modulo_substring(M,i)
            sub = []
            for subs in substrings:
                sub.append(self.index_of_coincidence(subs))
            totale.append(sub)

        for i in range(len(totale)):
            totale[i] = sum(totale[i]) / len(totale[i])
        return totale
    
    #Indice di coincidenza per una singola stringa 
    def index_of_coincidence(self,M):
        print(f"M{M}\n")
        n = len(M)
        f = self.count_freq(M)
        sum_ = 0
        for i in range(26):
            sum_ += (f[self._a[i]]) * (f[self._a[i]] - 1)
        return sum_ / (n*(n-1))
    
if __name__ == "__main__":
    testo = '''KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'''

    vigen = Cifrario_Viginere()
    ca = CrittoAnalisi()
    print(ca.kasiski_test(testo))
    print(ca.best_index_of_coincidence(testo,2,10))
    # print(vigen.D(testo))