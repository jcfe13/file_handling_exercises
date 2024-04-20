# 1. Read integers from "numbers.txt"
with open("numbers.txt", "r") as file:
    numbers = [int(num.strip()) for num in file.readlines()]
# 2. Separate integers into even and odd lists
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
# 3. Write even numbers to "even.txt"
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")
# 4. Write odd numbers to "odd.txt"
with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")
# 5. Display completion message