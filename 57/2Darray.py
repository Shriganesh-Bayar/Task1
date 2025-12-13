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
def Enter_array(size: int, message: str) -> list[float]:
    while True:
        try:
            arr = list(map(float, input(message).split()))
            if len(arr) != size:
                print(f"Please enter exactly {size} elements!")
                continue
            return arr
        except ValueError:
            print("All elements must be integers!")

if __name__ == "__main__":
    n = Enter_Input("Enter the number of rows: ")
    m = Enter_Input("Enter the number of colums: ")
    arr = []
    for i in range(n):
        arr.append(Enter_array(m, f"Enter row {i + 1}: "))
    key = Enter_Input("Enter the key element to find: ")
    for i, row in enumerate(arr):
        if key in row:
            print(f"The {key} is found at index ({i}, {row.index(key)})")
            break
    else:
        print(f"The {key} is not found in the matrix")
    