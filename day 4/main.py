# membuat program tebak angka terkecil > terbesar menggunakan python
import random

angka_rahasia = random.randint(1, 1000)
tebakan = None

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka antara 1 sampai 1000: "))
    
    if tebakan < angka_rahasia:
        print("Tebakan terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Tebakan terlalu besar")
    else:
        print("Tebakan anda benar")