# 1. Specify input and output file names
input_file_name = 'integers.txt'
output_file_even_name = 'double.txt'
output_file_odd_name = 'triple.txt'
# 2. Open the input file for reading
with open(input_file_name, 'r') as infile:
    numbers = [int(line.strip()) for line in infile.readlines()]
# 3. Initialize lists to store even and odd numbers
even_numbers = []
odd_numbers = []
# 4. Classify numbers as even or odd
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
# 5. Calculate squares of even numbers and cubes of odd numbers
squared_evens = [num ** 2 for num in even_numbers]
cubed_odds = [num ** 3 for num in odd_numbers]
# 6. Write squared evens to output_file_even (double.txt)
with open(output_file_even_name, 'w') as outfile_even:
    for num in squared_evens:
        outfile_even.write(f"{num}\n")
# 7. Write cubed odds to output_file_odd (triple.txt)
# 8. Print success message