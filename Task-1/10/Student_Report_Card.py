class Student:
    name: str
    subject1: int
    subject2: int
    subject3: int

    def __init__(self, name: str, subject1 :int, subject2 :int, subject3 :int):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    def report_card(self):
        print("\n")
        print("*************Report Card************")
        total_score = self.subject1 + self.subject2 + self.subject3
        average_score = total_score / 3
        print("Name:", self.name)
        print("Total Score:", total_score)
        print(f"Average Score: {average_score:.2f}")
        
        if average_score >= 60:
            grade = "1st Class"
        elif average_score >= 50:
            grade = "2nd Class"
        elif average_score >= 35:
            grade = "Pass Class"
        else:
            grade = "Fail"
        print("Class:", grade)

class Out_of_score_range(Exception):
    '''Raised when the entered number is either less than zero or greater than zero'''
    pass

def Enter_Input(message: str) -> int:
    while True:
        try:
            score = int(input(message))
            if score < 0 or score > 100 :
                raise Out_of_score_range("Subject Score should be between 0 to 100")
            return score
        except Out_of_score_range:
            print(Out_of_score_range)
        except ValueError:
            print("Invalid input!")

if __name__ == "__main__":
    name = input("Enter the name of Student: ")
    subject1 = Enter_Input("Enter the marks of subject1: ")
    subject2 = Enter_Input("Enter the marks of subject2: ")
    subject3 = Enter_Input("Enter the marks of subject3: ")
    student = Student(name, subject1, subject2, subject3)

    student.report_card()