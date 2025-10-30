'''
Objective:
Practice creating Python classes, using object-oriented programming (OOP) concepts, and working with common Python data types like lists, tuples, sets, and dictionaries.

Instructions:
Create a Python script.
Implement all tasks using classes, objects, and methods.
Include comments to explain your code.
Submit the Github Repository with your completed work.
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
import re
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
    def getGrade(self):
        return self.grades
#Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.
    def grades_tuple(self):
        grades = (self.grades,)
        return grades
# Remove the first and last grade in grades
    def firstLast(self):
        l = len(self.grades)
        self.grades.pop(0)
        self.grades.pop(l-2)
        return self.grades
        # Validate that the student's email follows name@domain.com format
    def validate_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, self.email):
            print(f"{self.name}'s email '{self.email}' is valid.")
            return True
        else:
            print(f"{self.name}'s email '{self.email}' is INVALID.")
            return False

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
    '''
    Create a set of all unique grades across all students and print it.
Part 4: Tuple Practice
Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).
'''
    
    print('NIcks grades: ',Student.grades_tuple(nick))
    try:
        dontAddTupple = Student.grades_tuple(nick)
        #dontAddTupple.append('f')
        dontAddTupple[1]= 'f'
        print('Dont add ',dontAddTupple)
    except TypeError as e:
        print(f"Type Error {e}")
    
    #Remove the last grade from each student’s grades list using .pop().
    for student in [rick, samantha, nick]:
        removed_grade = student.grades.pop()  # removes and returns the last item
        print(f"Removed {removed_grade} from {student.name}'s grades. New list: {student.grades}")
    print(nick.getGrade())
    print(f'Remove 1st last {nick.firstLast()}' )
    #Print the number of grades each student has using len().
    print(f'Rick has {len(rick.grades)} grades Samantha has {len(samantha.grades)} grades Nick has {len(nick.grades)} grades')
    #Access and print the first and last grade for each student.
        # Access and print the first and last grade for each student.
    print("\nFirst and last grade of each student:")
    for student in [rick, samantha, nick]:
        if len(student.grades) >= 2:  # ensure at least two grades
            first_grade = student.grades[0]
            last_grade = student.grades[-1]
            print(f"{student.name}: First grade = {first_grade}, Last grade = {last_grade}")
        elif len(student.grades) == 1:
            print(f"{student.name}: Only one grade = {student.grades[0]}")
        else:
            print(f"{student.name} has no grades left.")
        #BONUS: Count how many grades are above 90 across all students
    count_above_90 = 0
    for student in [rick, samantha, nick]:
        # Convert grades to integers before comparing
        high_scores = [int(g) for g in student.grades if int(g) > 90]
        count_above_90 += len(high_scores)
        print(f"{student.name} has {len(high_scores)} grades above 90: {high_scores}")

    print(f"\nTotal number of grades above 90 across all students: {count_above_90}")
        #BONUS: Validate student emails
    print("\nEmail validation results:")
    for student in [rick, samantha, nick]:
        student.validate_email()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Interrupted by user. Exiting gracefully...")
    
    except AttributeError as e:
        print(f"Attribute Error- {e}")
    finally:
        print("Closing Student class")