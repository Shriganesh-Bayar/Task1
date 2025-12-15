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

    @staticmethod
    def invoice(items):
        grand_total = 0

        print("\nInvoice")
        print("----------------------------------------------------")
        print(f"{'Code':10} {'Description':15} {'Qty':8} {'Price':10} {'Total':10}")
        print("----------------------------------------------------")

        for item in items:
            print(f"{item.code:10} {item.description:10} {item.quantity:8} ₹{item.price:8.2f} ₹{item.total_cost():10.2f}")
            grand_total += item.total_cost()

        print("----------------------------------------------------")
        print(f"Grand Total: ₹{grand_total:.2f}")

if __name__ == "__main__":
    items = []
    code_to_index = {}
    n = int(input("Enter the number of items: "))

    for i in range(n):
        print("Enter the details of item", i + 1, ": ")
        code = input("Item Code: ")
        description = input("Description: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price per item (₹): "))

        items.append(Item(code, description, quantity, price))
        code_to_index["code"] = i

    Item.invoice(items)    