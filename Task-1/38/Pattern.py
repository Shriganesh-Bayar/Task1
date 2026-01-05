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
    a = 0
    b = 1
    for i in range (n):
        for j in range(i + 1):
            if i == 0 and j == 0:
                print(1, end = " ")
            else:
                print(a + b, end = " ")
                a, b = b, a + b
        print()