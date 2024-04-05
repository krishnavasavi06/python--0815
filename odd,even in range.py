def odd_or_even(start,end):
    print("odd numbers between",start,"and",end,"are:")
    for num in range(start,end+1):
        if(num%2!=0):
            print(num,end=" ")
    print("\nEven numbers between",start,"and",end,"are:")
    for num in range(start,end+1):
        if num%2==0:
            print(num,end=" ")
            
start=int(input("Enter the starting number:"))
end=int(input("enter the ending number:"))
odd_or_even(start,end)
    