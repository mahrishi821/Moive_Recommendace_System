while True:
    
    age=float(input("Enter the age of child::"))
    weight=float(input("Enter weight of child in weight (in kg) ::"))
    height=float(input("Enter height of child (in m) ::"))
    BMI=float((weight)/(height**2))

    if BMI<=18.0:
        print("Under Weight")
        
    elif BMI>18.0 and BMI<25:
        print("Healthy")
        
    elif BMI>=25.0:
        print("over weight")
    
    ans=input("Do you want to continue (press y/n)::")
    
    if ans=='y':
        
        print("\n Thanku for use BMI calculator")
        break
    