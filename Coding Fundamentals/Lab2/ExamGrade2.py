grade = input ("Mark: ")
gradeint = int(grade)
level = input ("level: ")
levelint = int(level)

if levelint == 1:
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
elif levelint == 2:
    if gradeint > 100 or gradeint < 1:
        print("'Error: marks must be between 1 and 100")
    elif gradeint < 40:
        print("Grade: Fail")
    elif gradeint > 39 and gradeint < 51:
        print("Grade: Pass")
    elif gradeint > 50 and gradeint < 66:
        print("Grade: Merit")
    elif gradeint > 65 and gradeint < 101:
        print("Grade: Distinction")
    else:
        print("Error")
else:
    print("Error: Please input level 1 or 2")