# dictionaries : untuk menyimpan kata kunci atau kata yang spesifik.
mydict = {"nama": "Kevin", "umur": 17, "kota": "Bogor",}
print(mydict)

# untuk mengambil nilai dari kata kunci di kamus "mydict".
value_nama = mydict["nama"]
value_umur = mydict["umur"]
value_kota = mydict["kota"]
print(value_nama)
print(value_umur)
print(value_kota)

# untuk menambah kata kunci.
mydict["nomor"] = 20
print(mydict)

# del : untuk menghapus kata kunci.
del mydict["umur"]
print(mydict)

# jika kata kunci "nama" ada pada kamus "mydict", akan ter-print kata kunci "nama" itu sendiri.
if "nama" in mydict:
    print(mydict["nama"])

# mencoba print kata kunci "nama", kecuali jika tidak ada kata kunci-nya maka akan ter-print "error".
try:
    print(mydict["nama"])
except:
    print("error")

# untuk memperbaharui kamus dan menggantikannya apabila kata kunci-nya sama.
mydict2 = {"nama":"Dzaky", "age":26, "kota":"Jakarta"}
mydict3 = dict(nama="Hendra", age=72, negara="Indonesia", kota="Bekasi")
mydict2.update(mydict3)
print(mydict2)