import sys
import os

def separate_text(text, delimiter, jumps):
    result = ""
    count = 0
    jump_index = 0

    for char in text:
        result += char
        count += 1

        if count == jumps[jump_index]:
            if jump_index < len(jumps) - 1:
                result += delimiter
            count = 0
            jump_index += 1

    return result.rstrip(delimiter)  # Remove the delimiter at the end, if necessary

def show_help():
    print("Usage: python main.py [file_path] [--help]")
    print("Description: This script separates the text in a file into specific groups of characters,")
    print("             adding a delimiter after a variable number of characters.")
    print("\nParameters:")
    print("  file_path: (optional) Path of the data file to be processed.")
    print("             If not provided, the user will be prompted to enter the path.")
    print("  --help: Display this help message.")

# Check if the --help parameter was provided
if "--help" in sys.argv:
    show_help()
    sys.exit(0)

# Check if the file path was provided as an argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = input("Enter the path of the data file: ")

delimiter = input("Enter the delimiter character: ")
jumps = []
while True:
    jump = input("Enter the number of characters to jump (0 to finish): ")
    if jump == '0':
        break
    jumps.append(int(jump))

# Read the contents of the file
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found!")
    sys.exit(1)

# Perform text separation for each line
separated_lines = []
for line in lines:
    separated_line = separate_text(line.strip(), delimiter, jumps)
    separated_lines.append(separated_line)

# Create the path for the result file
file_name = os.path.splitext(os.path.basename(file_path))[0]
result_path = os.path.join(os.path.dirname(file_path), file_name + "-converted.txt")

# Save the result to the text file
try:
    with open(result_path, 'w') as result_file:
        result_file.write('\n'.join(separated_lines))
except Exception as e:
    print("An error occurred while saving the file:", str(e))
    sys.exit(1)

print("Result file saved:", result_path)
