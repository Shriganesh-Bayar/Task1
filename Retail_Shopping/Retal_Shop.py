class Item:
    code: str
    description: str
    quantity: int
    price: float

    def __init__(self, code, description, quantity, price):
        self.code = code
        self.description = description
        self.quantity = quantity
        self.price = price

    def total_cost(self):
        return self.quantity * self.price

    def Report(self):
        print("\nItem Details")
        print("------------")
        print("Item Code:", self.code)
        print("Description:", self.description)
        print("Quantity:", self.quantity)
        print("Price per item: ₹", self.price)
        print("Total Cost: ₹", self.total_cost())

if __name__ == "__main__":
    code = input("Enter item code: ")
    description = input("Enter item description: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item (₹): "))

    item = Item(code, description, quantity, price)
    item.display()
