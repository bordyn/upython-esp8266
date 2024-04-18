import json

# start with student record dict
student = {'name':'studen_A','score':3.0}

# dump into file
with open('student_a_file.json','w') as student_a_file:
    json.dump(student,student_a_file)

# dumping can also be done into 2 steps
student_record_str = json.dumps(student)
with open('student_a_file_string.txt','w') as student_file:
    student_file.write(student_record_str)

# load into dict
with open('student_a_file.json','r') as student_a_file:
    reading_student_a_dict = json.load(student_a_file)
print (reading_student_a_dict)

# loading can also be done into 2 steps
with open('student_a_file_string.txt','r') as student_file:
    student_record_str = student_file.read()
print (json.loads(student_record_str))
