def addition():
    a=1+2+1+1
    print(a)
    if a==3:
        print("A is 3")
        x="Gnanagowsalya is my friend"
        for x1 in x:
            print(x1)
        x=x.split(" ")
        for x2 in x:
            print(x2)
    elif a == 3 :
        print("A is Greaterthan")
        b="Santhiya is my friend"
        for x1 in b:
            print(x1)
        b=b.split(" ")
        for x2 in b:
            print(x2)
    elif a == 5 :
        print("A is Greaterthan Five")
        c="Santhiya is very bad girl"
        for x1 in c:
            print(x1)
        c=c.split(" ")
        for x2 in c:
            print(x2)
    y=input("Enter the Value").split()
    print(y)
addition()
