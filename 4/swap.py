def get_two_numbers() -> tuple[float, float]:
   while True:
        try:
            a, b = map(float, input("Enter two numbers: ").split())
            return a, b
        except ValueError:
            print("Invalid input! Please enter exactly two integers.")

if __name__ == "__main__":
    a, b = get_two_numbers()
    print("Before swapping:", a, b)
    a, b = b, a
    print("Afer swapping:", a, b)