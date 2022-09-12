e=int(input("enter"))
c=int(input("old loaves"))
r=185
e*=185
c*=float (185*60/100)
total=float(e+c)
if(e>0):
    print("regular:",r)
    print("amout new:",e)
    print("amount old:",float(c))
    print("total amout:",total)
else:
          print("its invalid")
          
