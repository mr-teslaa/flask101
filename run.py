# function
def findnumber():
    a = int(input("1st number: "))
    b = int(input("2nd number: "))
    c = int(input("3rd number: "))
    
    if a>b and a>c:
        print(f"{a} is big")
    elif b>a and b>c:
        print(f"{b} is big")
    else:
        print(f"{c} is big")

findnumber()