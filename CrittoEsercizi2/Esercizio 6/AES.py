
# https://legacy.cryptool.org/en/cto/aes-step-by-step

class AES:
    SBOX =  [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,0x54, 0xbb, 0x16    
    ]

    def __init__(self,N,key):
        self.N = N
        self.key = key
        #Prendo 11 chiavi anche se non necessarie
        self.KeyExpansion(key,N=10)

    # Per prendere byte a un indice specifico, per mantenere il resto del codice coerente con il libro
    def KeyAtByteNumber(self,key,byte_num):
        shift = (128 - 8) - byte_num*8
        return (key >> shift) & 0xFF

    # Restituisce b0|b1|b2|b3 in 32 bit 
    def MergeBytes(self,b0,b1,b2,b3):
        key = 0
        key = key | b3 
        key = key | (b2 << 8)
        key = key | (b1 << 16)
        key = key | (b0 << 24)
        return key

    def SubWord(self,word):
        subword = 0
        for i in range(4):
            shift = (24 - 8 * i)
            byte = (word >> shift) & 0xFF
            new_byte = self.SBOX[byte]
            subword |= new_byte << shift
        
        return subword

    def RotWord(self,word):
        b0 = (word >> 24) & 0xFF
        return b0 | word << 8

    def KeyExpansion(self,key,N=None):
        # Mantengo le 11 chiavi come dall codice del libro (anche se solo 3 saranno necessarie) 
        keys = N+1 if N else self.N+1

        w = [ 0 for _ in range(keys*4)]

        RCON = [None, 0x01000000,0x02000000,0x04000000,0x08000000,0x10000000,0x20000000,0x40000000,0x80000000,0x1B000000,0x36000000]
        for i in range(4):
            b0 = self.KeyAtByteNumber(key,4*i)
            b1 = self.KeyAtByteNumber(key,4*i+1)
            b2 = self.KeyAtByteNumber(key,4*i+2)
            b3 = self.KeyAtByteNumber(key,4*i+3)
            w[i] = self.MergeBytes(b0,b1,b2,b3)
            
        for i in range(4,keys*4):
            temp = w[i-1]
            if i % 4 == 0:
                temp = self.SubWord(self.RotWord(temp)) ^ RCON[i//4]
            w[i] = w[i-4] ^ temp
        
        self.key_schedule = []
        for i in range(keys):
            self.key_schedule.append((w[4*i],w[4*i+1],w[4*i+2],w[4*i+3]))


    def Encript(self, x):        
        state = self.InitState(x)
        self.AddRoundKey(self.key_schedule[0])

        for i in range(self.N-1):
            print(f"Round: {i+1}")
            key = self.key_schedule[i+1]
            print(self.print_state())
            self.SubBytes()
            print(self.print_state())
            self.ShiftRows()
            print(self.print_state())
            self.MixColumns()
            print(self.print_state())
            self.AddRoundKey(key)
            print(self.print_state())

        key = self.key_schedule[self.N]
        self.SubBytes()
        self.ShiftRows()
        self.AddRoundKey(key)
        return self.print_state()

    def print_state(self):
        state = self.state
        out = []
        for r in range(4):
            for c in range(4):
                out.append(state[c][r])
        return ''.join(f'{b:02x}' for b in out)


    def InitState(self,x):
        self.state = [ [ 0 for _ in range(4)] for _ in range(4)]
        shift = 128 - 8
        
        for i in range(16):
            col = i // 4
            row = i % 4
            byte = (x >> shift) & 0xFF
            shift -= 8
            self.state[row][col] = byte

    #Prende i byte dalla parola e li sostituisce con i corrispettivi nella sbox
    def SubBytes(self):
        for i in range(4):
            for j in range(4):
                self.state[i][j] = self.SBOX[self.state[i][j]]

    def ShiftRows(self):
        for r in range(1, 4):
            self.state[r] = self.state[r][r:] + self.state[r][:r]

    def AddRoundKey(self, round_key):
        for c in range(4):
            word = round_key[c]
            for r in range(4):
                byte = (word >> (24 - 8 * r)) & 0xFF
                self.state[r][c] ^= byte

    def galois_multiplication(self, a, b):
        p = 0
        for counter in range(8):
            if b & 1: p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            # keep a 8 bit
            a &= 0xFF
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p

    def MixColumns(self):
        for c in range(4):
            col = [self.state[r][c] for r in range(4)]
            col = self.MixColumn(col)
            for r in range(4):
                self.state[r][c] = col[r]

    def MixColumn(self, column):
        mult = [2, 1, 1, 3]
        cpy = list(column)
        g = self.galois_multiplication

        column[0] = g(cpy[0], mult[0]) ^ g(cpy[3], mult[1]) ^ \
                    g(cpy[2], mult[2]) ^ g(cpy[1], mult[3])
        column[1] = g(cpy[1], mult[0]) ^ g(cpy[0], mult[1]) ^ \
                    g(cpy[3], mult[2]) ^ g(cpy[2], mult[3])
        column[2] = g(cpy[2], mult[0]) ^ g(cpy[1], mult[1]) ^ \
                    g(cpy[0], mult[2]) ^ g(cpy[3], mult[3])
        column[3] = g(cpy[3], mult[0]) ^ g(cpy[2], mult[1]) ^ \
                    g(cpy[1], mult[2]) ^ g(cpy[0], mult[3])
        return column

