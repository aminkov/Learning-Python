names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
not_empty_names = filter(lambda s: s and s[0]=="A", names)

print( list(not_empty_names) )

names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
not_empty_names = filter(lambda s: s and len(s)==4, names)

print( list(not_empty_names) )



