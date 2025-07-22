def fact(n):
    temp=1
    if (n<2):
        return 1
    else:
        for i in range(n,0,-1):
            temp*=i
        return temp
         
a=int(input("Enter a number:"))       
x=fact(5)
print(f"Factorial of {a} is:{x}")
    