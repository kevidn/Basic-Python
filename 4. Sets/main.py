# sets : untuk menyimpan element unik, element tidak dapat di-duplikat.
myset = set("Haii")
print(myset)

# add : untuk menambah nilai, seperti menambah nilai 1, 2, 3.
myset2 = set()
myset2.add(1)
myset2.add(2)
myset2.add(3)
print(myset2)

# discard : untuk menghapus nilai, seperti menghapus nilai 2. 
myset2.discard(2)
print(myset2)

# clear : untuk menghapus satu set.
myset2.clear()
print(myset2)

# pop : untuk mencari nilai terkecil.
myset3 = set()
myset3.add(6)
myset3.add(5)
myset3.add(3)
print(myset3.pop())
print(myset3)

# untuk mengeluarkan semua value berurutan kebawah.
for x in myset3:
    print(x)

# union : untuk memasukkan set ke set lainnya dan mengurutkannya secara berurutan.
ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6, 8, 10}
prima = {2, 3, 5, 7, 11}
u = ganjil.union(genap)
print(u)

# intersection : untuk memilih element yang sama antar sets, seperti pada sets "ganjil" dan sets "prima" ada 3 element yang sama yaitu {3, 5, 7}. Sedangkan pada sets "genap" dan sets "prima" ada 1 element yang sama yaitu {2}.
i = ganjil.intersection(prima)
print(i)
z = genap.intersection(prima)
print(z)

# difference : untuk mencari perbedaan antara dua sets, seperti pada set "myset4" ada angka {5, 6, 7, 8, 9, 10}, sedangkan di set "myset5" tidak ada.
myset4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
myset5 = {1, 2, 3, 4, 11, 12, 13, 14, 15}
diff = myset4.difference(myset5)
print(diff)

# symmetric_difference : untuk menggabungkan masing-masing perbedaan antara kedua sets. Seperti di set "myset4" memiliki elemen {5, 6, 7, 8, 9, 10} yang tidak dimiliki di set "myset5", sedangkan set "myset5" memiliki {11, 12, 13, 14, 15} yang tidak dimiliki set "myset4".
diff2 = myset4.symmetric_difference(myset5)
print(diff2)

# update : untuk memperbaharui set dengan set lainnya.
myset4.update(myset5)
print(myset4)

# intersection_update : untuk mencari element yang ada pada kedua sets. Seperti {1, 2, 3, 4} ada pada set "myset6" dan "myset7".
myset6 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
myset7 = {1, 2, 3, 4, 11, 12, 13, 14, 15}
myset6.intersection_update(myset7)
print(myset6)

# issubset : untuk mengetahui apakah element di set ada pada set lainnya secara lengkap, jika ada akan ter-print "True", jika tidak akan ter-print "False". Seperti di set "myset8" ada elemen {4, 5, 6} yang elemennya ada pada set "myset9" juga.
myset8 = {4, 5, 6}
myset9 = {1, 2, 3, 4, 5, 6, 7}
print(myset8.issubset(myset9))

# issuperset : output-nya kebalikan dari issubset 
myset10 = {4, 5, 6}
myset11 = {1, 2, 3, 4, 5, 6, 7}
print(myset10.issuperset(myset11))

# isdisjoint : untuk mengetahui apakah element di set tidak ada pada set lainnya, jika tidak ada akan ter-print "True", jika ada akan ter-print "False". Seperti di set "myset11" element-nya tidak ada pada set "myset12".
myset11 = {4, 5, 6}
myset12 = {10, 11, 12}
print(myset11.isdisjoint(myset12))

# copy : untuk menduplikat set.
myset13 = {1, 2, 3}
myset14 = myset13.copy()
print(myset14)

# frozenset : element tidak akan bisa diubah.
myset15 = frozenset([1, 2, 3])
print(myset15)