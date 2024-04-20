# 1. Read integers from "numbers.txt"
with open("numbers.txt", "r") as file:
    numbers = [int(num.strip()) for num in file.readlines()]
# 2. Separate integers into even and odd lists
# 3. Write even numbers to "even.txt"
# 4. Write odd numbers to "odd.txt"
# 5. Display completion message