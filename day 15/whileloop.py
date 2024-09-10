# Inisialisasi variabel usia dengan nilai yang tidak valid
usia = 0 

# selama usia tidak dalam rentang yang vakud 

while usia < 1 or usia > 120:
    # Input usia
    usia = int(input("Masukkan usia anda (1-120): "))

    # Cetak usia
    print("Usia anda adalah: ", usia)