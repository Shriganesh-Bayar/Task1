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

# this takes exactly size number of input ofr array
def Enter_array(size: int) -> list[int]:
    while True:
        try:
            arr = list(map(int, input("Enter array elements: ").split()))
            if len(arr) != size:
                print(f"Please enter exactly {size} elements!")
                continue
            return arr
        except ValueError:
            print("All elements must be integers!")

def Enter_choice():
    while True:
        try:
            print("Enter the input\n1. Ascending Order\n2. Descending Order")
            choice = int(input("Enter your Choice: "))
            if choice != 1 and choice != 2:
                raise ValueError
            return choice
        except ValueError:
            print("The input should be either 1 or 2")

if __name__ == "__main__":
    n = Enter_Input()
    arr = Enter_array(n)
    choice = Enter_choice()
    if choice == 1:
        arr.sort()
        print("Array sorted in ascneding order:")
    else:
        arr.sort(reverse=True)
        print("Array sorted in descending order:")
    print(arr)
        