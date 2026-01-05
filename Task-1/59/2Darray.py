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
def Enter_array(size: int, message: str) -> list[int]:
    while True:
        try:
            arr = list(map(int, input(message).split()))
            if len(arr) != size:
                print(f"Please enter exactly {size} elements!")
                continue
            return arr
        except ValueError:
            print("All elements must be integers!")

def printMatrix(matrix):
    for row in matrix:
        for i in row:
            print(i, end = " ")
        print()

if __name__ == "__main__":
    n = Enter_Input("Enter the number of rows: ")
    m = Enter_Input("Enter the number of colums: ")
    matrix = []
    for i in range(n):
        matrix.append(Enter_array(m, f"Enter row {i + 1}: "))
    print("Original Matrix: ")
    printMatrix(matrix)
    
    transpose = [[matrix[i][j] for i in range(n)] for j in range(m)]
    print("Transpose Matrix:")
    printMatrix(transpose)
    