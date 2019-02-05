# https://progressbg-python-course.github.io/ProgressBG-VMware-Python-Slides/pages/themes/functions/functions.html#/17
# Write a program which will calculate a user BMI.
# Split your logic into functions, and organise your program as given bellow:
userdata = {}
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
#     while True:
#         global userdata
#         userdata['name'] = input("Please, enter your name: ")
#         if len(userdata['name']) < 2:
#             continue
#         else:
#             break
#     while True:
#         userdata['height'] = float(input("Please, enter your height(meters): "))
#         if userdata['height'] <= 50 or userdata['height'] >= 250 :
#             continue
#         else:
#             break
#     while True:
#         userdata['weight'] = float(input("Please, enter your weight(kg.): "))
#         if userdata['weight'] <= 5 or userdata['weight'] >= 300 :
#             continue
#         else:
#             break    
#     print(userdata)
# get_user_data()

userdata = {'weight': 67.0, 'height': 67.0, 'name': 'yy'}

def calc_BMI(w,h):
    """calculates the BMI

    Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]

    Returns:
        [float] -- [calculated BMI = w / (h*h)]
    """
    bmi = w / (h*h)
    return bmi
    print(bmi)


calc_BMI(userdata['height'],userdata['weight'])

# def calc_BMI_category(bmi):
#   """Calculates the BMI category



#   Arguments:
#     bmi {[float]} -- [the bmi number index]

#   Returns:
#     [string] -- [bmi category]
#   """
#   pass

# def print_results(bmi_category):
#   """[Prints the BMI category to the user ]

#   Arguments:
#     bmi_category {[string]} -- []
#   """
#   pass

# def cm_to_meters(cm):
#   """converts centimetres to meters

#   Arguments:
#     cm {[int]}

#   Returns:
#     [float]
#   """
#   pass

# user_data = get_user_data()
# bmi = calc_BMI(user_data["weight"],user_data["height"] )
# bmi_category = calc_BMI_category(bmi)
# print_results(bmi_category)