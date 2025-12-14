class Employee:
    name: str
    EmpID: str
    basic_salary: float
    special_allowance: float
    bonus_percentage: float
    gross_monthly_salary: float
    annual_gross_salary: float
    taxable_annual_income: float
    total_tax: float
    net_salary: float

    def __init__(self, name, EmpID, basic_salary, special_allowance, bonus_percentage):
        self.name = name
        self.EmpID = EmpID
        self.basic_salary = basic_salary
        self.special_allowance = special_allowance
        self.bonus_percentage = bonus_percentage

        # calculating the gross monthly and annual salry
        self.gross_monthly_salary = self.basic_salary + self.special_allowance
        self.annual_gross_salary = self.gross_monthly_salary * 12 * (100 + bonus_percentage) / 100
    
    def Report(self):
        print("\nReport:")
        print("Name:", self.name)
        print("EmpID:", self.EmpID)
        print(f"Gross Monthly Salary: ₹{self.gross_monthly_salary}")
        print(f"Annual gross salary: ₹{self.annual_gross_salary}")

    def Taxable_Income(self):
        print("\nTaxable Income Report:")
        self.taxable_annual_income = self.annual_gross_salary - 50000
        print(f"Annual gross salary: ₹{self.annual_gross_salary}")
        print("Taxable Income: ₹50000")
        print(f"The Taxable annual income: ₹{self.taxable_annual_income}")

    def calculate_tax(self):
        tax = 0
        if self.taxable_annual_income <= 700000:
            print("Taxable income is not more than 7lakh, hence no tax")
            pass

        # ₹0-₹300000
        if self.taxable_annual_income >= 300000:
            slab_tax = min(self.taxable_annual_income - 300000, 300000) * 0.05
            tax += slab_tax
            print("₹300000-₹600000 ->", slab_tax)

        # ₹0-₹300000
        if self.taxable_annual_income >= 600000:
            slab_tax = min(self.taxable_annual_income - 300000, 300000) * 0.1
            tax += slab_tax
            print("₹600000-₹900000 ->", slab_tax)

        # ₹0-₹300000
        if self.taxable_annual_income >= 900000:
            slab_tax = min(self.taxable_annual_income - 300000, 300000) * 0.15
            tax += slab_tax
            print("₹900000-₹1200000 ->", slab_tax)

        # ₹0-₹300000
        if self.taxable_annual_income >= 1200000:
            slab_tax = min(self.taxable_annual_income - 300000, 300000) * 0.2
            tax += slab_tax
            print("₹1200000-₹1500000 ->", slab_tax)

        # ₹0-₹300000
        if self.taxable_annual_income >= 1500000:
            slab_tax = min(self.taxable_annual_income - 300000, 300000) * 0.3
            tax += slab_tax
            print("Above ₹1500000 ->", slab_tax)

        education_health = tax * 0.04
        self.total_tax = tax + education_health
        print("Tax:", tax)
        print("Tax on education and health: ", education_health)
        print("Total tax:", self.total_tax)   

    def net_salary(self):
        self.net_salary = self.annual_gross_salary - self.total_tax
        print(f"Gross annual salary: ₹{self.annual_gross_salary}")
        print(f"Total tax: ₹{self.total_tax}")
        print(f"Net annual salary: ₹{self.net_salary}")
        
if __name__ == "__main__":
    n = int(input("Enter number of employee: "))
    id = {}
    employee = [None] * n
    for i in range(n):
        name = input("Enter the name of employee: ")
        EmpId = input("Enter the employee ID: ")
        basic_salary = float(input(f"Enter the basic salary of {name}: "))
        special_allowance = float(input(f"Enter the special allowance of {name}: "))
        bonus_percentage = float(input(f"Enter the bonus percentage(%): "))
        employee[i] = Employee(name, EmpId, basic_salary, special_allowance, bonus_percentage)
        id[EmpId] = i

    for i in range(n):
        employee[i].Report()
        employee[i].Taxable_Income()
        employee[i].calculate_tax()