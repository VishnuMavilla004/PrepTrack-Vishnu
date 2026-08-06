# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# TODO: Validate that the student name is not empty.
student_name = input("Enter student name: ")
while student_name == "":
    print("Student name cannot be empty")
    student_name = input("Enter the Student Name: ")

registration_number = input("Enter registration number: ")

#TODO: Validate that the registration number is not empty
while registration_number == "":
    print("Registration number cannot be empty")
    registration_number = input("Enter your registration number: ")

# TODO: Validate that the graduation year is between 2025 and 2027.
graduation_year = int(input("Enter graduation year: "))
while graduation_year < 2025 or graduation_year > 2027:
    print("Graduation year must be between 2025 and 2027")
    graduation_year = int(input("Enter your graduation year: "))

# TODO: Validate attendance between 0 and 100.
attendance = float(input("Enter attendance percentage: "))
while attendance < 0 or attendance > 100:
    print("Attendance must be between 0 and 100")
    attendance = float(input("Enter your attendance percentage: "))

# TODO: Accept only yes or no.
project_input = input("Has the student completed the required project? Enter yes or no: ")
while project_input != "yes" or project_input != "no":
    if project_input == "yes" or project_input == "no":
        break
    else:
        print("Please enter yes or no only")
        project_input = input("Has the student completed the required project? Enter yes or no: ")

project_completed = False

if project_input == "yes":
    project_completed = True
else:
    project_completed = False


# TODO: Accept only yes or no.
profile_input = input("Is the student profile verified? Enter yes or no: ")
while profile_input != "yes" or profile_input != "no":
    if profile_input == "yes" or project_input == "no":
        break
    else:
        print("Please enter yes or no only")
        profile_input = input("Is the student profile verified? Enter yes or no: ")

# TODO: Convert profile_input into True or False.
profile_verified = False

if profile_input == "yes":
    profile_verified = True
else:
    profile_verified = False


# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0
