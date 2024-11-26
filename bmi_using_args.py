def BMI_Calculator(**kwargs):
    name=kwargs.get('name')
    weight=kwargs.get('weight')
    height=kwargs.get('height')
    place=kwargs.get('place')
    bmi=weight/((height)**2)
    return bmi
def calc():
    for i in range(5):
        name=input("please enter your name")
        weight=float(input("enter your weight in kgs"))
        height=float(input("enter your height in meters"))
        place=input("enter your place")
        bmi=weight/((height)**2)
        if weight>0 and height>0:
            if bmi<18.5:
                print(f"{bmi} you are belongs to under weight category")
            elif bmi>=18.5 and bmi<=24.9:
                print(f"{bmi} you are in normal weight")
            elif bmi>=25 and bmi<=29.9:
                print(f"{bmi} you are belongs to over weight category")
            else:
                print(f"{bmi} you are in obesity")
        else:
            print("only positive values are accepted here")
  
calc()
