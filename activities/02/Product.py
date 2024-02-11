class Product:
    def __init__(self):
        self.product_id = 1
        self.product_name = 'Kagayaku'
        self.product_category = 'Soap'
        self.product_stock_quantity = 5
        self.total_product_stock_quantity = 100

    def display_inventory_stock(self):
        print(f'Current Product Stock: {self.product_stock_quantity}\n')

    def add_product(self, product_id, product_stock_quantity):
        self.product_id = product_id
        self.product_stock_quantity = product_stock_quantity
        print(f'Total Stock: {self.total_product_stock_quantity + self.product_stock_quantity}\n')

    def display_product(self):
        print(f'Product ID: {self.product_id}')
        print(f'Product Name: {self.product_name}')
        print(f'Product Category: {self.product_category}')
        print(f'Total Stock: {self.total_product_stock_quantity + self.product_stock_quantity}\n')
