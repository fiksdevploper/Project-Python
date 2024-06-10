# membuat program konfersi suhu sederan menggunakan python

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("pilih konversi suhu: ")
print("1. celcius ke fahrenheit")
print("2. fahrenheit ke celcius")

pilihan = input("masukan pilihan (1/2): ")

if pilihan == "1":
    celcius = float(input("masukan suhu dalam celcius: "))
    print(f"suhu dalam fahrenheit adalah {celsius_to_fahrenheit(celcius)}")
elif pilihan == "2":
    fahrenheit = float(input("masukan suhu dalam fahrenheit: "))
    print(f"suhu dalam celcius adalah {fahrenheit_to_celsius(fahrenheit)}")
else:
    print("pilihan tidak tersedia")