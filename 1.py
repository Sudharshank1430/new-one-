def isiso(a,b):
    if len(a)!=len(b):
        return False
    else:
        c,d={},{}
        for i in range (len(a)):
            e,f=a[i],b[i]
            if(e not in c):
                c[e]=f
            if(f not in d):
                d[f]=e
            if c[e]!=f or d[f]!=e:
                return False
    return True
a= input ("s:")
b=input("t:")
print(isiso(a,b))
                
