# Academy Attendance Tracker

# Student Records

students = {
    "S101": ("Ali", "Python"),
    "S102": ("Sara", "Python"),
    "S103": ("Ahmed", "Data Science"),
    "S104": ("Ayesha", "Data Science")
}

print("ACADEMY STUDENT RECORDS")

for student_id, details in students.items():
    name, course = details

    print(student_id, "-", name, "-", course)


# Search Student

search_id = input("Enter Student ID: ")

student = students.get(search_id)

if student:
    name, course = student

    print("Student Found")
    print("Name:", name)
    print("Course:", course)

else:
    print("Student Not Found")


# Attendance Records

saturday_attendance = {
    "S101", "S102", "S103"
}

sunday_attendance = {
    "S102", "S103", "S104"
}


# Attendance Comparison

print("ATTENDANCE COMPARISON")

all_attendance = saturday_attendance.union(sunday_attendance)

both_days = saturday_attendance.intersection(sunday_attendance)

saturday_only = saturday_attendance.difference(sunday_attendance)

one_day_only = saturday_attendance.symmetric_difference(sunday_attendance)

print("Total Students Present:", all_attendance)
print("Present Both Days:", both_days)
print("Saturday Only:", saturday_only)
print("Only One Day:", one_day_only)
