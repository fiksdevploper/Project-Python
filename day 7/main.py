# project To-do list menggunakan bahasa pemerograman Python

tugas = []
# tugas di tambahkan
def tambah_tugas():
    tugas_baru = input("Masukkan tugas baru: ")
    tugas.append(tugas_baru)
    print("Tugas baru telah ditambahkan.")
# lihat tugas pada daftar
def lihat_tugas():
    if tugas:
        print("Daftar Tugas: ")
        for i, t in enumerate(tugas, start=1):
            print(f"{i}. {t}")
    else:
        print("Tidak ada tugas yang di tambahkan. ")
# hapus tugas pada daftar
def hapus_tugas():
    lihat_tugas()
    nomor = int(input("Masukkan nomor tugas yang ingin di hapus: "))
    if 0 < nomor <= len(tugas):
        tugas.pop(nomor - 1)
        print("Tugas telah di hapus.")
    else:
        print("Tugas tidak ditemukan.")

# menu pilihan
while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid. ")
# code end