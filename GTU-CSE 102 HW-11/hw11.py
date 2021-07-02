def add_room_to_end(number,floor,capacity):
    number=str(number)
    floor=str(floor)
    capacity=str(capacity)
    with open('room.txt','a',encoding='utf-8') as file:
        file.write(number+',')
        file.write(floor+',')
        file.write(capacity+'\n')

def add_room_after_room_number(number1,number2,floor,capacity):
    x=0
    number1=str(number1)
    number2=str(number2)
    floor=str(floor)
    capacity=str(capacity)
    with open('room.txt','r+',encoding='utf-8') as file:
        list1=file.readlines()
        for i in list1:
            l=i.split(',')
            if number1 in l:
                e=list1.index(i)
                list1.insert(e+1,number2+','+floor+','+capacity+'\n')
                file.seek(0)
                file.writelines(list1)
                x=x+1
    if x==0:
        add_room_to_end(number2,floor,capacity)


def add_customer_to_end(name,age,gender):
    age=str(age)
    
    with open ('customer.txt','a',encoding='utf-8') as file:
        file.write(name+',')
        file.write(age+',')
        file.write(gender+'\n')

def link_custormers_to_room(l5):
    l2=[]
    l3=[]
    with open('room.txt','r+') as file:
        l=file.readlines()
    with open('customer.txt','r+') as file:
        l1=file.readlines()
    for i in l:
        x=0
        i=i[:-1]
        a=i.split(',')
        for j in l1:
            b=j.split(',')
            if a[0]==b[0]:
                x=x+1
        if x==0:
            l2.append((a[0],a[2]))
    y=len(l5)
    print(l2)
    for i in l2:
        if i[1]==str(y) or i[1]==str(y+1):
            l3.append(i[0])
    if len(l3)!=0:
        with open('customer.txt','r+') as file:
            l1=file.readlines()
            if y==3:
                for i in l1:
                    a=i.split(',')
                    e=l1.index(i)
                    if a[0]==l5[0] or a[0]==l5[1] or a[0]==l5[2]:
                        a.insert(0,l3[0])
                        z=''
                        for r in a:
                            z=z+r+','
                        z=z[:-1]
                        l1.remove(i)
                        l1.insert(e,z)
                        file.seek(0)
                        file.writelines(l1)  
            elif y==2:
                for i in l1:
                    a=i.split(',')
                    e=l1.index(i)
                    if a[0]==l5[0] or a[0]==l5[1]:
                        a.insert(0,l3[0])
                        z=''
                        for r in a:
                            z=z+r+','
                        z=z[:-1]
                        l1.remove(i)
                        l1.insert(e,z)
                        file.seek(0)
                        file.writelines(l1)
            elif y==1:
                for i in l1:
                    a=i.split(',')
                    e=l1.index(i)
                    if a[0]==l5[0]:
                        a.insert(0,l3[0])
                        z=''
                        for r in a:
                            z=z+r+','
                        z=z[:-1]
                        l1.remove(i)
                        l1.insert(e,z)
                        file.seek(0)
                        file.writelines(l1)
    else:
        print('THERE İS NO ROOM AVAILABLE')

def show_vacancy():
    l2=[]
    with open('room.txt','r+') as file:
        l=file.readlines()
    with open('customer.txt','r+') as file:
        l1=file.readlines()
    for i in l:
        x=0
        i=i[:-1]
        a=i.split(',')
        for j in l1:
            b=j.split(',')
            if a[0]==b[0]:
                x=x+1
        if x==0:
            l2.append((a[0],a[1],a[2]))
    for i in l2:
        print(i)

def get_by_floor(floor):
    floor=str(floor)
    with open('room.txt','r+') as file :
        l=file.readlines()
    for i in l:
        l1=i.split(',')
        if floor==l1[1]:
            print(i)

def print_list():
    l3=[]
    
    with open('room.txt','r+') as file :
        l=file.readlines()
    with open('customer.txt','r+',encoding='utf-8') as file:
        l1=file.readlines()
    for i in l:
        l3=[]
        x=0
        i=i[:-1]
        a=i.split(',')
        
        for j in l1:
            j=j[:-1]
            b=j.split(',')
            
            if a[0]==b[0]:
                l3.append(j)
                x=1
        
        if x==1:
            l4=[]
            if len(l3)==1:
                for k in l3:
                    c=k.split(',')
                    for p in c:
                        l4.append(p)
                print("""
                Room {} (Floor {} - capacity {}x):
                ->{}({}-{})
                """.format(a[0],a[1],a[2],l4[1],l4[2],l4[3]))
            elif len(l3)==2:
                for k in l3:
                    c=k.split(',')
                    for p in c:
                        l4.append(p)
                print("""
                Room {} (Floor {} - capacity {}x):
                ->{}({}-{})
                ->{}({}-{})
                """.format(a[0],a[1],a[2],l4[1],l4[2],l4[3],l4[5],l4[6],l4[7]))
            elif len(l3)==3:
                for k in l3:
                    
                    c=k.split(',')
                    for p in c:
                        l4.append(p)
                print("""
                Room {} (Floor {} - capacity {}x):
                ->{}({}-{})
                ->{}({}-{})
                ->{}({}-{})
                """.format(a[0],a[1],a[2],l4[1],l4[2],l4[3],l4[5],l4[6],l4[7],l4[9],l4[10],l4[11]))
        else:
            print("""
                Room {} (Floor {} - capacity {}x):
                ->Empty
                """.format(a[0],a[1],a[2]))

            
while True:
    print("""
    1-ADD ROOM
    2-ADD ROOM AFTER ROOM NUMBER
    3-ADD CUSTOMER TO END
    4-LINK CUSTOMERS TO ROOM
    5-SHOW VACANCY
    6-GET BY FLOOR NUMBER
    7-PRINT ROOM AND CUSTOMER LIST
    """)
    t=int(input('Selection:'))
    if t==1:
        number=int(input('room number:'))
        floor=int(input('floor number:'))
        capacity=int(input('room capacity:'))
        add_room_to_end(number,floor,capacity)
        print('room added')
    elif t==2:
        number1=int(input('number1:'))
        number2=int(input('number2:'))
        floor=int(input('floor number:'))
        capacity=int(input('room capacity:'))
        add_room_after_room_number(number1,number2,floor,capacity)
    elif t==3:
        name=input('name:')
        age=int(input('age:'))
        gender=input('gender:')
        add_customer_to_end(name,age,gender)
    elif t==4:
        l5=[]
        print("""
        Enter the number of customers
        """)
        answer=int(input('number:'))
        if answer==1:
            name1=input('name:')
            l5.append(name1)
        if answer==2:
            name1=input('name1:')
            name2=input('name2:')
            l5.append(name1)
            l5.append(name2)

        if answer==3:
            name1=input('name1:')
            name2=input('name2:')
            name3=input('name3:')
            l5.append(name1)
            l5.append(name2)
            l5.append(name3)

        link_custormers_to_room(l5)
    elif t==5:
        show_vacancy()
    elif t==6:
        floor=int(input('floor number:'))
        get_by_floor(floor)
    elif t==7:
        print_list()





                
