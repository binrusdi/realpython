# Properti atau Dekorator
"""
Fitur ini memungkinkan anda untuk mengubah sebuah atribut pada kelas tanpa menyentuhnya langsung. Fitur ini bertujuan untuk merubah atribut dengan menggunakan validasi, yang mana didalam nya ada fitur get, set untuk merubah atribut.
"""


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property # get, hanya mengembalikan nilai
    def radius(self):
        return self._radius
    
    @radius.setter # set, untuk memvalidasi perubahan nilai atribut
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError('Positive expected')
        self._radius = value

    def calculate_area(self):
        return math.pi * self._radius**2
    
circle_1 = Circle(1)
print(circle_1.radius) # 1
print(circle_1.calculate_area()) # Output: 3.141592653589793
