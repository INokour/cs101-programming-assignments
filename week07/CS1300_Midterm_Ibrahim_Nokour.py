student_id = "2025-CS-0432"
student_email = "SMITH.JANE@SCHOOL.EDU"
course_code = "CS1300-001"

# Task 1:
print(student_id[0:4])
print(student_id[8:12])
print(student_email.lower().split("@")[0])

if course_code[0:2] == "CS":
    print("This is a CS course.")

new_id = f"{student_id[0:4]}_{student_id[8:12]}"
print(new_id)