# Tuple
'''
- Tidak dapat diubah, ditambah, dihapus 'itemnya'
- Boleh sama
- Punya index
'''
from logging import exception

contoh = ('avanza', 'xenia', 1, 3, 5, 'xenia', 'avanza')

# Akses tuple
print(type(contoh))
print(contoh[0:])
print(contoh[:len(contoh)])

# Operasi tuple yang di perbolehkan
x = ('yaris', 'alpard')
y = ('datsun',)

x += y
print(x) # ('yaris', 'alpard', 'datsun')

contoh1 = (1,2,3)
print(contoh1) # (1, 2, 3)

del contoh1

try:
    print(contoh1)
except NameError:
    print('Nama variable tidak ada') # Nama variable tidak ada, karena contoh1 sudah di hapus oleh key "del"
    
# Modifikasi tuple, menggunakan 'list'
daftar_belanja = ('Sayur', 'Buah', 'Furnitur')
y = list(daftar_belanja)
y.append('Termos')
daftar_belanja = tuple(y)
print(daftar_belanja, type(daftar_belanja))

# Method tuple
deret_angka = (1, 9, 8, 5, 6, 8, 9)
print(deret_angka.index(5)) # output: 3
'''
method index -> mencari index nilai tertentu lalu di kembalikan no index nya
'''

print(deret_angka.count(9)) # output 2
'''
method count -> mencari berapa kali nilai tertentu muncul di dalam sebuah tuple.
mengembalikan total kemunculan
'''