"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students,
order their names alphabetically and print each one on a new line.
"""

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])

second_high = sorted(set([i[1] for i in students]))[1]
print("\n".join(sorted([i[0] for i in students if i[1] == second_high])))

"""
input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry
"""