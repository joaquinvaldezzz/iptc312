from Product import Product

product = Product()

while True:
    print('Welcome to Fatima One Stop Shop:')
    print('1. Enter Product ID')
    print('2. Add an item')
    print('3. Display product')
    print('4. Exit\n')

    user_choice = int(input('Choose an option: '))

    if user_choice == 1:
        product.display_inventory_stock()
    elif user_choice == 2:
        product_id = input('Enter a product ID: ')
        product_stock_quantity = int(input('Enter stock quantity: '))

        product.add_product(product_id, product_stock_quantity)
    elif user_choice == 3:
        product.display_product()
    elif user_choice == 4:
        print('\nProgram terminated.')
        break
    else:
        print('Incorrect input.')
