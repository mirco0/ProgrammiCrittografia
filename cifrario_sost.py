import random
class Cifrario_Sostituzione:
    class K:
        _K1 = {}
        _K2 = {}

        hide_unmapped = True

        def get(self, m):
            if m == '\n':
                return m
            
            default = m
            if self.hide_unmapped:
                default = "-"

            return self._K1.get(m,default)

        def get_inverse(self,M):
            if M == '\n':
                return M
            
            default = M
            if self.hide_unmapped:
                default = "-"

            return self._K2.get(M,default)


        def init_random(self):
            start = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            end = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            random.shuffle(end)
            for i in range(len(start)):
                self._K1[start[i]] = end[i]

        def update_keys(self):
            for a in self._K1.items():
                self._K2[a[1]] = a[0]

        def is_mapped(self,X):
            return X in self._K1 or X in self._K2
        
        def set_key(self,K):
            self._K1 = K
            self.update_keys()

        def map_char(self,M,m):
            self._K1[M] = m
            self._K2[m] = M

        def __str__(self):
            return f"{self._K1}"

    K = K()

    def E(self,m):
        R = []
        for m_ in m:
            R.append(self.K.get(m_))
        return "".join(R)

    def D(self,c):
        R = []
        for c_ in c:
            R.append(self.K.get_inverse(c_))
        return "".join(R)
    
    def force_key(self,M,m):
        self.K.map_char(M,m)

class Guesser:
    english_frq = {
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

    def count_freq(self,M):
        freq = {}
        total = 0
        for m in M:
            if( m != '\n' and m != ' '):
                total += 1
                freq[m] = freq.get(m,0) + 1 
        for k in freq.keys():
            freq[k] = freq[k] / total
        return freq

    #Riempe il resto della chiave con abbinamenti in base alla frequenza 
    def guess_key(self,M,K):

        message_freq = self.count_freq(M)
        # Lista ordinata di coppie (Lettera, Frequenza) per la lingua inglese
        FRQ_MESSAGE   = sorted(list(message_freq.items()),key=lambda x: x[1],reverse=True)
        # Lista ordinata di coppie (Lettera, Frequenza) per il messaggio
        FRQ_ENGLISH = sorted(list(self.english_frq.items()),key=lambda x: x[1],reverse=True)
        
        i = 0
        j = 0

        while i < len(FRQ_MESSAGE) and j < len(FRQ_ENGLISH):

            #Se la lettera UPPERCASE è stata già accoppiata 
            if(K.is_mapped(FRQ_MESSAGE[i][0])):
                i+=1
                continue
            
            #Se la lettera lowercase è stata già accoppiata
            if(K.is_mapped(FRQ_ENGLISH[j][0].lower())):
                j+=1
                continue
            
            K.map_char(FRQ_MESSAGE[i][0],(FRQ_ENGLISH[j][0]).lower())

            i+=1
            j+=1
        return K

if __name__ == "__main__":
    testo = '''
EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCK
QPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCG
OIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZU
GFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNS
ACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNC
IACZEJNCSHFZEJZEGMXCYHCJUMGKUCY'''

    sost = Cifrario_Sostituzione()
    # sost.K.hide_unmapped = False
    # Passo 1
    sost.force_key('F','w')
    sost.force_key('C','e')
    # Passo 2
    sost.force_key('Z','h')
    sost.force_key('N','l')
    # Passo 3
    sost.force_key('G','a')
    sost.force_key('Q','j')
    sost.force_key('Y','r')
    sost.force_key('S','o')
    # Passo 4
    sost.force_key('D','b')
    sost.force_key('K','s')
    sost.force_key('H','f')
    sost.force_key('A','v')
    # Passo 5
    sost.force_key('U','t')
    sost.force_key('W','g')
    sost.force_key('L','y')
    sost.force_key('I','d')

    sost.force_key('E','i') # Da algoritmo
    sost.force_key('O','n') # Da algoritmo
    # Passo 6
    sost.force_key('P','u')
    sost.force_key('M','m')
    sost.force_key('X','p')
    sost.force_key('J','c')


    # guesser = Guesser()
    # guesser.guess_key(testo,sost.K)
    
    print(sost.E(testo))