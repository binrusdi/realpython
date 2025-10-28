'''
Dalam python tidak ada fitur protect, private seperti dalam java. Tapi para pytonista sepakat dengan konvensi penamaan pada atribut dan metode untuk dijadikan non-public. ( _radius, _calculate_area() )
'''

class SampleClass:
    def __init__(self, value):
        self.__value = value
    def __method(self):
        print(self.__value)
        
sample_instance = SampleClass('Hello')
# print(sample_instance.__value) # Output: AttributeError: 'SampleClass' object has no attribute '__value'

"""
Dari contoh diatas kita mendapatkan error ketika mengakses atribut SampleClass. Karena itu memiliki dunder (dua garis bawah sebelum nama atribut). duner ini sejatinya merubah nama atribut secara otomatis agar tidak da0at di akses langsung.
"""

print(vars(sample_instance)) # Output: {'_SampleClass__value': 'Hello'}

