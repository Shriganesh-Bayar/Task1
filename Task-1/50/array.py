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

if __name__ == "__main__":
    n = Enter_Input()
    arr = Enter_array(n)
    odd = 0
    even = 0
    for i in arr:
        odd += (i % 2 == 1)
        even += (i % 2 == 0)
    print("Number of odd number is:", odd)
    print("Number of even number is:", even)

    