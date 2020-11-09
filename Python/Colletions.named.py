"""
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

task;
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name
Your task is to help Dr. Wesley calculate the average marks of the students.

Average = Sum of all marks / total students
"""

from collections import namedtuple

n = int(input())
a = input()
total = 0
Student = namedtuple('Student', a)
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/n))

"""
Input;
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Output;

78.00
"""
