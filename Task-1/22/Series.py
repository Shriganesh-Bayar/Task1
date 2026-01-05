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
    if n == 1:
        print("First 1 element of the series is: ")
        print([1])
    elif n == 2:
        print("First 2 element of the series is: ")
        print([1, 4])
    else:
        ans = [1, 4, 7]
        for i in range(3, n):
            # ans[n] = ans[n - 1] + ans[n - 2] + ans[n - 3]
            ans.append(ans[-1] + ans[-2] + ans[-3])
        print(f"First {n} element of the series are:")
        print(ans)