#catching exceptions with try
#we can think of it as an if/else statement - try/except
try:
    w = float(input('weight:'))
except:
    print('Please, enter a number')
else:
    print('If there is no exception, this will be printed')
finally:
    #do smth no matter if there was an exception or not
    print('this is the "Finally" block')
print(w)

print('END of the program')
