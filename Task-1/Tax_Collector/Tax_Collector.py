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
        self.Taxable_Income()
        self.calculate_tax()
        self.net_salary()
    
    def Report(self):
        print("\nReport:")
        print("Name:", self.name)
        print("EmpID:", self.EmpID)
        print(f"Gross Monthly Salary: ₹{self.gross_monthly_salary}")
        print(f"Annual gross salary: ₹{self.annual_gross_salary}")
        print(f"Taxable Income: ₹{self.taxable_annual_income}")
        print(f"Total tax: ₹{self.total_tax}")
        print(f"Annual net salary: ₹{self.net_salary}")

    def Taxable_Income(self):
        print("\nTaxable Income Report:")
        self.taxable_annual_income = self.annual_gross_salary - 50000
        print(f"Annual gross salary: ₹{self.annual_gross_salary}")
        print("Taxable Income: ₹50000")
        print(f"The Taxable annual income: ₹{self.taxable_annual_income}")

    def calculate_tax(self):
        tax = 0
        print("\nTax break-down")
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
        print("\nNetsalary calculation: ")
        self.net_salary = self.annual_gross_salary - self.total_tax
        print(f"Gross annual salary: ₹{self.annual_gross_salary}")
        print(f"Total tax: ₹{self.total_tax}")
        print(f"Net annual salary: ₹{self.net_salary}")

class Negative_Number(Exception):
    '''Raised when the entered number is negative '''
    pass

class Salary_Limit(Exception):
    '''Raise when the salary is not in the limit of a employee's salary'''
    pass

class Allowance_Limit(Exception):
    '''Raise when the special allowance is not in the limit of a employee's salary'''
    pass

def Enter_Input(message: str) -> int:
    while True:
        try:
            number = int(input(message))
            if number <= 0 :
                raise Negative_Number("Number should be Postive integer!")
            return number
        except Negative_Number:
            print(Negative_Number)
        except ValueError:
            print("Number should be Postive integer!")

def Enter_name():
    while True:
        name = input("Enter employee's name: ").strip()
        if len(name) > 50:
            print("Atmost 50 characters")
        elif not name.replace(" ", "").isalpha():
            print("Alphabets only allowed to be a name")
        else: 
            return name
        
def Enter_EmpID():
    while True:
        EmpID = input("Enter employee's ID: ").strip()
        if 5 < len(EmpID) > 10: 
            print("EmpID should have only 5 - 10 character")
        elif not EmpID.isalnum():
            print("Alphanumeric characters only")
        else:
            return EmpID
        
def Enter_basic_salary():
    while True:
        try: 
            basic_salary = float(input("Enter the employee's basic salary: "))
            if basic_salary <= 0 or basic_salary :
                raise Salary_Limit("The salary should be in between [1, 10000000]")
            return basic_salary
        except Salary_Limit:
            print(Salary_Limit)
        except ValueError:
            print("Only positive numbers allowed")

def Enter_bonus():
    while True:
        try:
            bonus_percentage = input("Enter the Employee's bonus: ")
            if bonus_percentage < 0 or bonus_percentage > 100:
                raise ValueError
        except ValueError:
            print("Only Numbers between 0 - 100")

def Enter_special_allowance():
    while True:
        try:
            special_allowance = float(input("Enter the employee's special allowance: "))
            if special_allowance < 0 or special_allowance > 10000000:
                raise Allowance_Limit("The salary should be in between [1, 10000000]")
            return special_allowance
        except Allowance_Limit:
            print(Allowance_Limit)
        except ValueError:
            print("Only non-negative numbers allowed")
         
if __name__ == "__main__":
    n = Enter_Input("Enter number of employee: ")
    id = {}
    employee = [None] * n
    for i in range(n):
        name = Enter_name()
        EmpId = Enter_EmpID()
        basic_salary = Enter_basic_salary()
        special_allowance = Enter_special_allowance()
        bonus_percentage = Enter_bonus()
        employee[i] = Employee(name, EmpId, basic_salary, special_allowance, bonus_percentage)
        id[EmpId] = i

    print() # new line

    while True:
        person_id = input("Enter the employee's id: ")
        if person_id not in id:
            print(f"{person_id} is not present in the employee list")
        else:
            employee[id[person_id]].Report()