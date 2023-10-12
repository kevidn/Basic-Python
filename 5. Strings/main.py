# strings : tipe data yang berisi huruf dan karakter lainnya.
mystring = 'Saya adalah Kevin'
print(mystring)

# triple " : memisah string ke dua baris.
mystring2 = """Saya 
Kevin"""
print(mystring2)

# untuk melihat urutan karakter di string. Seperti karakter ke -5 di string 'mystring5' adalah 'K'.
mystring3 = 'Saya Kevin'
char = mystring3[5]
print(char)

# untuk mengambil sebagian elemen dengan berurutan di list, seperti elemen ke-2 yaitu 'y' sampai elemen sebelum ke-13 yaitu 'K'.
mystring4 = 'Saya adalah Kevin'
substring = mystring4[2:13]
print(substring)

# untuk membuat kalimat dari gabungan string
mystring6 = 'Saya'
mystring7 = 'Kevin'
sentence = mystring6 + " " + mystring7
print(sentence)

# untuk membuat string ditulis kebawah.
mystring8 = 'Kevin'
for i in mystring8:
    print(i)

# jika karakter 'z' ada pada string 'mystring9' maka akan ter-print "yes", jika tidak 'no'.
mystring9 = 'Dzaky'
if 'z' in mystring9:
    print('yes')
else:
    print ('no')

# strip : untuk menghilangkan space yang kosong didalam string.
mystring10 = '    Saya Hidup  '
mystring10 = mystring10.strip()
print(mystring10)

# upper : untuk membuat kata atau kalimat di string menjadi kapital seluruhnya.
mystring11 = 'Kevin Dzaky'
print(mystring11.upper())

# lower : untuk membuat kata atau kalimat di string menjadi huruf kecil seluruhnya.
mystring12 = 'Kevin Dzaky'
print(mystring12.lower())

# startswith : untuk mengetahui apakah string diawali dengan kata tertentu. Jika iya akan ter-print "True", jika tidak "False". Seperti string 'mystring13' yang diawali dengan 'Halo'.
# endswith : untuk mengetahui apakah string diakhiri dengan kata tertentu. Jika iya akan ter-print "True", jika tidak "False". Seperti string 'mystring13' yang diakhiri dengan 'Dunia'.
mystring13 = 'Halo Dunia'
print(mystring13.startswith('Halo'))
print(mystring13.endswith('Dunia'))

# find : untuk mengetahui urutan keberapa karakter di string. Seperti 'D' adalah karakter ke-5.
# count : untuk mengetahui ada berapa karakter yang spesifik di string. Seperti 'a' ada 3.
# replace : untuk mengganti karakter di string. Seperti 'Dzaky' yang digantikan oleh 'Kevin'.
mystring14 = 'Saya Dzaky'
print(mystring14.find('D'))
print(mystring14.count('a'))
print(mystring14.replace('Dzaky', 'Kevin'))

# untuk menghapus koma di string.
mystring15 = 'saya,tinggal,di,bogor'
mylist = mystring15.split(',')
mystring16 = ''.join(mylist)
print(mystring16)

# untuk menduplikat string. Seperti di string 'mystring17' yang berisi 'abc' di-duplikat 6 kali.
mystring17 = ['a'] * 6
print(mystring17)

# menggabungkan string yang sudah di-duplikat. Seperti 'mystring17' yang isinya sudah di-duplikat dan digabung yang hasilnya menjadi 'aaaaaa'.
mystring18 = ''.join(mystring17)
print(mystring18)

# untuk menggabungkan variable ke string.
var = "Kevin"
mystring19 = "the variable is %s" % var
print(mystring19)

# untuk menggabungkan dua variable ke dalam string.
var2 = 6.66
var3 = 70.44
mystring20 = f"the variable is {var2} and {var3}"
print(mystring20)