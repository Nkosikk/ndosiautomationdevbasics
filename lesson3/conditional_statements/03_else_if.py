# student_grade = int(input('Enter your grade'))   # can ask the user to input data
#student_grade = 50

student_grade = int(input('Enter the student grade: '))

if student_grade <= 59:
    print('E')
elif student_grade <= 69:
    print('D')
elif student_grade <= 79:
    print('C')
elif student_grade <= 89:
    print('B')
else:
    print('A')


