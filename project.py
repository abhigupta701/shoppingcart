ld = {1:['abhi','abhi123','abhi',8435587742,'misrod']}
key = 0
item ={}
ikey = 0
ld1={}

udata=open("user_info.txt","r")
datax = udata.readlines()
a=(len(datax))
key+=a
for i in datax:
    data1=i.split(" ")
    ld[int(data1[0])]=[data1[1],data1[2],data1[3],int(data1[4]),data1[5]]
udata.close()

idata=open("item_info.txt","r")
datai = idata.readlines()
n=(len(datai))
ikey+=n
for i in datai:
    data1=i.split(" ")
    item[int(data1[0])]=[data1[1],data1[2],int(data1[3])]
idata.close()
def reg():
    global key
    key +=1
    us=input("enter username")
    ps=input("enter password")
    name=input("enter name")
    mn=int(input("enter phone number"))
    add=input("enter addaress")
    ld[key]=[us,ps,name,mn,add]

#data data storing in file
    
    user_data = open("user_info.txt", "a")
    data=[str(key),us,ps,name,str(mn),add]
    c=0
    for i in data:
        c+=1
        if c==6:
            user_data.writelines(i+"\n")
            c=0
        else:
            user_data.writelines(i+" ")
            
    user_data.close()

    

def login():
    us=input("enter user name")
    ps=input("enter password")
    
    for i in ld.keys():
        m=0
        a=[]
        for j in ld.get(i):
            m+=1
            if m==1:
                a.append(j)
            elif m==2:
                a.append(j)
            elif us == a[0] and ps == a[1]:
                return i
            else:
                print("wrong user name or password")
def admin():
    global ikey
    while True:        
        a=ld.get(1)
        print("welcome",a[0])
        print("press 1 for add item")
        print("press 2 for remove item")
        print("press 3 for viwe id items")
        print("press 4 for viwe user")
        print("press 5 for exit")
        choice=int(input("enter your choice"))
        if choice==1:
            while True:
                ikey +=1
                iname=input("enter item name")
                idetels=input("enter item details")
                iprice=int(input("enter item print"))
                item[ikey]=[iname,idetels,iprice]
                x=input("do you wanna continue y/n")
                    
                user_data = open("item_info.txt", "a")
                data=[str(key),iname,idetels,str(iprice)]
                c=0
                for i in data:
                    c+=1
                    if c==4:
                        user_data.writelines(i+"\n")
                        c=0
                    else:
                        user_data.writelines(i+" ")
                
                if x=="n":
                    break
        elif choice==2:
            dele=int(input("enter item id ro delete item"))
            if dele in item.keys():
                item.pop(dele)
                print("item is deleted")
            else:
                print("id not found")
        elif choice==3:
            x=item.keys()
            for i in x:
                a=0
                print("id :-",i)
                for j in item.get(i):
                    a+=1
                    if a==1:
                        print("item name:-",j)
                    elif a==2:
                        print("item details:-",j)
                    elif a==3:
                        print("price:-",j)
        elif choice==4:
            print(ld)
        elif choice==5:
            break
        else:
            print("wrong choice")
            
def user(ukey):
    ad=[]
    while True:
        a=ld.get(ukey)
        print("welcome",a[2])
        print("press 1 for shhoping")
        print("press 2 for cart")
        print("press 3 for logout")
        choice=int(input("enter your choice"))
        if choice == 1:
            while True:
                x=item.keys()
                for i in x:
                    a=0
                    print("id :-",i)
                    for j in item.get(i):
                        a+=1
                        if a==1:
                            print("item name:-",j)
                        elif a==2:
                            print("item details:-",j)
                        elif a==3:
                            print("price:-",j)
                z=int(input("enter id to add item into cart"))
                ad.append(z)
                en=input("do you wanna add more items y/n")
                if en=="n":
                    break
            
        elif choice==2:
            t=0
            for end in ad:
                c=0
                for f in item.get(end): 
                    c+=1
                    print(f)
                    if c==3:
                        t=t+int(f)
            print("your totle ammount is :-",t)
            
        elif choice==3:
            break
            
        else:
            print("wrong choice")


            
#main's part       
while True:
    print("press 1 for singup")
    print("press 2 for login")
    print("press 3 for exit")
    choice=int(input("enter your choice"))
    if choice==1:
        reg()
    elif choice == 2:
        k=login()
        if k==1:
            admin()
        else:
            user(k)
    elif choice==3:
        exit()
    else:
        print("wrong choice")
    
