nim = [0,0,1,2,2,6,9]
n = len(nim)

penjumlahanData = 0

for i in nim:
    penjumlahanData += i

print("hasil penjumalahan data :",penjumlahanData)
print("n :",n)

print("<------------------------->")
#mencari mean

x = penjumlahanData/n
print("Mean :",x)

#mencari median
if n % 2 != 0:
    dataGanjil =(n+1)/2
    median = nim[int(dataGanjil)]
else:
    #genap
    pass


print("Jadi median berada pada angka ke-",dataGanjil)
print("jadi nilai median :",median)

