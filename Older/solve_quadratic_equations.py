#a = int(input("Please, enter a: "))
#b = int(input("please enter b: "))
#c = int((input("please enter c: "))
a = input("Please, enter a: ")
b = input("please enter b: ")
c = input("please enter c: ")
#a = 2
#b = 1
#c = -3
print("your equation is: " + str(a) + "x^2" + str(b) + "x" + str(c) + " = 0 ")
a = int(a)
b = int(b)
c = int(c)
d = b*b -4*a*c
if d < 0:
    print("There are no roots")
elif d == 0:
    x1 = -b/2*a
    print("The equation has 1 solution: " + str(x1))
else:
    x1 = -(b+d**0.5)/2*a
    x2 = -(b-d**0.5)/2*a
    print("The equation has 2 roots: " + str(x1) + " and " + str(x2))