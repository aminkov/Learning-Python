#catching exceptions with try
#we can think of it as an if/else statement - try/except
try:
    w = float(input('weight:'))
except:
    print('Please, enter a number')

print(w)
