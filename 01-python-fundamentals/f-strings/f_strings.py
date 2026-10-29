from datetime import datetime

# 1. Insert variables into text
name = "Ali"
age = 17

print(f"Hello, {name}!")
print(f"{name} is {age} years old.")

# 2. Use multiple variables in one sentence
course = "Python"
level = "Beginner"

print(f"{name} is learning {course} at a {level} level.")

# 3. Perform simple calculations
first_number = 10
second_number = 5

print(f"Addition: {first_number} + {second_number} = {first_number + second_number}")
print(f"Multiplication: {first_number} * {second_number} = {first_number * second_number}")

# 4. Use string methods inside an f-string
student_name = "ali khan"

print(f"Uppercase name: {student_name.upper()}")
print(f"Title case name: {student_name.title()}")

# 5. Format decimal places
price = 1234.5678

print(f"Price with two decimal places: {price:.2f}")

# 6. Format large numbers with commas
population = 1234567

print(f"Population: {population:,}")

# 7. Format a decimal as a percentage
completion = 0.875

print(f"Completion: {completion:.1%}")

# 8. Align text left, right, and center
word = "Python"

print(f"Left aligned:   |{word:<12}|")
print(f"Right aligned:  |{word:>12}|")
print(f"Center aligned: |{word:^12}|")

# 9. Add leading zeros to a number
ticket_number = 7

print(f"Ticket number: {ticket_number:03d}")

# 10. Display the sign of a number
change = 25
negative_change = -25

print(f"Positive balance change: {change:+d}")
print(f"Negative balance change: {negative_change:+d}")

# 11. Display an integer in binary, octal, and hexadecimal
number = 42

print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")

# 12. Use the debug equals sign
student_name = "Ali"

print(f"{student_name=}")
print(f"{age=}")

# 13. Use string conversion specifiers
message = "café"

print(f"String conversion: {message!s}")
print(f"Representation: {message!r}")
print(f"ASCII representation: {message!a}")

# 14. Display literal curly braces
print(f"Literal braces: {{name}}")

# 15. Set field width and precision using variables
width = 10
precision = 2
measurement = 123.456

print(f"Measurement: |{measurement:{width}.{precision}f}|")

# 16. Format date and time
event_time = datetime(2026, 10, 30, 17, 45)

print(f"Date: {event_time:%d-%m-%Y}")
print(f"Time: {event_time:%I:%M %p}")
