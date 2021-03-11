import random

s8 = 0
s7 = 0 

for i in range(20):
    kocka = random.randint(1,6)
    kocka2 = random.randint(1,6)
    dobás = kocka + kocka2
    print(dobás)
    if dobás == 8:
        s8 = s8 + 1
    if dobás == 7:
        s7 = s7 + 1      
print('nyolcas', s8)        
print('hetes', s7)       

