import math

def Enter_Input() -> float:
    while True:
        try:
            number = float(input("Enter the number: "))
            return number
        except ValueError:
            print("Number should be Postive number!")

if __name__ == "__main__":
    n = Enter_Input()
    # modf(n) gives the fraction and 
    fraction, whole = math.modf(n)
    print("whole number: ", int(whole))
    print("Fraction part: ", round(fraction, 4))