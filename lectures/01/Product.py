class Product:
    def __init__(self, product_id, product_name, product_category):
        self.product_id = product_id
        self.product_name = product_name
        self.product_category = product_category

    # def __public__(self):
    #     print('This is a public method.')
    #
    # def _private_(self):
    #     print('This is a private method.')

    def display_items(self):
        print(f'Product ID: {self.product_id}')
        print(f'Product Name: {self.product_name}')
        print(f'Product Category: {self.product_category}')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student(name='Joaquin', age=21)

print(student.name)  # Prints Joaquin
print(student.age)  # Prints 21
