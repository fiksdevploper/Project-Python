# project penghiyung kalori makanan menggunakan bahasa pemerograman python

kalori_makanan = {
    "ayam" : 100,
    "gandum" : 150,
    "coklat" : 250,
    "susu" : 300,
    "telur ayam" : 400,
    "sapi" : 200,
    "ikan" : 300,
    "udang" : 350,
    "kangkung" : 300,
    "kacang tanah" : 400,
    "wortel" : 300,
    "kentang" : 300,
    "kacang hijau" : 400,
    "kacang polong" : 400,
    "kacang merah" : 400,
    "kacang tanah hijau" : 400,
    "kacang tanah merah" : 400,
    "kacang tanah putih" : 400,
    "kambing" : 400,
    "bebek" : 500,
    "buah" : 600,
    "sayur" : 700,
    "nasi" : 800,
    "untak" : 900,
    "telur bebek" : 900
}

total_kalori = 0

def tambah_makanan():
    global total_kalori
    makanan = input("masukan makanan yang ingin ditambahkan: ")
    if makanan in kalori_makanan:
        total_kalori += kalori_makanan[makanan]
        print(f"{makanan} ditambahkan. Total kalori sekarang: {total_kalori}")
    else:
        print("makanan yang anda maksud tidak ada di daftar")

def lihat_total_kalori():
    print(f"total kalori sekarang: {total_kalori}")

while True:
    print("pilih tindakan: ")
    print("1. tambah makanan")
    print("2. lihat total kalori")
    print("3. keluar")
    pilihan = input("masukan pilihan (1/2/3): ")
    if pilihan == "1":
        tambah_makanan()
    elif pilihan == "2":
        lihat_total_kalori()
    elif pilihan == "3":
        print("terima kasih! sampai jumpa kembali!")
        break
    else:
        print("pilihan tidak valid. silahkan masukan pilihan yang sesuai.")