a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

# find which one if biggest
if a>b and a>c:   
    print(f"{a} is biggest")

    # find the 2nd and 3rd number
    if b>c:
        print(f"{b} is bigger")
        print(f"{c} is big")
    else: 
        print(f"{c} is bigger")
        print(f"{b} is big")

elif b>a and b>c:
    print(f"{b} is biggest")

    # find the 2nd and 3rd number
    if a>c:
        print(f"{a} is bigger")
        print(f"{c} is big")
    else: 
        print(f"{c} is bigger")
        print(f"{a} is big")

else:
    print(f"{c} is biggest")

    # find the 2nd and 3rd number
    if a>b:
        print(f"{a} is bigger")
        print(f"{b} is big")
    else: 
        print(f"{b} is bigger")
        print(f"{a} is big")
