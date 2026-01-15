def fact(num):
    if num==0 or num==1:
        return 1
    
    return num * fact(num-1)

n = int(input("Enter a number : "))
result = fact(n)

print(f"The factorial of {n} is {result}")