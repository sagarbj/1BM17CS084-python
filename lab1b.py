def fib(n):
    num1=0;
    num2=1;
    if n==1:
        print(num1)
    elif n==2:
        print(str(num1)+" , "+str(num2),end="")
    else:
         print(str(num1)+" , "+str(num2),end="")
    for i in range(2,int(n)):
        sum=num1+num2
        num1=num2
        num2=sum
        print(" , "+str(sum),end="")
n=input("enter the fibbonaci series to find :  ")
fib(int(n))
