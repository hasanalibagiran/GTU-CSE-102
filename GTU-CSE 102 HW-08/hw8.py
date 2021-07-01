import random
import time


s={6:'S-1',7:'M-11',17:'M-28',13:'P',25:'S-12',29:'B',40:'T',36:'B',32:'M-52',45:'S-22',48:'P',50:'B',60:'S-44',57:'M-77',54:'T',63:'S-52',66:'B',69:'M-77',79:'T',76:'M-83',73:'S-68',82:'B',85:'P',89:'M-94',99:'S-56',98:'S-72',93:'T'}
t=0
l=[]
l1=[]

for i in range(0,100,10):
    t=t+1     
    l1=[]
    for j in range(1,11):
        l1.append(i+j)
    if t%2!=0:
        for k in l1:
            l.append(k)
    else:
        l1.reverse()
        for k in l1:
            l.append(k)
l2=s.items()
l.reverse()
lc=[]
for i in l:
    lc.append(i)

for i,j in l2 :
    for k in range(0,100):
        if i==l[k]:
            lc[k]=(i,j)


def printer():
    t=-1
    for i in range(0,10):
        for j in range(0,10):
            t=t+1
            if type(lc[t])==tuple :
                print(lc[t][1],end='   ')
            else:
                print(lc[t],end='   ')
        print()

printer()

player1=1
player2=1
d=0
while True:
    printer()
    z=random.randint(1, 6)
    d=d+1
    
    if d%2!=0:
        print('Player1 is on {}'.format(player1))
        p=int(input('PRESS 1 FOR ROLLING DICE:'))
        print('rolling dice for player1'+'\n'+'dice rolled:{}'.format(z))
        r=player1+z
        e=l.index(r)
        if type(lc[e])==tuple:
            if lc[e][1]=='P':
                continue
            elif lc[e][1]=='B':
                player1=player1+z+5
            elif lc[e][1]=='T':
                player1=player1+z-5
            else:
                a=lc[e][1]
                l6=a.split('-')
                player1=int(l6[1])
        else:
            player1=player1+z
        print('Player1 is on {}'.format(player1))
    else:
        print('Player2 is on {}'.format(player2))
        p=int(input('PRESS 1 FOR ROLLING DICE:'))
        print('rolling dice for player2'+'\n'+'dice rolled:{}'.format(z))
        r=player2+z
        e=l.index(r)
        if type(lc[e])==tuple:
            if lc[e][1]=='P':
                continue
            elif lc[e][1]=='B':
                player2=player2+z+5
            elif lc[e][1]=='T':
                player2=player2+z-5
            else:
                a=lc[e][1]
                l6=a.split('-')
                player2=int(l6[1])
        else:
            player2=player2+z
        print('Player2 is on {}'.format(player2))
    if player1>=100:
        print('PLAYER1 WON')
        time.sleep(10)
        break
    elif player2>=100:
        print('PLAYER2 WON')
        time.sleep(10)
        break






