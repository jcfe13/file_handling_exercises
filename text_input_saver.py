# 1. Initialize an empty list for lines of text
lines = []
# 2. Loop to get input lines from the user
while True:
    line = input("Enter line: ")
    lines.append(line)
    choice = input("Are there more lines? (y/n): ")
    if choice.lower() != 'y':
        break
# 3. Save lines to 'mylife.txt'
# 4. Display a completion message