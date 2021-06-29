import string
def encryption(key,encrypted,l):
    e=''
    for i in encrypted:
        
        if i==" " :
            e=e+"_"
        if i not in l:
            continue
        else:
            x=l.index(i)
            if x-key<0 :
                z=key-x
                x=-z
                e=e+l[x]
            else:
                x=x-key
                e=e+l[x]
    return e
encrypted=input('your message:')
key=int(input('encryption key:'))
a=string.ascii_lowercase
l=list(a)
r=encryption(key, encrypted,l)

with open("encyrpted.txt","w",encoding='utf-8') as file:
    file.write(r)



    
        
        
