# Pengingat Catatan Harian

catatan = {}

def tambah_catatan():
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    catatan[tanggal] = input("Masukkan catatan Anda: ")
    print("Catatan berhasil ditambahkan!")

def lihat_catatan():
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    if tanggal in catatan:
        print("Catatan Anda pada", tanggal, ":", catatan[tanggal])
    else:
        print("Catatan untuk tanggal tersebut tidak ditemukan.")

while True:
    print("\nPilih tindakan:")
    print("1. Tambah Catatan")
    print("2. Lihat Catatan")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        tambah_catatan()
    elif pilihan == '2':
        lihat_catatan()
    elif pilihan == '3':
        print("Terima kasih! Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Mohon masukkan angka 1, 2, atau 3.")
