import mainBMI
userdata = {}
bmi = 0
calc_BMI_category(bmi)

user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)