import string
def decryption(e,l1,key):
    d=''
    for i in e :
        if i=="_":
            d=d+" "
        else:
            y=l1.index(i)
            if y+key>25:
                z=(y+key)-26
                d=d+l1[z]
            else:
                z=y+key
                d=d+l1[z]
    return d
a=string.ascii_lowercase    
l1=list(a)
e=''
with open("encyrpted.txt","r+",encoding='utf-8') as file:
    for i in file:
        e=e+i
    file.close()
key=int(input('your key:'))
x=decryption(e,l1,key)
with open("secretmessage.txt","w",encoding='utf-8') as file:
    file.write(x)


