a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=input("choose the function to do[+,-,/,*,**]:")

if c=='+':
    print(f"sum: {a+b}")

elif c=='-':
    print(f"subtraction: {a-b}")

elif c=='/':
    print(f"divide: {a/b}")

elif c=='*':
    print(f"multiplication: {a*b}")

elif c=='**':
    print(f"a power b: {a**b}")

else:
    print("incorrect data")