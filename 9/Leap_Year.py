class Negative_Year(Exception):
    '''Raised when the entered number is negative'''
    pass

def Enter_Year(message: str) -> int:
    '''Try catch block + infinite loop until correct input'''
    while True:
        try:
            year = int(input(message))
            if year < 0 :
                raise Negative_Year("Years cannot be negative")
            return year
        except Negative_Year:
            print(Negative_Year)
        except ValueError:
            print("Invalid input!")

if __name__ == "__main__":
    year = Enter_Year("Enter a year: ")
    print(year, "is", end = " ")
    if (year % 400 != 0 and year % 100 == 0) or (year % 4 != 0):
        print("not", end=" ")
    print("a leap year")