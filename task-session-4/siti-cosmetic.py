cosmetic_items = [
    {"name": "Lipstick", "variant": "Red", "price": 225000},
    {"name": "Lipstick", "variant": "Pink", "price": 225000},
    {"name": "Eyeshadow Palette", "variant": "Neutral Shades", "price": 399000},
    {"name": "Foundation", "variant": "Light", "price": 269000},
]


for item in cosmetic_items:
    benefit = int(item["price"] * 0.1)
    item['benefit' ] = benefit
    item['sellingPrice'] = item["price"] + item["benefit"]

def print_list_cosmetic_items():
    print('----------------------------------------------------------------')
    print('List of Cosmetic')
    print('----------------------------------------------------------------')
    for item in cosmetic_items:
        print('Name: ',item['name'],"Variant: ", item['variant'],'Price: ', item['price'],'Benefit: ', item['benefit'],'Selling Price: ', item['sellingPrice'] )

def add_cosmetic_item():
    name = input("Enter the name of the cosmetic item: ")
    variant = input("Enter the variant of the cosmetic item: ")
    price = int(input("Enter the price of the cosmetic item: "))
    benefit = int(price * 0.1)
    sellingPrice = price + benefit
    cosmetic_items.append({"name": name, "variant": variant, "price": price, "benefit": benefit, "sellingPrice": sellingPrice})

print_list_cosmetic_items()

isChoosing = True

while isChoosing:
    print('----------------------------------------------------------------')
    print("1. Add a cosmetic item")
    print("2. Print the list of cosmetic items")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_cosmetic_item()
    elif choice == '2':
        print_list_cosmetic_items()
    elif choice == '3':
        isChoosing = False
    else:
        print("Invalid choice")
