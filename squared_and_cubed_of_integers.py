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
# 5. Calculate squares of even numbers and cubes of odd numbers
# 6. Write squared evens to output_file_even (double.txt)
# 7. Write cubed odds to output_file_odd (triple.txt)
# 8. Print success message