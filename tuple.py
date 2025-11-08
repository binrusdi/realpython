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
print(x)

contoh1 = (1,2,3)
print(contoh1)

del contoh1

try:
    print(contoh1)
except NameError:
    print('Nama variable tidak ada')