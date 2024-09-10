print ("# Program Python Persegi Panjang Bintang #")
print ("==========================================")

print ()

tinggi_persegi = int(input("Input tinggi persegi: "))
lebar_persegi = int(input("Input lebar persegi: "))

print ()

for i in range (tinggi_persegi):
    for j in range (lebar_persegi):
        print ("*", end = '')
    print ()
