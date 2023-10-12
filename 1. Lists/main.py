# list : untuk menyimpan elemen yang variabelnya bisa berbeda-beda, dan elemennya dapat diubah-ubah.
mylist = ["zero", "one", "two"]
mylist2 = ["nol", "satu", "dua"]
mylist3 = [2, 0, -17, 38, -5, 9]
print(mylist)

# print semua element di list.
for a in mylist:
    print(a)

# jika ada element "one" di list, output akan print hasil "ada", jika tidak output akan print hasil "ga ada".
if "one" in mylist:
    print("ada")
else:
    print("ga ada")

# len : untuk menghitung ada berapa element di list.
print(len(mylist))

# append : menambah element pada list di posisi terakhir.
mylist.append("three")
print(mylist)

# insert : menambah element pada list di posisi yang lebih spesifik, seperti urutan ke 2.
mylist.insert(2, "nyempil")
print(mylist)

# pop : untuk menghapus element terakhir di list.
item = mylist.pop()
print(mylist)

# remove : untuk menghapus element yang spesifik di list, seperti "zero".
item = mylist.remove("zero")
print(mylist)

# clear : untuk menghapus semua element di list.
item = mylist2.clear()
print(mylist)

# reverse : untuk membalikkan urutan element di list.
item = mylist.reverse()
print(mylist)

# sort : untuk mengurutkan element angka di list.
item = mylist3.sort()
print(mylist2)

# untuk memperbanyak elemen dengan mengulangnya atau mengkalinya, seperti angka 6 yang diulang 3 kali.
mylist4 = [6] * 3
print(mylist4)

# untuk mengambil sebagian elemen angka yang berurutan di list, seperti elemen ke 2 yaitu angka 3 sampai elemen sebelum ke 7 yaitu angka 7.
mylist5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist5[2:7]
print(a)

# untuk mengkuadratkatkan elemen angka di list, seperti 1*1, 2*2 sampai 9*9.
mylist6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i*i for i in mylist6]
print(mylist6)
print(b)
