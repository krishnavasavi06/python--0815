p=int(input("Enter the principle Amount:"))
n=int(input("Enter the number of years:"))
sc=input("Senior citizen yes/no:")
g=input("Male/Female:")
if sc=="Y" and g=="M":
    print("SI=",(p*n*12)/100)
elif sc=="Y" and g=="F":
    print("SI=",(p*n*15)/100)
else:
    print("SI=",(p*n*10)/100)