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
        print(row)

if __name__ == "__main__":
    # for matrix multiplication number of column in 1st matrix = number rows in 2nd matrix
    n = Enter_Input("Enter the number of rows in 1st matrix: ")
    m = Enter_Input("Enter the number of colums in 2nd matrix: ")
    p = Enter_Input("Enter number of column in 2nd matrix: ")
    a = []
    for i in range(n):
        a.append(Enter_array(m, f"Enter row {i + 1}: "))
    b = []
    for i in range(m):
        b.append(Enter_array(p, f"Enter row {i + 1}: "))
    print("Frist matrix:")
    printMatrix(a)

    print("Second Matrix: ")
    printMatrix(b)

    result = [[0] * p for i in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += a[i][k] * b[k][j]
    
    print("Resultant Matrix: ")
    printMatrix(result)

    