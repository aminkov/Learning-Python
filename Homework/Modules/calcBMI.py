import functionsBMI as f
bmi=0
f.calc_BMI_category(bmi)

user_data = f.get_user_data()
bmi = f.calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = f.calc_BMI_category(bmi)
f.print_results(bmi_category)