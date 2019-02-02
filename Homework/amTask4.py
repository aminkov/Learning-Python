""" Given are next list of words:
words = ["dog", "talent", "loop", "aria", "tent", "choice"]
Write a program which will find and output all of the words which starts and ends with same letter
Words which starts and end with same letter are:
talent
aria
tent """

words = ["dog", "talent", "loop", "aria", "tent", "choice"]
for i in words:
    length = len(i)
    if (i[0] == i[length-1]):
        print(i)

