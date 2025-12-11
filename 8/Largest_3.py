def Enter_List() -> float:
    '''Try catch block + infinite loop until correct input'''
    while True:
        try:
            arr = list(map(float, input("Enter a list of numbers: ").split()))
            return arr
        except ValueError:
            print("Invalid input!")

if __name__ == "__main__":
    arr = Enter_List()
    arr.sort()
    print("The largest 3 numbers are: ")
    for i in range (1, 4):
        print(arr[-i])