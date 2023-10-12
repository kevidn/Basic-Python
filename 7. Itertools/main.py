# itertools : modul yang berisi alat-alat yang berguna
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

# PRODUCT
# untuk menghasilkan produk kartesian (kemungkinan kombinasi) dari list.
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(list(prod))

# PERMUTATIONS
# untuk menghasilkan permutasi (kemungkinan urutan/susunan) dari berbagai element dalam list.
c = [6, 7, 8]
perm = permutations(c)
print(list(perm))

# COMBINATIONS
# untuk menghasilkan kemungkinan kombinasi dari list tanpa memperhatikan urutan.
d = [9, 10, 22, 30]
comb = combinations(d, 2)
print(list(comb))

# COMBINATIONS WITH REPLACEMENT
# untuk menghasilkan kemungkinan kombinasi dari list tanpa memperhatikan urutan dan boleh mengunakan element yang sama dalam satu kombinasi.
comb2 = combinations_with_replacement(d, 2)
print(list(comb2))

# ACCUMULATE
# untuk mengakumulasi nilai dalam list.
e = [4, 5, 6, 7]
acc = accumulate(e)
print(e)
print(list(acc))

# GROUPBY
# untuk mengelompokkan element-element yang sama dalam list.

# untuk mengelompokkan angka, angka yang kurang dari 3 akan ter-print "True", jika lebih dari 3 maka akan ter-print "False"
def smaller_than_3(x):
    return x < 3
nomor = [1, 2, 3, 4, 5]
group_obj = groupby(nomor, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

# untuk mengelompokkan list yang menyesuaikannya dengan salah satu element. Seperti 'umur' yang dijadikan patokan, sehingga setiap 'nama' menyesuaikan dengan 'umur'-nya.
orang = ({'nama': 'Kevin', 'umur': 17}, {'nama': 'Dzaky', 'umur': 17}, {'nama': 'Hendra', 'umur': 16}, {'nama': 'Tama', 'umur': 16}, {'nama': 'Vin', 'umur': 18})
group_obj2 = groupby(orang, key=lambda x: x['umur'])
for key, value in group_obj2:
    print(key, list(value))

# COUNT
# untuk mengitung angka, seperti menghitung angka 10, jika sudah angka == 15, maka akan berhenti.
for count in count(10):
    print(count)
    if count == 15:
        break

# CYCLE
# untuk mengulang semua element dalam list, seperti angka [1, 2, 3] yang akan diulang terus-menerus, jika semua '#' dihapus.
#f = [1, 2, 3] 
#for g in cycle(f):
#    print(g)

# REPEAT
# untuk mengulang element, seperti angka [1] yang akan diulang 6 kali.
for h in repeat(1, 6):
    print(h)

