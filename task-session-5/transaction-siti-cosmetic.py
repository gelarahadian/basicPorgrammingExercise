class CosmeticItem:
    def __init__(self, name, variant, cost_price, stock):
        self.name = name
        self.variant = variant
        self.cost_price = cost_price
        self.stock = stock
        self.selling_price = int(cost_price * 1.1)  # 10% markup for selling price

class CosmeticStore:
    def __init__(self):
        self.items = []
        self.transactions = 0
        self.profit = 0

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print("Available Cosmetic Items:")
        print("--------------------------")
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item.name} ({item.variant}) - Price: IDR {item.selling_price} - Stock: {item.stock}")

    def make_transaction(self, item_index, quantity):
        item = self.items[item_index - 1]
        if item.stock >= quantity:
            total_price = item.selling_price * quantity
            print(f"Transaction successful! You bought {quantity} {item.name} ({item.variant}) for IDR {total_price}")
            item.stock -= quantity
            self.transactions += 1
            self.profit += total_price - (item.cost_price * quantity)
        else:
            print("Insufficient stock!")

def main():
    store = CosmeticStore()

    # Add some initial items to the store
    store.add_item(CosmeticItem("Lipstick", "Red", 200000, 10))
    store.add_item(CosmeticItem("Lipstick", "Pink", 200000, 15))
    store.add_item(CosmeticItem("Eyeshadow Palette", "Neutral Shades", 350000, 8))
    store.add_item(CosmeticItem("Foundation", "Light", 250000, 12))

    while True:
        print("\nWelcome to Siti's Cosmetic Store!")
        print("----------------------------------")
        print("1. Display available items")
        print("2. Make a purchase")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            store.display_items()
        elif choice == "2":
            store.display_items()
            item_index = int(input("Enter the item number you want to purchase: "))
            quantity = int(input("Enter the quantity you want to purchase: "))
            store.make_transaction(item_index, quantity)
        elif choice == "3":
            print(f"\nTotal transactions: {store.transactions}")
            print(f"Total profit: IDR {store.profit}")
            print("Thank you for using Siti's Cosmetic Store!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
