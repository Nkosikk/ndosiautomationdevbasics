student_grade = int(input('Please enter student grade'))

if student_grade <= 59:
    print('E')
elif student_grade <= 69:
    print('D')
elif student_grade <= 79:
    print('C')
else:
    print('A')