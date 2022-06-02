student_first_name = input ("what is your first name?\n: ")
student_second_name = input ("what is your last name?\n: ")
degree_name = input ("what degree are you doing\n: ")
coursework_mark = float(input ("what mark was given on your coursework?\n: "))
exam_mark = float(input ("what was your first exam mark?\n: "))
second_exam_mark = float(input ("what was your second exam mark?\n: "))

module_mark =(coursework_mark*0.6)+(exam_mark*0.15)+(second_exam_mark*0.25)

print("your module mark is " + str(module_mark))