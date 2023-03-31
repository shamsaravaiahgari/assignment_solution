from collections import namedtuple
# Get the number of students
num_students = int(input())
# Initialize a namedtuple with the input ordering
student = namedtuple("student", input().split())
# Calculate the total marks
total = sum(int(student(*input().split()).MARKS) for _ in range(num_students))
# Calculate the average marks and print it
print(total / num_students)
