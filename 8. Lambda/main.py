# lambda : untuk membuat function tanpa harus menamainya.
from functools import reduce

# untuk menambahkan angka ke dalam argumen. Seperti angka '5' yang menjadi argumen ditambah ke variable 'a' yang function-nya "x + 12".
a = lambda x: x + 12
print(a(5))

# untuk menambahkan angka ke dalam argumen menggunakan kata kunci 'def'.
def b(x):
    return x + 12
print(b(5))

# untuk mengalikan angka dalam argumen. Seperti angka '2' dan '8' yang masuk ke dalam variable 'b' yang function-nya "x*y". Sehingga angka '2' menjadi 'x' dan angka '8' menjadi 'y'.
b = lambda x,y: x*y
print(b(2,8))

c = [(1, 20), (10, 15), (-1, 82), (-23, 6), (54, 3)]

# untuk mengurutkan list c berdasarkan nilai ke-2 (indeks ke-1).
d = sorted(c, key=lambda x: x[1])

# untuk mengurutkan list c berdasarkan nilai ke-1 (indeks ke-0).
e = sorted(c, key=lambda x: x[0])

print(c)
print(d)
print(e)

f = [5, 6, 7, 8, 9, 10]

# untuk mengalikan masing-masing angka di iterable 'f' dengan 2
g = map(lambda x: x*2, f)
print(list(g))

# untuk mengkuadratkan angka di iterable 'f'.
h = map(lambda x: x*x, f)
print(list(h))

# untuk mengetahui angka yang bisa dibagi 2 di iterable 'f'. 
i = filter(lambda x: x%2==0, f)
print(list(i))

# REDUCE
# untuk mengurangi (reduce) elemen dalam iterable menjadi satu nilai tunggal.

# untuk mengalikan masing-masing angka dalam iterable menjadi satu angka.
j = reduce(lambda x,y: x*y, f)
print(j)