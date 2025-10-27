'''
Objective:
Practice creating Python classes, using object-oriented programming (OOP) concepts, and working with common Python data types like lists, tuples, sets, and dictionaries.

Instructions:
Create a Python script.
Implement all tasks using classes, objects, and methods.
Include comments to explain your code.
Submit the Github Repository with your completed work.
 
Part 3: Dictionary & Set Integration

Create a set of all unique grades across all students and print it.
Part 4: Tuple Practice
Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.
Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).
Part 5: List Operations
Remove the last grade from each student’s grades list using .pop().
Access and print the first and last grade for each student.
Print the number of grades each student has using len().
Part 6: Bonus (Optional)
Use regular expressions to validate that each student’s email follows the format: name@domain.com.
Count how many grades are above 90 across all students.

'''

'''
Part 1: Class Definition
Create a class called Student with the following attributes:
name (string)
email (string)
grades (list of integers)
Add the following methods:
add_grade(self, grade): Adds a grade to the grades list.
average_grade(self): Returns the average of all grades.
display_info(self): Prints the student’s name, email, and grades.
'''
from collections import Counter
class Student:
    def __init__(self,name,email,grades):
        self.name = name
        self.email = email
        self.grades = grades
    #  Adds a grade to the grades list.
    def add_grade(self,grade):
        self.grades.append(grade)
    # Returns the average of all grades
    def average_grade(self):
        accumlative = 0
        for grade in self.grades:
            accumlative += int(grade)
        return accumlative / len(self.grades)
    #  Prints the student’s name, email, and grades
    def display_info(self):
        print(self.name, ' ',self.email,' ',self.grades)
    def get_student_by_email(self,email):
        print(email.get("name"))
    #Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().
    @staticmethod
    def get_student_by_email(student_dict, email):
        student = student_dict.get(email)
        if student:
            print(f"Found student: {student} from email {student.email} as {student.name}")
            return student
        else:
            print(f"No student found with that email of {email}")
            return None
def main():
    rick = Student("Rick","rick@gmail.com",['91','72','45','66','98','100'])
    samantha = Student("Samantha","samantha@gmail.com",['11','12','55','16','48','10'])
    nick = Student("Nick","nick@gmail.com",['90','98','45','86','91','100'])
    rick.add_grade('89')
    rick.add_grade('99')
    rick.display_info()
    
    samantha.add_grade('9')
    samantha.add_grade('19')
    samantha.display_info()
     
    nick.add_grade('98')
    nick.add_grade('92')
    nick.display_info()
     
      # Display and average
    for student in [rick, samantha, nick]:
        student.display_info()
        print(f"{student.name}'s Average:", student.average_grade())

    # Dictionary mapping emails to Student objects
    student_dict = {
        rick.email: rick,
        samantha.email: samantha,
        nick.email: nick
    }

    # Lookup students by email
    Student.get_student_by_email(student_dict, "nick@gmail.com")
    Student.get_student_by_email(student_dict, "samantha@gmail.com")
    Student.get_student_by_email(student_dict, "rick@gmail.com")
    Student.get_student_by_email(student_dict, "missing@gmail.com")

     # ✅ Collect all grades (flatten list)
    all_grades_list = []
    for student in student_dict.values():
        all_grades_list.extend(student.grades)

    # ✅ Unique grades (set)
    all_grades_set = set(all_grades_list)

    # ✅ Grade frequencies (Counter)
    grade_counts = Counter(all_grades_list)

    print("\nAll unique grades across all students:")
    print(sorted(all_grades_set, key=int))

    print("\nGrade frequencies across all students:")
    for grade, count in sorted(grade_counts.items(), key=lambda x: int(x[0])):
        print(f"Grade {grade}: {count} time(s)")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Interrupted by user. Exiting gracefully...")
    finally:
        print("Closing Student class")