class Negative_Number(Exception):
    '''Raised when the entered number is negative '''
    pass

def Enter_Input(message: str) -> int:
    while True:
        try:
            number = int(input(message))
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
    n = Enter_Input("Enter the number of elements: ")
    arr = Enter_array(n)
    key = Enter_Input("Enter the key element to find: ")
    found = -1
    if key in arr:
        found = arr.index(key)
    if found == -1:
        print(f"The element {key} is not present in the array")
    else:
        print(f"The element {key} is found at position {found + 1}")
    