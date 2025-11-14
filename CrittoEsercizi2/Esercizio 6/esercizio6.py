from AES import AES

N = 2
key = 0x2B7E151628AED2A6ABF7158809CF4F3C
x   = 0x3243F6A8885A308D313198A2E0370734

aes = AES(N,key)

#Stampa key-schedule 
# for x in aes.key_schedule:
#     for h in x:
#         print(hex(h),end="")
#     print()

y = aes.Encript(x)

print(y)