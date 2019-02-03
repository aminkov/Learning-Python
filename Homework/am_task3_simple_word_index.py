# Make a program which will count the words' frequency (the count) of a given text
#  apple and banana one apple one banana
# a red apple and a green apple
# a - 2
# green - 1
# banana - 2
# and - 2
# one - 2
# red - 1
# apple - 4

#code start
print("___________")
test = ("apple and banana one apple one banana a red apple and a green apple")
listtext = test.split(" ")
words_set = set(listtext)
for i in words_set:
    print("{} - {}".format(i,listtext.count(i)))
print("___________")
#code end

