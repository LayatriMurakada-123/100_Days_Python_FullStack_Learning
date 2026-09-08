'''
#BMI usecase --> BMI(Body Mass Index)

#weight --> kgs
#height --> metres
#feet --> inches --> inch --> 2.54

#BMI = (weight)/((height)**2)
n_of_t_user_input = int(input("Enter the value:"))
for i in range(n_of_t_user_input):
    #name
    name = input("Enter the UserName:")
    #weight = 75
    weight = float(input("Enter the weight in kgs:"))
    #height = 1.45
    height = float(input("Enter the height in metres:"))
    if weight > 0 and height > 0:
        BMI = (weight)/((height)**2)
        print("BMI:", BMI)

        #<18.5 --> Underweight
        if BMI < 18.5:
            print("Underweight")

        #18.5 - 24.9 --> Normal weight
        elif 18.5 <= BMI <= 24.9:
            print("Normal weight")

        #25 - 29.9 --> Overweight
        elif 25 <= BMI <= 29.9:
            print("Overweight")
        
        #>=30 --> Obesity
        elif BMI>=30:
            print("Obesity")
    else:
        print("Make sure to enter only +ve values")
'''

#Repition --> While
#Task --> Store the results of name , weight , height --> BMI into a collection
#Same above task we need to handle the errors(Exception Handling) and also make sure strictly to enter only numeric values

while True:
    
    #in this case we prefer Exception Handling
    try:
        name = input("Enter the name:")
        weight = float(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        if weight > 0 and height > 0:
            break
        else:
            print("Make sure to enter only +ve values")

    #except ValueError:
         #print("Invalid input! Please enter only numeric values.")
    except Exception as e:
        print(f"The Error  {e}")
BMI = weight / (height ** 2)
print(BMI)
# BMI Category
if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI <= 24.9:
    category = "Normal weight"
elif 25 <= BMI <= 29.9:
    category = "Overweight"
else:
    category = "Obesity"
print("Category:", category)         



