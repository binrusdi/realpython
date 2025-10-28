# Mendefinisikan class

import math # memanggil module bawaan python yaitu 'math'


class Circle:
    def __init__(self, radius):
        self.radius = radius # Attribut instance

    def calculate_area(self): # Method
        return math.pi * self.radius ** 2
    

"""
Dalam cuplikan kode di atas, saya mendefinisikan kelas Circle dengan menggunakan kata kunci 'class'.
didalam badan kelas, saya menulis dua metode:
Pertama 'def __init__()' yang mempunyai arti khusu dalam kelas python.
Metode ini dikenal sebagai 'inisialisasi' objek karena mendefinisikan dan menetapkan nilai awal untuk atribut objek. (..lebih lanjut di tutor Atribut Instan ya ^_^ ).

Kedua 'def calculate_area()' yang mana akan menghitung luas lingkaran tertentu berdasarkan jari-jarinya.
"""

# Membuat objek dari kelas Circle

object_circle_1 = Circle(42)
print(object_circle_1) # Output: <__main__.Circle object at 0x00000268CCB56A50>

"""
Untuk membuat objek dari kelas python seperti 'Circle'. kamu harus memanggil konstruktor kelas, yaitu 'Circle'
dengan sepasang tanda kurung '()' dan serangkaian argumen yang sesuai.
Seperti apa argumen nya? dalam python, konstruktor kelas menerima argumen yang sesuai atau sama dengan metodenya -> '__init__()'. Dalam contoh, kelas Circle mengharapkan argumen 'radius'.
"""

# Merubah atribut dan mengakses atribut dan metode kelas

object_circle_1.radius = 20 # Merubah atribut

print(object_circle_1.radius) # Output: 20

print(object_circle_1.calculate_area()) # Akses metode kelas
