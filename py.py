'''
Objective:
Practice creating Python classes, using object-oriented programming (OOP) concepts, and working with common Python data types like lists, tuples, sets, and dictionaries.

Instructions:
Create a Python script.
Implement all tasks using classes, objects, and methods.
Include comments to explain your code.
Submit the Github Repository with your completed work.
 
Part 3: Dictionary & Set Integration
Create a dictionary called student_dict that maps each student’s email to their corresponding Student object.
Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().
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

def main():
    rick = Student("Rick","rick@gmail.com",['91','72','45','66','98','100'])
    samantha = Student("Samantha","samantha@gmail.com",['11','12','55','16','48','10'])
    nick = Student("Nick","nick@gmail.com",['90','98','45','86','91','100'])
    rick.add_grade('89')
    rick.add_grade('99')
    rick.display_info()
    print("Ricks Average ",rick.average_grade())
    samantha.add_grade('9')
    samantha.add_grade('19')
    samantha.display_info()
    print("Samanthas Average ",samantha.average_grade())
    nick.add_grade('98')
    nick.add_grade('92')
    nick.display_info()
    print("Nicks Average ",nick.average_grade())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Interrupted by user. Exiting gracefully...")
    finally:
        print("Closing Student class")