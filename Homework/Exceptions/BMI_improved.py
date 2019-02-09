bmi = 0
userdata = {}

def get_float_from_user(msg):
    inp = float(input(msg))
    return inp


def get_string_from_user(msg):
    inp = str(input(msg))
    return inp

def get_user_data():
    """retrieves user data from the command line
    Returns:
        [dictionary] of the form:
        {
            "name" : "user_name",
            "height": "user heigth in meters",
            "weight": "user weight in kilograms",
        }
    """
    global userdata
    while True:
        try:
            userdata['name'] = get_string_from_user("Please, enter your name: ")
        except ValueError:
            print("***Enter a number, please!")
        except EOFError:
            print("***Oops, something went wrong! Try again!")
        except KeyboardInterrupt:
            print("***Oops, something went wrong! Try again!")
        except BaseException:
            print("***Oops, something went wrong! Try again!")
        else:
            if len(userdata['name']) < 2:
                print("Your name must be longer than just 2 simbols")
                continue
            else:
                break

    while True:
        try:
            userdata['height'] = get_float_from_user("Please, enter your height(meters): ")
        except ValueError:
            print("***Enter a number, please!")
        except EOFError:
            print("***Oops, something went wrong! Try again!")
        except KeyboardInterrupt:
            print("***Oops, something went wrong! Try again!")
        except BaseException:
            print("***Oops, something went wrong! Try again!")
        else:
            if userdata['height'] <= 0.5 or userdata['height'] >= 2.5 :
                continue
            else:
                break

    while True:
        try:
            userdata['weight'] = get_float_from_user("Please, enter your weight(kg.): ")
        except ValueError:
            print("***Enter a number, please!")
        except EOFError:
            print("***Oops, something went wrong! Try again!")
        except KeyboardInterrupt:
            print("***Oops, something went wrong! Try again!")
        except BaseException:
            print("***Oops, something went wrong! Try again!")
        else:
            if userdata['weight'] <= 5 or userdata['weight'] >= 300 :
                continue
            else:
                break
    return userdata

def calc_BMI(w,h):
    """calculates the BMI
    Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]
    Returns:
        [float] -- [calculated BMI = w / (h*h)]
    """
    global bmi
    bmi = round((w / (h*h)),2)
    print('Your BMI index is: {}'.format(bmi))
    return bmi

def calc_BMI_category(bmi):
    """Calculates the BMI category
    Arguments:
        bmi {[float]} -- [the bmi number index]
    Returns:
        [string] -- [bmi category]
    """
    if bmi <= 15:
        return 'Very severely underweight'
    elif bmi > 15 and bmi <= 16:
        return 'Severely underweight'
    elif bmi > 16 and bmi <= 18.5:
        return 'Underweight'
    elif bmi > 18.5 and bmi <= 25:
        return 'Normal'
    elif bmi > 25 and bmi <= 30:
        return 'Overweight'
    elif bmi > 30 and bmi <= 35:
        return 'Moderately obese' 
    elif bmi > 35 and bmi <= 45:
        return 'Severely obese'
    elif bmi > 45 and bmi <= 60:
        return 'Super obese'
    elif bmi > 60:
        return 'Hyper Obese'

calc_BMI_category(bmi)

def print_results(bmi_category):
    """[Prints the BMI category to the user ]
    Arguments:
        bmi_category {[string]} -- []
    """
    print('Your BMI category is {}!'.format(bmi_category))

def cm_to_meters(cm):
    """converts centimetres to meters
    Arguments:
        cm {[int]}
    Returns:
        [float]
    """
    m = float(cm / 100)
    return m


user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)