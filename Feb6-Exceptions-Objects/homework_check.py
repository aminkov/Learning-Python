#sorting in dictionary

student_scores = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Mariya': 5.50,
    'Georgy': 5.00,
    'Georgi1':4.00,
}

def sort_by_last_letter(item):
    return item[0][-1:]

srt = sorted(student_scores.items(), key=sort_by_last_letter)
print(srt)