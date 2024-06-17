# project menghitung faktorial menggunakan bahasa pemerograman python
def hitung_faktorial():
    num = int(input("Masukkan angka bilangan: "))
    faktorial = 1
    
    if num < 0:
        print("Faktorial tidak terdefinisi untuk bilangan negatif")
    elif num == 0:
        print("Faktorial dari 0 adalah 1")
    else:
        for i in range(1, num + 1):
            faktorial *= i
        print("Faktorial dari", num, "adalah", faktorial)
# hitung faktorial
hitung_faktorial()