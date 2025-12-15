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
    def invoice(items, membership):
        grand_total = 0
        total_quantity = 0

        print("\nInvoice")
        print("-" * 65)
        print(f"{'Code':10} {'Description':15} {'Qty':8} {'Price':10} {'Total':10}")
        print("-" * 65)

        for item in items:
            item_total = item.total_cost()
            grand_total += item_total
            total_quantity += item.quantity

            print(
                f"{item.code:10} "
                f"{item.description:15} "
                f"{item.quantity:8} "
                f"{item.price:10.2f} "
                f"{item_total:10.2f}"
            )

        print("-" * 65)
        print(f"{'Sub Total':48} {grand_total:10.2f}")

        discount = 0

        if grand_total > 10000:
            amount_discount = grand_total * 0.10
            discount += amount_discount
            print(f"{'10% Amount Discount':48} -{amount_discount:9.2f}")

        discounted_total = grand_total - discount
        if total_quantity > 20:
            quantity_discount = discounted_total * 0.05
            discount += quantity_discount
            print(f"{'5% Quantity Discount':48} -{quantity_discount:9.2f}")

        discounted_total = grand_total - discount
        if membership:
            member_discount = discounted_total * 0.02
            discount += member_discount
            print(f"{'2% Membership Discount':48} -{member_discount:9.2f}")

        final_total = grand_total - discount

        if final_total < 5000:
            tax_rate = 0.05
        elif final_total <= 20000:
            tax_rate = 0.10
        else:
            tax_rate = 0.15

        tax = final_total * tax_rate

        print(f"{'Tax Applied':48} {tax:10.2f}")

        final_payable = final_total + tax

        print("-" * 65)
        print(f"{'Final Payable Amount':48} {final_payable:10.2f}")


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

    membership = input("Membership (y/n): ").lower() == 'y'
    Item.invoice(items, membership)    