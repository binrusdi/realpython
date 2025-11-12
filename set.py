# Set
'''
- Dapat diubah
- Tidak ada duplikat
- Element tidak boleh diubah
'''

a = {1, 2, 4, 6, 8}
b = {1, 2, 3, 4, 5}

# ==Operasi atau method pada set== #

# 1 add() -> menambahkan elemen ke dalam set. jika elem sudah ada tidak terjadi apa²
c = {'apple', 'jeruk'}
c.add('sirsak')
print(c)

# 2 clear -> menghapus isi set(all elemen)
d = {1, 3, 4}
print(d)
d.clear()
print(d)

# 3 copy() -> mengembalikan salinan set

# union() -> menggabungkan huruf dari kedua himpunan sambil menghilangkan duplikat
print(a.union(b))
# print(a|b) # ekuivalen
# Output: {1, 2, 3, 4, 5, 6, 8}

# intersection() -> mengambil nilai yang sama dari dua himpunan
print(a.intersection(b))
# print(a & b) # ekuivalen
# Output: {1, 2, 4}

# different() -> mengambil nilai yang ada di a tapi tidak ada di b
print(a.difference(b))
# print(a - b) # ekuivalen
# Output: {8, 6}

# symmetric_difference() -> mengambil nilai yang ada di a atau b, tapi tidak keduanya
print(a.symmetric_difference(b))
# print(a^b) # ekuivalen
# Output: {3, 5, 6, 8}

# Superset dan subset
induk = {2, 3, 4, 5, 6}
anak = {3, 5, 6}

print(induk.issuperset(anak))
print(anak.issubset(induk))