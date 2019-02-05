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
print("____________")
test = ("apple and banana one apple one banana a red apple and a green apple")
listtext = test.split(" ")
#find lenght of the longest word
a=0
for i in listtext:
    a = max(a, len(i))
#eliminate duplicate words
words_set = set(listtext)
#create a dictionary with unique words
result_dict = {}
b=0
for i in words_set:
    result_dict[i] = listtext.count(i)
#sort dictionary by key value
sorted_d = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
#print formated result
for i,j in sorted_d:
    print("{:{field_size}} |{:^3}|".format(i,j,field_size = a))
print("____________")
#code end