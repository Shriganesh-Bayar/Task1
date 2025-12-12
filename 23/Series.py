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
    # series doens't contain the element 16 * n + 1, where n >= 1
    ans = [1]
    current_number = 1
    i = 1
    while i < n:
        current_number += 4
        if (current_number - 1) % 16 == 0:
            continue
        ans.append(current_number)
        i += 1

    print(f"First {n} element of the series are:")
    print(ans)