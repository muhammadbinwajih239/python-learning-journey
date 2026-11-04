# ==========================================
# 1. A Simple Function
# ==========================================

def greet():
    print("Hello, World!")

greet()


# ==========================================
# 2. Function with a Parameter
# ==========================================

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Muhammad")


# ==========================================
# 3. Parameters and Arguments
# ==========================================

# Parameter: A variable written inside the function definition.
# Argument: The actual value passed when calling the function.

def introduce(name, city):
    print(f"My name is {name}.")
    print(f"I live in {city}.")

introduce("Muhammad", "Karachi")


# ==========================================
# 4. Function with Multiple Parameters
# ==========================================

def add_numbers(first_number, second_number):
    result = first_number + second_number
    print(f"Sum: {result}")

add_numbers(10, 20)


# ==========================================
# 5. Positional Arguments
# ==========================================

# Arguments are assigned according to their position.

def student_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student_info("Muhammad", 17)


# ==========================================
# 6. Keyword Arguments
# ==========================================

# Arguments are passed using parameter names.
# Their order does not matter.

def student_details(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student_details(age=17, name="Muhammad")


# ==========================================
# 7. Default Parameter Values
# ==========================================

# A default value is used when no argument is provided.

def greet_guest(name="Guest"):
    print(f"Welcome, {name}!")

greet_guest()
greet_guest("Muhammad")


# ==========================================
# 8. Function with a Return Statement
# ==========================================

# return sends a value back from the function.

def calculate_sum(first_number, second_number):
    result = first_number + second_number
    return result

total = calculate_sum(10, 20)

print(f"Total: {total}")


# ==========================================
# 9. Difference Between print() and return
# ==========================================

# print() displays a value on the screen.

def show_message():
    print("Learning Python Functions")

# return sends a value back to the caller.

def get_message():
    return "Learning Python Functions"

show_message()

message = get_message()
print(message)


# ==========================================
# 10. Function Returning a Calculated Value
# ==========================================

def multiply_numbers(first_number, second_number):
    return first_number * second_number

result = multiply_numbers(5, 4)

print(f"Multiplication: {result}")


# ==========================================
# 11. Local Variables
# ==========================================

# A local variable is created inside a function.
# It can be accessed within that function.

def show_local_variable():
    message = "This is a local variable."
    print(message)

show_local_variable()


# ==========================================
# 12. Global Variables
# ==========================================

# A global variable is created outside a function.
# It can be accessed inside functions in the same scope.

course_name = "Python"

def show_course():
    print(f"Current Course: {course_name}")

show_course()


# ==========================================
# 13. Using the global Keyword
# ==========================================

# The global keyword allows a function to modify
# a global variable.

score = 10

def update_score():
    global score
    score = 20

update_score()

print(f"Updated Score: {score}")


# ==========================================
# 14. Function with an if-else Condition
# ==========================================

# Functions can also contain conditions.

def check_number(number):
    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = check_number(10)

print(result)
