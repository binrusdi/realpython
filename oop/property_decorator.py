# Properti atau Dekorator
"""
Fitur ini memungkinkan anda untuk mengubah sebuah atribut pada kelas tanpa menyentuhnya langsung. Fitur ini bertujuan untuk merubah atribut dengan menggunakan validasi, yang mana didalam nya ada fitur get, set untuk merubah atribut.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def radius(self):
        return self._radius
    
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError('Positive expected')
        self._radius = value

    def calculate_area(self):
        return math.pi * self._radius**2
    
circle_1 = Circle(100)
print(circle_1) # <__main__.Circle object at 0x0000021E2EE7BFD0>

'''Lihat output diatas, karna kita belum menggunakan properti, itu hanya mengembalikan namespace class Circle '<__main__.Circle object at 0x0000021E2EE7BFD0>' '''
