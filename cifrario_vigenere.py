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


    K = K("")

    def set_K(self, K):
        self.K.value = K
    
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
    freq_english = {
    'A': 0.082,
    'B': 0.015,
    'C': 0.028,
    'D': 0.043,
    'E': 0.127,
    'F': 0.022,
    'G': 0.020,
    'H': 0.061,
    'I': 0.070,
    'J': 0.002,
    'K': 0.008,
    'L': 0.040,
    'M': 0.024,
    'N': 0.067,
    'O': 0.075,
    'P': 0.019,
    'Q': 0.001,
    'R': 0.060,
    'S': 0.063,
    'T': 0.091,
    'U': 0.028,
    'V': 0.010,
    'W': 0.023,
    'X': 0.001,
    'Y': 0.020,
    'Z': 0.001

}
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

        return (ret,MCDs)

    # divide una stringa in d sottostringhe con gli elementi
    # y1 = y1ym+1y2m+1··· 
    def modulo_substring(self,M,d):
        substrings = [[] for _ in range(d)]
        for i in range(len(M)):
            substrings[i % d].append(M[i])
        
        for i in range(len(substrings)):
            substrings[i] = "".join(substrings[i])
        return substrings

    # Per indovinare la chiave è necessario sapere la lunghezza prima
    def guess_g_(self,M,d):
        key = []
        n_primo = len(M) / d
        
        # Calcolo M_g
        subs = self.modulo_substring(M,d)
        for sub in subs:
            text_freq = self.count_freq(sub)

            max_,letter = 0,0
            for g in range(26):
                M_g = 0
                for i,a in enumerate(self._a):
                    c = chr(((i + g) % 26) + ord('A'))
                    M_g += ((self.freq_english[a] * text_freq[c]))
                M_g /= (n_primo)

                if(M_g > max_):
                    max_ = M_g
                    letter = g
                print(f"{M_g:.4f}")
            print()
            key.append(chr(letter + ord('A')))

        return "".join(key)

    def best_index_of_coincidence(self,M,min_len,max_len):
        totale = []
        for i in range(min_len,max_len):
            substrings = self.modulo_substring(M,i)
            sub = []
            for subs in substrings:
                sub.append(self.index_of_coincidence(subs))
            totale.append(sub)

        # Calcola la media
        for i in range(len(totale)):
            totale[i] = sum(totale[i]) / len(totale[i])

        return totale
    
    #Indice di coincidenza per una singola stringa 
    def index_of_coincidence(self,M):
        # print(f"M{M}\n")
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
    
    # print(ca.kasiski_test(testo))

    print(ca.best_index_of_coincidence(testo,2,10))
    K = ca.guess_g_(testo,6)
    print(K)
    vigen.set_K(K)
    print(vigen.D(testo))