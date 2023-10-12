# collections : pustaka
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# COUNTER
# untuk menghitung ada berapa karakter dan jumlahnya. Seperti 'd' ada 6, 'z' ada 4, dan k ada '3', dan 'k' ada 3.
a = "dddzzzdddkkk"
mycounter = Counter(a)
print(mycounter)

# untuk mengetahui kata kunci dalam string.
print(mycounter.keys())

# untuk mengetahui berapa karakter per satu kata kunci dalam string.
print(mycounter.values())

# untuk mengetahui kata kunci paling umum dalam string dan jumlah karakernya. Seperti dalam string 'a', karakter paling umum pertama adalah 'd' dengan jumlah 6 karakter.
print(mycounter.most_common(1))

# untuk mengetahui kata kunci dan print sesuai jumlah karakternya dalam string.
print(list(mycounter.elements()))

# NAMEDTUPLE
# untuk menyimpan tuple.
Point = namedtuple('Point', 'x, y')
pt = Point(55, -66)
print(pt)

# ORDEREDDICT
# untuk menyimpan dictionary secara berurutan.
ordered_dict = OrderedDict()
ordered_dict['Satu'] = 1
ordered_dict['Dua'] = 2
ordered_dict['Tiga'] = 3
ordered_dict['Empat'] = 4
ordered_dict['Lima'] = 5
ordered_dict['Enam'] = 6
print(ordered_dict)

# DEFAULTDICT
# untuk menyimpan dictionary yang isinya bisa diatur. Seperti untuk menghitung berapa urutan karakter 'v'.
d = defaultdict(int)
d['k'] = 1
d['e'] = 2
d['v'] = 3
print(d['v'])

# DEQUE
# untuk mengimplementasikan antrian.
d = deque()
d.append(1)
d.append(2)

# appendleft : untuk menambahkan karakter ke paling kiri. Seperti menambahkan integer 0 ke paling kiri di dalam deque yang berisi 1, 2.
d.appendleft(0)
print(d)

# pop : untuk menghapus karakter paling kanan.
d.pop()
print(d)

# extend : untuk menambahkan karakter dengan jumlah banyak.
d.extend([4, 5, 6])
print(d)

# rotate : untuk membalikkan urutan karakter.
d.rotate()
print(d)