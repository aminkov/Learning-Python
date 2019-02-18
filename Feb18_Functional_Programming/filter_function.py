l = [1,2,3,4,5]

# even_l = []
# for i in l:
#     if i%2==0:
#         even_l.append(i)


# def is_even(i):
#     if i%2==0:
#         return True
#     else:
#         return False

# even_l = filter( is_even, l)
# print(list(even_l))

even_l = filter(lambda i: i%2==0, l)
print(list(even_l))

