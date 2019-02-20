# def greet(name):
#   print("Hello, {}".format(name))

# # a function can be passed as argument to another function
# def wrapper(f, n):
#   f(n)

# wrapper(greet, "Alex")


def solve_quadratics(a,b,c):
    d = b*b-4*a*c
    if d < 0:
        print("There are no roots")
    elif d > 0:
        x1 = (-b+d**0.5)/2*a
        x2 = (-b-d**0.5)/2*a
        print("There are two roots: {} and {}".format(x1,x2))
    else:
        x1 = -b/2*a
        print(f"There is one root: {x1}")

# solve_quadratics(2,4,-1)
        
def quadratic(a,b,c,function):
    function(a,b,c)
    print(f"{a}x^2 {b}x {c}")

# quadratic(2,4,-1, solve_quadratics)

def decorate_quadratics(a,b,c,function,f):
    print("*" * 100)
    f(a,b,c,function)
    print("*" * 100)

decorate_quadratics(2,4,-1, solve_quadratics, quadratic)