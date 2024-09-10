# membuat daftar kontak sederhana menggunakan python
kontak = {}
# tambahkan nama dan nomor telepon pengguna
def tambah_kontak(nama,nomor):
    kontak[nama] = nomor
    print("kontak berhasil ditambahkan")
# lihat semua kontak
def lihat_semua_kontak():
    if kontak:
        print("daftar kontak: ")
    for nama, nomor in kontak.items():
        print (f"{nama}, {nomor}")
    else:
        print("daftar kontak kosong")
def cari_kontak(nama):
    if nama in kontak:
        print("Nomor", nama, "adalah", kontak[nama])
    else:
        print("Kontak", nama, "tidak ditemukan")
# loop
while True:
    # menu pilihn pengguna
    print ("\nPilih Tindakan:") 
    print ("1. Tambah Kontak")
    print ("2. Lihat Kontak")
    print ("3. Cari Kontak")
    print ("4. Keluar")
    # pilihan pengguna
    pilihan = input("masukan pilihan (1/2/3/4): ")
    # jika pengguna  memilih nomor 1 maka menginputkan nama dan nomor
    if pilihan == "1":
        nama = input("masukan nama: ")
        nomor = input("masukan nomor: ")
        tambah_kontak(nama, nomor)
    # jika pengguna  memilih nomor 2 maka menampilkan semua kontak
    elif pilihan == "2":
        lihat_semua_kontak()
    # jika pengguna  memilih nomor 3 maka penggunak akan mencari nomor kontak
    elif pilihan == "3":
        nama = input("masukan nama kontak yang ingin dicari: ")
        cari_kontak(nama)
    # jika pengguna  memilih nomor 4 maka pengguna akan keluar
    elif pilihan == "4":
        print("terima kasih! Sampai jumpa kembali!")
        break
    # jika pengguna salah memasukan nama atau nomor telepon maka tuliasn di bawah ini akan muncul
    else:
        print("pilihan tidak valid. Mohon masukan pilihan yang sesuai.")