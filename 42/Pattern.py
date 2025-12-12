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
    ans = []
    # here a[i] = (a + (i - 1) * d) * (-1) ^ (i - 1)
    # when we use 0 based indexing then it will
    # a[i] = (a + i * d) * (-1) ^ i 
    a = 1
    d = 4
    for i in range(n):
        ans.append((a + i * d) * ((-1) ** i))
    print(ans)
