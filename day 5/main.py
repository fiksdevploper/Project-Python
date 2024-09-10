# Pengingat Catatan Harian
catatan = {}
# tambahkan tanggal,bulan,dan tahun pembuatan catatan
def tambah_catatan():
    tanggal = input("Masukkan tanggal (DD-MM-YYYY): ")
    catatan[tanggal] = input("Masukkan catatan Anda: ")
    print("Catatan berhasil ditambahkan!")
# jika data tidak di temukan maka code ini akan
def lihat_catatan():
    tanggal = input("Masukkan tanggal (DD-MM-YYYY): ")
    if tanggal in catatan:
        print("Catatan Anda pada", tanggal, ":", catatan[tanggal])
    else:
        print("Catatan untuk tanggal tersebut tidak ditemukan.")
# menu pilihan pengguna
while True:
    print("\nPilih tindakan:")
    print("1. Tambah Catatan") # jika pengguna ingin menambahkan tambah catatan maka pilih menu ini
    print("2. Lihat Catatan") # jika pengguna ingin melihat catatan maka pilih menu ini
    print("3. Keluar") # jika pengguna ingin keluar dari menu maka pilih nomor ini
    
    # menu pilihan 
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
