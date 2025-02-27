# write a function that find bmi
# define function
def getbmi(weight=0,height=0):

    if weight==0 or height==0:
        print("give valid input....")

    else:
        height = height/100

        bmi = weight / (height**2)
        print(round(bmi,2))

        if(bmi<=18.5):
            print("underweight")

        elif bmi>18.5 and bmi<24.9:
            print("normal weight")

        elif bmi>=25 and bmi<30:
            print("overweight")

        elif bmi>30:
            print("obesity")

# call function
getbmi(50.3,189)

getbmi()    

getbmi(50)