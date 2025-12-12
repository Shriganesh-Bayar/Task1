def Enter_Input() -> int:
    while True:
        try:
            number = int(input("Enter the number: "))
            return number
        except ValueError:
            print("Number should be Postive integer!")

if __name__ == "__main__":
    n = Enter_Input()
    print("Given number:", n)
    negative = True if n < 0 else False
    n = abs(n)
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n //= 10
    m *= -1 if negative else 1
    print("Reversed:", m)
