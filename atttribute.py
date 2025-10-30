# Melambpirkan Data ke kelas dan Instans
"""
- Atribut kelas : variable yang didefinisikan langsung di badan kelas. Data nya bersifat umum untuk kelas dan semua instannya.
"""

'''
==Example==
Katakanlah kita ingin membuat kelas yang menyimpan jumlah instan yang telah dibuat. Dalam hal ini kita dapat menggunakan atribut kelas.
'''

print("==Example Atribut Kelas== \n")

class ObjectCounter:
    num_instances = 0 # Atribut kelas
    def __init__(self):
        # ObjectCounter.num_instances += 1
        type(self).num_instances += 1  # Alternatif cara mengakses atribut kelas

ObjectCounter()
# Membuat instan 1
ObjectCounter()
# Membuat instan 2
print(ObjectCounter.num_instances)  # Output: 2

obj = ObjectCounter()
print(obj.num_instances)  # Output: 3

'''
Jika kamu ingin memodifikasi atribut kelas, kamu dapat melakukannya melalui kelas itu sendiri atau melalui instan, tetapi perubahan melalui instan akan membuat atribut instan baru yang menimpa atribut kelas untuk instan tersebut.
'''

class PenghitungObjek:
    jumlah_instans = 0 # Atribut kelas
    def __init__(self):
        self.jumlah_instans += 1  # Ini akan membuat atribut instan baru

print(PenghitungObjek()) # Output: <__main__.PenghitungObjek object at 0x000001DC8B31BFA0>
print(PenghitungObjek()) # Output: <__main__.PenghitungObjek object at 0x000001DC8B31BFA0>
print(PenghitungObjek.jumlah_instans) # Output: 0 (atribut kelas tetap tidak berubah)

obj1 = PenghitungObjek()
print(obj1.jumlah_instans)  # Output: 1 (atribut instan)

obj2 = PenghitungObjek()
print(obj2.jumlah_instans)  # Output: 1 (atribut instan)
'''
Lihat pada objek yang dibuat, atribut kelas 'jumlah_instans' tetap 0, sedangkan atribut instan 'jumlah_instans' pada obj1 adalah 1 dan obj2 adalah 1 juga.
'''

print("==Example Atribut Instans==")

"""
- Atribut instan : variable yang didefinisikan di dalam metode instan menggunakan 'self' argumen dan notasi '.' (.self.attribut = value). Data hanya tersedia untuk instan tersebut dan menentukan statusnya. 
"""


class DataInstansMobil:
    def __init__(self, make, model, year, color):
        self.make = make
        self. model = model
        self.year = year
        self.color = color
        self.started = False # Atribut instan kongkret
        self.speed = 0
        self.max_speed = 180

'''
Dikelas ini, anda mendefinisikan atribut instan didalam metode __init__(). Atribut .make .model .year .color mengambil nilai dari argumen, yang diteruskan ke konstruktor kelas. sedangkan untuk atribut .started .speed .max_speed diinisialisasi dengan nilai default yang bukan berasal dari masukan pengguna.
'''

data_car1 = DataInstansMobil("Toyota", "Camry", 2020, "Red")
print("Mobil 1: \n")
print(data_car1.make) # Output: Toyota
print(data_car1.model) # Output: Camry
print(data_car1.year) # Output: 2020
print(data_car1.color) # Output: Red
print(data_car1.started) # Output: False
print(data_car1.speed) # Output: 0
print(data_car1.max_speed) # Output: 180

'''
Tidak seperti atribut kelas, atribut instan tidak dapat diakses melalui kelas itu sendiri.
'''

print(DataInstansMobil.make) # Akan menghasilkan AttributeError: type object 'DataInstansMobil' has no attribute 'make'




















