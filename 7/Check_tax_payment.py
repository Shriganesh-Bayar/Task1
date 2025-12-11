class Negative_Salary(Exception):
    '''Raise a exception when salary is entered negative'''
    pass

def Enter_Input(message: str) -> float:
    '''Try catch block + infinite loop until correct input'''
    while True:
        try:
            Principle = float(input(message))
            if Principle < 0 :
                raise Negative_Salary("Amount cannot be negative!")
            return Principle
        except Negative_Salary:
            print(Negative_Salary)
        except ValueError:
            print("Invalid input!")

if __name__ == "__main__":
    name = input("Enter the name: ")
    salary = Enter_Input("Enter the salary: ")
    print(name, "must pay tax" if salary > 300000 else "no need to pay tax")
    