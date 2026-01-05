def Enter_Input(message: str = "") -> int:
    '''Try catch block + infinite loop until correct input'''
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid input!")
        
if __name__ == "__main__":
    nuumber = Enter_Input("Enter a number: ")
    print(nuumber, "is a", "odd" if nuumber % 2 == 1 else "even")
