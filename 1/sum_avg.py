def sum(a : float, b : float) -> float:
   return a + b

def avg(a : float, b : float) -> float:
   return sum(a, b) / 2

def get_two_numbers() -> tuple[float, float]:
   while True:
        try:
            a, b = map(float, input("Enter two numbers: ").split())
            print("You entered:", a, b)
            return a, b
        except ValueError:
            print("Invalid input! Please enter exactly two integers.")

if __name__ == "__main__":
   a, b = get_two_numbers()
   print(f"The sum of {a} and {b} is ", sum(a, b))
   print(f"The average of {a} and {b} is ", avg(a, b))