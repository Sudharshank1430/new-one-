def countstrings(n,start):
    if n==0:
        return 1
    cnt=0
    for i in range (start,5):
        cnt+=countstrings(n-1,i)
    return cnt
def countvsting(n):
    return countstrings(n,0)
n=int (input("enter :"))
if(n<0):
    print("not less than 0")
else:
    print( countvsting(n))
