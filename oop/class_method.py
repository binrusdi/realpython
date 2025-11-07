# Class method adalah fungsi yang dimiliki suatu kelas dengan pengaksesan lewat kelas
'''
Ciri deklarasi method class
- Parameter pertama adalah 'cls' yang merupakan alias dari class yang mendeklarasikan method tersebut.
- Class method di deklarasikan dengan menulis decorator @classmethod
'''

class ClanHouse:
    def __init__(self, name='', house=''):
        self.name = name
        self.house = house

    @classmethod
    def create(cls):
        obj = cls() # ekuivalen dengan cls() -> ClanHouse()
        return obj

    def info(self):
        print(f'{self.name} dari {self.house}')

p1 = ClanHouse()
p1.name = 'Rusdiana'
p1.house = 'House of Cimahi'
p1.info()

p2 = ClanHouse('Adam', 'House of Cijerah')
p2.info()

p3 = ClanHouse.create() # karna ini mengembalikan objek, jadi tidak diberikan parameter/tidak dioverload
p3.name = 'Indra'
p3.house = 'House of Rancaekek'
p3.info()