# https://progressbg-python-course.github.io/ProgressBG-VMware-Python-Slides/pages/themes/dictAndSetDataTypes/dictAndSetDataTypes.html#/9/1
# Represent the information given in next table in appropriate data structure, named student_scores.
""" From student_scores data, create a new data structure named best_students_scores, storing the information (name and score) only for students with scores greater than 4.00
Print out the names of the students from best_students_scores
 Ivan
Maria
Georgy """
#code start
student_scores = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Mariya': 5.50,
    'Georgy': 5.00,
    'Georgi1':4.00,
}

print(student_scores)
best_students_scores = {}
for j in student_scores:
    if (student_scores[j]>=5):
        best_students_scores[j] = student_scores[j]

print(best_students_scores)
for i in best_students_scores:
    print(i)
#code end