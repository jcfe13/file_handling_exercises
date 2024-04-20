# 1. Initialize variables to track the student with the highest GWA
highest_gwa = float('inf')
top_student = ''
# 2. Open the file and read all lines
with open("students_gwa.txt", "r") as file:
    for line in file:
        name, gwa_str = line.strip().split(',')
# 3. Display the student who achieved the highest GWA