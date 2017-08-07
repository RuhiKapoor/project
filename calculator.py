def add (a,b) :
    return a+b
def sub (a,b) :
    return a-b
def multiply (a,b) :
    return a*b
def divide (a,b) :
    return a/b
choice=input("Enter your choice")
if choice > 4 :
    print "invalid option"
    exit()
a=int(raw_input("Enter first no:"))
b=int(raw_input("Enter second no:"))

if choice == 1 :
    print (add(a,b))
if choice == 2 :
    print (sub(a,b))
if choice == 3:
    print (sub(a, b))
if choice == 4:
    print (sub(a, b))
