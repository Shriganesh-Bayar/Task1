class Employee:
    name: str
    EmpID: str
    basic_salary: float
    special_allowance: float
    bonus_percentage: float
    gross_monthly_salary: float
    annual_gross_salary: float

    def __init__(self, name, EmpID, basic_salary, special_allowance, bonus_percentage):
        self.name = name
        self.EmpID = EmpID
        self.basic_salary = basic_salary
        self.special_allowance = special_allowance
        self.bonus_percentage = bonus_percentage

        # calculating the gross monthly and annual salry
        self.gross_monthly_salary = self.basic_salary + self.special_allowance
        self.annual_gross_salary = self.gross_monthly_salary * 12 * (100 + bonus_percentage) /100
    
    def Report(self):
        print("Name:", self.name)
        print("EmpID:", self.EmpID)
        print("Gross Monthly Salary:", self.gross_monthly_salary)
        print("Gross annual salary:", self.annual_gross_salary)
        
if __name__ == "__main__":
    n = int(input("Enter number of employee: "))
    employee = [None] * n
    for i in range(n):
        name = input("Enter the name of employee: ")
        EmpId = input("Enter the employee ID: ")
        basic_salary = float(input(f"Enter the basic salary of {name}: "))
        special_allowance = float(input(f"Enter the special allowance of {name}: "))
        bonus_percentage = float(input(f"Enter the bonus percentage(%): "))
        employee[i] = Employee(name, EmpId, basic_salary, special_allowance, bonus_percentage)
    for i in range(n):
        employee[i].Report()
    pass