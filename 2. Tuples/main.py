# tuple : untuk menyimpan element yang variabelnya bisa berbeda-beda, namun elemennya tidak dapat berubah.
mytuple = tuple(["Kevin", 17, "Bogor"])
print(mytuple)

# untuk print element yang posisinya spesifik, seperti element ke 2 yaitu "Bogor".
item = mytuple[2]
print(item)

# untuk print semua element berurutan ke bawah.
for a in mytuple:
    print(a)

# jika element "Bogor" ada pada mytuple, akan ter-print "ada", jika element tersebut tidak ada, akan ter-print "ga ada".
if "Bogor" in mytuple:
    print("ada")
else:
    print("ga ada")

# count = untuk menghitung ada berapa element yang sama, seperti element a yang jumlahnya ada 4.
mytuple2 = ('a', 'a', 'b', 'a', 'c', 'b')
print(mytuple2.count('a'))

# untuk mengambil sebagian elemen angka yang berurutan di list, seperti elemen ke-4 yaitu angka 5 sampai elemen sebelum ke-9 yaitu angka 9.
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
c = b[4:9]
print(c)

# i1 : untuk melihat element paling pertama.
# *i2 : untuk melihat element diantara pertama dan terakhir.
# i3 : untuk melihat element paling terakhir.
mytuple3 = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = mytuple3
print(i1)
print(i2)
print(i3)

# ADDITIONAL !!!
# untuk melihat size dari tuple atau function lainnya.
import sys
print(sys.getsizeof(mytuple), "bytes")