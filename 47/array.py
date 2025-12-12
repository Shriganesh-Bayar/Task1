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
def Enter_array(size: int) -> list[float]:
    while True:
        try:
            arr = list(map(float, input("Enter array elements: ").split()))
            if len(arr) != size:
                print(f"Please enter exactly {size} elements!")
                continue
            return arr
        except ValueError:
            print("All elements must be integers!")

if __name__ == "__main__":
    n = Enter_Input()
    arr = Enter_array(n)
    minimum = min(arr)
    print("Minimum element of array is:", minimum)
    