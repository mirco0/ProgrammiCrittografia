from cifrario_spn import Cifrario_SPN 

cifrario = Cifrario_SPN(4,4,4)


# Esempio 4.1 TODO: terminare
PS = {
    '0': 'E',
    '1': '4',
    '2': 'D',
    '3': '1',
    '4': '2',
    '5': 'F',
    '6': 'B',
    '7': '8',
    '8': '3',
    '9': 'A',
    'A': '6',
    'B': 'C',
    'C': '5',
    'D': '9',
    'E': '0',
    'F': '7'
} 

# trasforma le permutazioni per lavorare con le stringhe binarie al posto delle stringhe esadecimali
PS1 = {}
for a in PS.items():
    # k = f'{int(a[0],16):0>4b}'
    k = int(a[0],16)
    v = int(a[1],16)

    # v = f'{int(a[1],16):0>4b}'
    PS1[k] = v

PP = {
    '1':  '1',
    '2':  '5',
    '3':  '9',
    '4':  '13',
    '5':  '2',
    '6':  '6',
    '7':  '10',
    '8':  '14',
    '9':  '3',
    '10': '7',
    '11': '11',
    '12': '15',
    '13': '4',
    '14': '8',
    '15': '12',
    '16': '16'
}

PP1 = {}
for a in PP.items():
    k = int(a[0]) - 1
    v = int(a[1]) - 1
    PP1[k] = v


cifrario.Ps.set_key(PS1)
cifrario.Pp.set_key(PP1)

plain_text = 0b0010011010110111


K = [
    0b0011101010010100,
    0b1010100101001101,
    0b1001010011010110,
    0b0100110101100011,
    0b1101011000111111
]
cifrario.K = K
print(f" y {cifrario.get_value(cifrario.SPN(plain_text))}")
