def  vote(age):
    if age>=18:
        print("You are eligible to vote.")
    else:
        print("you are not eligible to vote.")
        
age=int(input("Enter your age:"))
vote(age)
