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
    # series contain only odd number => ans[n] = 2 * n + 1
    ans = []
    for i in range(n):
        ans.append(2 * i + 1)
    print(f"First {n} element of the series are:")
    print(ans)