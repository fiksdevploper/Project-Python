# membuat game sederhana otherspy menggunakan python
import random 
welcome_message = "Otherspy Games!"
otherspy_posisi = random.randint(1,5)

# print (welcome_message)
print ("***************************")
print (f"******{welcome_message}******")
print ("***************************")

# nama pengguna
nama_pengguna = input ("Siapa Nama Kamu ? ")

# print nama pengguna
print(f'''Hallo, Selamat Datang! {nama_pengguna} Coba perhatikan lubang di bawah ini
|_| |_| |_| |_| |_|
''')

# lubang others berada pada nomor
pilihan_pengguna = int(input("Menurut kamu, di mana otherspy berada [1,2,3,4,5] ? "))

# konfirmasi pengguna
konfirmasi_pengguna = input (f"apakah kamu yaki otherspy berada di lubang nomor {pilihan_pengguna} ? (ya/tidak) ")

# logic konfirmasi
# jika user memilih "ya" maka jawaban akan di lanjut seperti ini
if konfirmasi_pengguna == "ya":
    print ("Ok, Mari kita lihat hasil jawaban kamu")

# dan, jika user memilih "Tidak" maka user akan mengulang input lubang others
else:
    pilihan_pengguna = int(input("Coba tebak lagi kamu hanya memiliki 1 kesempatan lagi , di mana otherspy berada [1,2,3,4,5] ? "))

# logic
# jika pilihan pengguna benar
if pilihan_pengguna == otherspy_posisi:
    print(f"Selamat {nama_pengguna}, Tebakan Kamu benar! posisi otherspy berada di lubang nomor{otherspy_posisi}!")
else:
    print(f"Kamu salah, otherspy berada di {otherspy_posisi}, sedangkan kamu memilih nomor {pilihan_pengguna}!")
