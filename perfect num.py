def is_perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum== num
number=int(input("Enter the number:"))
if is_perfect_number(number):
    print(number,"is a perfect number")
else:
    print(number,"is not a perfect number.")
