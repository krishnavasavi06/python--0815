def digits(num):
    sum=0
    while(num>=0):
        d=num%10
        sum+=d
        num//=10
    return sum
num=int(input("enter the number:"))
result=digits(num)
print("sum of digits:",result)