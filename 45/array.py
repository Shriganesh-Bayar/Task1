class Negative_Number(Exception):
    '''Raised when the entered number is negative '''
    pass

def Enter_Input() -> int:
    while True:
        try:
            number = int(input("Enter the number of elements: "))
            if number <= 0 :
                raise Negative_Number("Number should be Postive integer!")
            return number
        except Negative_Number:
            print(Negative_Number)
        except ValueError:
            print("Number should be Postive integer!")

if __name__ == "__main__":
    n = Enter_Input()
    arr = []
    for i in range(n):
        x = input(f"Enter the {i}th element: ")
        arr.append(x)
    # arr = list(map(int, input().split()))
    # this would work but the input can have less than n or more than n element
    print(arr)