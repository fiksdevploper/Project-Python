print ("# Algoritma persegi Deret Angka Pada Python #")
print ("=============================================")
print ()

besar_persegi = int(input("Input besar persegi: "))
print ()

k = 1
for i in range(1,besar_persegi+1):
    for j in range (1,besar_persegi+1):
        print (k, '', end = '', sep='')
        k = k + 1
    print ('')