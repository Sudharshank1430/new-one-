try:
    n=int(input('enter:'))
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print ("it is a pallendrome ")
    else :
        print("it is not a pallendrome ")
except ValueError:
    print("invalid")
