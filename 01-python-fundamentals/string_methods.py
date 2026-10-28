name = "Muhammad Bin Wajih"

print(name)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

text = "  Hello Python  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

print(name.find("Bin"))
print(name.count("a"))
print(name.replace("Muhammad", "Mhmd"))
print(name.startswith("Muhammad"))
print(name.endswith("Wajih"))

print(name.split())
print(" ".join(["Python", "String", "Methods"]))

print("Muhammad".isalpha())
print("123".isdigit())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print("   ".isspace())
