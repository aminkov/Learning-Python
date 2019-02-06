#catching exceptions with try
#we can think of it as an if/else statement - try/except
try:
    w = float(input('weight:'))
except EOFError:
    print('THis is a EOFError...')
except ValueError:
    print('This is a ValueError, did you enter a number?')
else:
    print('If there is no exception, this will be printed')
finally:
    #do smth no matter if there was an exception or not
    print('this is the "Finally" block')
print(w)

print('END of the program')

#You can also use 'raise' to throw an exception

str = input('Enter a name: ')
if (str == 'pesho'):
    raise KeyboardInterrupt
