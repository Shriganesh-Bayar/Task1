class Negative_Amount(Exception):
    '''Raised when the entered number is negative '''
    pass

def Enter_Input(message: str) -> float:
    while True:
        try:
            Principle = float(input(message))
            if Principle < 0 :
                raise Negative_Amount("Amount cannot be negative!")
            return Principle
        except Negative_Amount:
            print(Negative_Amount)
        except ValueError:
            print("Invalid input!")

def Calculate_Discount(TotalAmount : float, Discount : float):
    return TotalAmount * Discount / 100

if __name__ == "__main__":
    TotalAmount = Enter_Input("Enter the Total amount: ")
    Discount = Enter_Input("Enter the discount percentage(%): ")
    print(f"Discount for {TotalAmount} is:", Calculate_Discount(TotalAmount, Discount))