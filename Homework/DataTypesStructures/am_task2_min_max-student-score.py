""" Using the same information as in Task1, i.e.
Print out the name and score of the student with maximum score
Print out the name and score of the student with minimum score
 Maria - 5.5
Alex - 3.5 """
#code start
student_scores = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Mariya': 5.50,
    'Georgy': 5.00,
    'Georgi1':4.00,
}
# way 1
print("**********************")
print("Solution - way 1")
a=0
b=10
for i in student_scores:
    a = max(a, student_scores[i])
    b = min(b, student_scores[i])
for i in student_scores:
    if (a == student_scores[i]):
        print("{} - {}".format(i,student_scores[i]))
    if (b == student_scores[i]):
        print("{} - {}".format(i,student_scores[i]))
# way 2
print("**********************")
print("Solution - way 1")
a=0
listscores=[]
for i in student_scores:
    listscores.append(student_scores[i])
    a+=1
for i in student_scores:
    if (max(listscores) == student_scores[i]):
        print("{} - {}".format(i,student_scores[i]))
    if (min(listscores) == student_scores[i]):
        print("{} - {}".format(i,student_scores[i]))
print("**********************")
#code end
