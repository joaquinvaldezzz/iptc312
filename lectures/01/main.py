from Product import Product


# Extend the Product with the SkinCare class
class SkinCare(Product):
    def __init__(self, product_id, product_name, product_category, product_quantity):
        super().__init__(product_id, product_name, product_category)
        self.product_quantity = product_quantity

    def display_items(self):
        super().display_items()
        print(f'Product Quantity: {self.product_quantity}')


product = SkinCare(product_id=1, product_name='Kagayaku', product_category='Soap',
                   product_quantity=12)

product.display_items()
