def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

num=int(input("Enter number: "))
print("Fibonacci series:",end=" ")
for i in range(num):
    print(fib(i),end=" ")
