import random

def printer(l1,a,b,x):
    l1[x]='B'
    t=0
    for j in range(0,a):
        for k in range(0,b):
            print(l1[t],end='')
            t=t+1
        print()

l=['#','#','#',' ','F']
a=int(input('row number:'))
b=int(input('column number:'))
l1=[]
r=a*b

for i in range (0,a*b):
    if i>int(r/2) and l[4] not in l1:
        z=random.randint(0,4)
    else :
        z=random.randint(0,3)
    l1.append(l[z])
x=random.randint(0,a*b)

printer(l1,a,b,x)
l2=[' ']
energy=int(a*b/2)
print("""
1-MOVE UP: PRESS 8
2-MOVE DOWN : PRESS 2
3-MOVE RİGHT : PRESS 6
4-MOVE LEFT : PRESS 4
""")
while True:
    answer=int(input('answer:'))
    energy-=1
    if energy==0:
        print('FAINTED')
        break
    if answer==8:
        if x-b<0:
            print('out of map')
        else:
            l1[x]=l2[-1]
            x=x-b
            l2.append(l1[x])
            printer(l1,a,b,x)
    elif answer==2 :
        if x+b>a*b :
            print('out of map')
        else:
            l1[x]=l2[-1]
            x=x+b
            l2.append(l1[x])
            printer(l1,a,b,x)
    elif answer==6:
        try:
            l1[x]=l2[-1]
            x+=1
            l2.append(l1[x])
            printer(l1,a,b,x)
        except:
            print('out of map')
    elif answer==4:
        try:
            l1[x]=l2[-1]
            x-=1
            l2.append(l1[x])
            printer(l1,a,b,x)
        except:
            print('out of map')
    if l2[-1]=='F':
        print('i have found it')
        break
            




    
        
