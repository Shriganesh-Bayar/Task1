def Enter_Input() -> int:
    while True:
        try:
            number = int(input("Enter the number: "))
            return number
        except ValueError:
            print("Number should be Postive integer!")

if __name__ == "__main__":
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    n = Enter_Input()
    negative = True if n < 0 else False
    n = abs(n)
    ans = []
    while n > 0:
        remainder = n % 10
        ans.append(words[remainder])
        n //= 10
    ans.reverse()
    # if number is negative, we need to indicate it is negative
    if negative:
        print("Negative", end = " ")
    for c in ans:
        print(c, end = " ")
    print()
    