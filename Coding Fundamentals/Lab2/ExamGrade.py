grade = input ("Mark: ")
gradeint = int(grade)

if gradeint > 100 or gradeint < 1:
    print("'Error: marks must be between 1 and 100")
elif gradeint < 50:
    print("Grade: Fail")
elif gradeint > 49 and gradeint < 61:
    print("Grade: Pass")
elif gradeint > 60 and gradeint < 71:
    print("Grade: Merit")
elif gradeint > 70 and gradeint < 101:
    print("Grade: Distinction")
else:
    print("Error")