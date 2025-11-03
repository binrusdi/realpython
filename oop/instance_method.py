"""
Salah satu aturan pada instan method adalah parameter pertama harus di beri nama 'self'.
Parameter self wajib saat deklarasi, 'dan tidak boleh di isi argumen saat pemanggilan'
Parameter 'setelah self' yaitu untuk menampung data dan dapat diolah nantinya.
"""

all_person = []

class Person:
    def __init__(self):
        self.name = ''
        self.age = 0

    def info(self):
        print(f'nama : {self.name} \n umur : {self.age}')

    def set_attr(self, name, age):
        self.name = name
        self.age = age

rusdiana = Person()
rusdiana.set_attr('Rusdiana', 28)
all_person.append(rusdiana)

angga = Person()
angga.set_attr('Angga', 25)
all_person.append(angga)

for p in all_person:
    p.info()
    print()

"""
Pengaksesan method dengan class diperbolehkan dengan syarat, paramether pertama adalah instance object
"""

class Mahasiswa:
    def __init__(self):
        self.name = ''
        self. age = 0
        self.nim = 0

    def get_acces(self, name, nim):
        self.name = name
        self.nim = nim

    def display_acces(self, name, age, nim):
        print(f'name: {name}\nage: {age}\nnim : {nim}')

mhs = Mahasiswa()
print(Mahasiswa.display_acces(mhs,'Rusdiana', 28, 234567))











