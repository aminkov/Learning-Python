def get_float_from_user(msg):
    inp = float(input(msg))
    return inp

while True:
    try:
        user_height = get_float_from_user("I need to know your height in centimetres: ")
        user_weight = get_float_from_user("And your weight in kilograms: ")
        print("Your height is: {:5.2f}cm. and you weight {:.2f}kg.".format(user_height, user_weight))
    except ValueError:
        print("***Enter a number, please!")
    except EOFError:
        print("***Oops, something went wrong! Try again!")
    except KeyboardInterrupt:
        print("***Oops, something went wrong! Try again!")
    except BaseException:
        print("***Oops, something went wrong! Try again!")
    else:
        break

