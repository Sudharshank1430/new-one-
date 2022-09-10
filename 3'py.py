def num(a):
    sum=0;
    while(a):
        sum+=(a%10)*(a%10);
        a=int(a/10);
    return sum;
def happy(a):
    x=a;
    y=a;
    while(True):
        x=num(x);
        y=num(num(y));
        if(x!=y):
           continue;
        else:
            break;
    return(x==1);
a=int ( input ('n:'))
if( happy(a)):
    print("true");
else:
    print("false");
