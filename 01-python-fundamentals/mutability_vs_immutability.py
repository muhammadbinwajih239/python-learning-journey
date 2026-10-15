# Python Fundamentals: Mutability vs Immutability

# 1. Strings are immutable

name = "MUHAMMAD"

result = name.lower()

print("Original string:", name)
print("Lowercase result:", result)


# 2. Lists are mutable

numbers = [1, 2, 3]

numbers.append(4)

print("Updated list:", numbers)


# 3. sorted() returns a new sorted list

values = [3, 1, 2]

sorted_values = sorted(values)

print("Original values:", values)
print("New sorted list:", sorted_values)


# 4. sort() modifies the original list

values.sort()

print("Values after sort():", values)
