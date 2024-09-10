print ("# Algoritma Angka Pada Python #")
print ("===============================")
print ("")

besar_persegi = int(input("Input besar persegi: "))
print ("")

for i in range(1,besar_persegi+1):
    for j in range (1,besar_persegi+1):
        print (i, '', sep = '', end = '')
    print ('')
    