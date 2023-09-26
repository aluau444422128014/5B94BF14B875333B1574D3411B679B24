def sort_students(student_list):
  # Sort the student list in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
  return sorted_students


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


# Sample student objects
students = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.9),
    Student("David", "D004", 3.7),
]

# Test the sort_students function
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )
