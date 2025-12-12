class Negative_Number(Exception):
    '''Raised when the entered number is negative '''
    pass

def Enter_Input() -> int:
    while True:
        try:
            number = int(input("Enter the number: "))
            if number <= 0 :
                raise Negative_Number("Number should be Postive integer!")
            return number
        except Negative_Number:
            print(Negative_Number)
        except ValueError:
            print("Number should be Postive integer!")

if __name__ == "__main__":
    n = Enter_Input()
    for i in range (1, n + 1):
        row = "".join(str(i) for j in range(i))
        print(row)