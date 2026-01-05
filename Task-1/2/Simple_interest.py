class Negative_Amount(Exception):
    '''Raised when the entered number is negative'''
    pass

def Enter_Input(message: str) -> float:
    '''Try catch block + infinite loop until correct input'''
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
    
def SimpleInterest(Principle : float, Time : float, RateOfInterest : float):
    return Principle * Time * RateOfInterest / 100

if __name__ == "__main__":
    """Simple Interest = PTR / 100"""
    Principle = Enter_Input("Enter the Principle amount: ")
    Time = Enter_Input("Enter the time(in years) to which interest to be calculated: ")
    RateOfInterest = int(input("Enter the rate of interest in percentage(%): "))

    print(f"The rate of interest for Principle amount of {Principle} over {Time} years with rate of interest {RateOfInterest}% is", SimpleInterest(Principle, Time, RateOfInterest))