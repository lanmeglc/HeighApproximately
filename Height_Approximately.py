sex = input("Are you male or female? \n")
mom_height = input("What is your mom`s height? \n")
dad_height = input("What is your dad`s height? \n")
num = 13
num2 = 2
female_height = (int(mom_height) + int(dad_height) - int(num)) // int(num2)
male_height = (int(mom_height) + int(dad_height) + int(num)) // int(num2)

if sex == "female":
    print("If you are " + sex + " your height shall be approximately " + str(female_height) + "cm.")
elif sex == "male":
    print("If you are " + sex + " your height shall be approximately " + str(male_height) + "cm.")