# if statement code challenge

try:

    #captures the student's name and grade 
    userInputStudentName = input("Please enter in the student's name: ")
    userInputGradePercentage = input("Please enter the student's grade percentage: ")
    studentGradePercentage = int(userInputGradePercentage)

    if (studentGradePercentage >= 90):
        print(userInputStudentName + " currently has an A")
    elif ((studentGradePercentage < 90) and (studentGradePercentage >= 80)):
        print(userInputStudentName + " currently has a B")
    elif ((studentGradePercentage < 80) and (studentGradePercentage >= 70)):
        print(userInputStudentName + " currently has a C")
    elif ((studentGradePercentage < 70) and (studentGradePercentage >= 60)):
        print(userInputStudentName + " currently has a D")
    else:
        print(userInputStudentName + " currently has a F")

except ValueError:
    print("No valid number")