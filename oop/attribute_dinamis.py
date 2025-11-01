# Atribut kelas dan instan dinamis
"""
Dalam python, anda dapat menambahkan atribut baru kedalam kelas atau instan secara dinamis. Fitur ini memungkinkan anda untuk menambah data dan prilaku baru sebagai respone terhadap perubahan persyaratan atau konteks program.
"""

'''Contoh kasus => 
Semisal anda mempunyai data. Selanjutnya anda ingin merepresentasikan data tersebut sebagai instan dari sebuah kelas.
'''

class Record:
    pass


rusdiana_record = Record()

# Menambahkan atribut secara dinamis
rusdiana_record.name = 'Rusdiana'
rusdiana_record.age = 25
rusdiana_record.occupation = 'Data Scientist'
rusdiana_record.skills = ['Python', 'Machine Learning', 'Data Analys']

print(rusdiana_record.__dict__)
# Output: {'name': 'Rusdiana', 'age': 25, 'occupation': 'Data Scientist', 'skills': ['Python', 'Machine Learning', 'Data Analys']}

'''Dalam contoh diatas, anda membuat kelas kosong Record. Kemudian anda membuat instan rusdiana_record dari kelas tersebut'''

# Menambhakna metode secara dinamis
def __init__(self, name, job):
    self.name = name
    self.job = job

Record.__init__ = __init__
print(Record.__dict__)

def greet(self):
    return f'Hello, my name is {self.name}, and I work as a {self.job}.'

Record.greet = greet
print(Record.__dict__)

dian_record = Record('Dian', 'Atlet')
print(dian_record.greet())  # Output: Hello, my name is Dian, and I work as a Atlet.


















