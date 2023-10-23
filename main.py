students = []

def add_student(name):
    students.append({
        'name':name , 'math':None , 'history':None , 'english':None , 'computer_science':None , 'biology':None 
    })

def set_math_grade(student_name,grade):
    for student in students:
        if student['name'] == student_name :
            student['math'] = grade
            

def set_history_grade(student_name,grade):
    for student in students:
        if student['name'] == student_name :
            student['history'] = grade

def set_english_grade(student_name,grade):
    for student in students:
        if student['name'] == student_name :
            student['english'] = grade
                                    
def set_computer_grade(student_name,grade):
    for student in students:
        if student['name'] == student_name :
            student['computer_science'] = grade
                                                
def set_biology_grade(student_name,grade):
    for student in students:
        if student['name'] == student_name :
            student['biology'] = grade

def calculate_total_grade(student_name):
    for student in students:
        if student['name'] == student_name:
            total_grade = sum(grade for subject, grade in student.items() if subject != 'name')
            return total_grade

def display_students():
    print("List of students and their grades:")
    for student in students:
        total_grade = calculate_total_grade(student['name'])
        print(f"Name {student['name']} , Math: {student['math']}, History: {student['history']}, English: {student['english']}, Computer science: {student['computer_science']}, Biology: {student['biology']}, Total Grade: {total_grade} ")                                                       
add_student('Shahina')     
add_student('Alice')
set_math_grade('Shahina',90)
set_history_grade('Shahina',85)
set_english_grade('Shahina',98)
set_computer_grade ('Shahina',87)
set_biology_grade('Shahina',65)
set_math_grade('Alice',67)
set_history_grade('Alice',98)
set_english_grade('Alice',45)
set_computer_grade('Alice',57)
set_biology_grade('Alice',74)
display_students()