def sumsquare(l):
    odd,even=[],[]
    for items in l:
        if items %2==0:
            even.append(items)
        else:
           odd.append(items)
        square1, square2=[],[]
        total1,  total2=0,0
        total2=0
        for item in odd:
          square1.append(item**2)
        for item1 in even:
          square2.append(item1**2)
        for i in range(0,len(square1)):
          total1=total1+square1[i]
        for i in range(0,len(square2)):
          total2=total2+square2[i]
        final_answer=[]
        for j in total1,total2:
             final_answer.append(j)
        print(final_answer)
m=[]
x=int(input('enter max:'))
for i in range (0,x):
    ele=int(input())
    m.append(ele)
li=sumsquare(m)
    
