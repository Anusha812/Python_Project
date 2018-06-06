print('RESTAURANT -- THE SHERATON -- MULTI CUISINE HOTEL'.center(100,'*'))
sch={0:" Vegetable Fried Rice ",1:" Chicken Chowmein ",2:" Crab Rangoon ",3:"Chicken Fried Rice ",4:" Egg Rolls ",5:" Sweet and Sour Soup ",6:" Orange Chicken ",7:" Sweet and Sour Pork ",8:" Egg Drop Soup ",9:"American chop suey "}
rch={0:150,1:200,2:250,3:200,4:150,5:100,6:250,7:200,8:150,9:150}
sit={0:" Chicken Pasta ",1:" Fetuccine Alfredo ",2:" Lasanga ",3:" Linguine with Clam Sauce ",4:" Veal Marsala ",5:" Chicken Pasta ",6:" Vegetable Pasta ",7:"Shrimp Fra ",8:" Penne Alla ",9:"Spagetti "}
rit={0:150,1:250,2:200,3:250,4:200,5:200,6:150,7:250,8:250,9:200}
sin={0:" Biryani ",1:" Butter Chicken ",2:" Paneer Butter Masala ",3:" Tandoori Chicken ",4:" Palak Paneer ",5:" Chole Bhature ",6:" Dal Makhani ",7:" Malai Kofta ",8:" Naan-Parathas ",9:"Idly-Dosa-Vada-Sambar "}
rin={0:150,1:200,2:250,3:200,4:150,5:100,6:250,7:200,8:150,9:150}
sdr={0:" Ice Tea ",1:" Virgin Mohito ",2:" Blue Lagoon ",3:" Grape Wine ",4:" Jaljeera ",5:" Badam Mild ",6:" Berry Blast ",7:" Cold Coffee ",8:"Tea ",9:"Expresso "}
rdr={0:40,1:50,2:40,3:50,4:30,5:40,6:50,7:50,8:30,9:50}
sde={0:" Kulfi ",1:" Rasgulla ",2:" Gulab Jamun ",3:" Rasmalai ",4:" Kheer ",5:" Boondi ka Laddu ",6:" Doodh ka Peda ",7:" Kaju Barfi ",8:" Faluda ",9:"Mysore Pak "}
rde={0:40,1:50,2:50,3:50,4:50,5:30,6:20,7:30,8:50,9:40}
sic={0:" Chocolate ",1:" Vanilla ",2:" Pista ",3:" Tender Coconut ",4:" Coffee ",5:" Strawberry ",6:" Butter Scotch ",7:" Black Current ",8:" Mango ",9:"Raspberry "}
ric={0:40,1:50,2:60,3:30,4:50,5:60,6:40,7:60,8:50,9:60}
q=0;a=0;e=0;i=0;o=0;u=0;
items=[]
rates=[]
done='no'
def head(h1):
    print(h1)
    print('item code','item name'.rjust(17),' item rate')
def menu(z1,z2,z3):
    while(z1<=9):
        print(z1,z2.get(z1).rjust(26),z3.get(z1))
        z1=z1+1
def apnd(r1,r2):
    w=int(input('enter your choice(in terms of the item code):'))
    print('your selected item is:',r1.get(w),'and its price is Rs.',r2.get(w))
    items.append(r1.get(w))
    rates.append(r2.get(w))
while(done=='no'):
 n=int(input('enter a number from 1 for chinese menu , 2 for italian menu, 3 for indian menu, 4 for drinks, 5 for desserts and 6 for icecreams'))
 while (n==1):
    head('chinese menu')
    menu(q,sch,rch)
    y=input('do u want to order any thing from this(y/n):')
    if (y=='y'):
        apnd(sch,rch)
    elif(y=='n'):
        break
    else:
        print('wrong choice')
 while (n==2):
    head('italian menu')
    menu(a,sit,rit)
    y=input('do u want to order any thing from this(y/n):')
    if (y=='y'):
        apnd(sit,rit)
    elif(y=='n'):
        break
    else:
        print('wrong choice')
 while (n==3):
    head('indian menu')
    menu(e,sin,rin)
    y=input('do u want to order any thing from this(y/n):')
    if (y=='y'):
        apnd(sin,rin)
    elif(y=='n'):
        break
    else:
        print('wrong choice')
 while (n==4):
    head('drinks menu')
    menu(i,sdr,rdr)
    y=input('do u want to order any thing from this(y/n):')
    if (y=='y'):
        apnd(sdr,rdr)
    elif(y=='n'):
        break
    else:
        print('wrong choice')
 while (n==5):
    head('dessert menu')
    menu(o,sde,rde)
    y=input('do u want to order any thing from this(y/n):')
    if (y=='y'):
        apnd(sde,rde)
    elif(y=='n'):
        break
    else:
        print('wrong choice')
 while (n==6):
    head('icecreams menu')
    menu(u,sic,ric)
    y=input('do u want to order any thing from this(y/n):')
    if (y=='y'):
        apnd(sic,ric)
    elif(y=='n'):
        break
    else:
        print('wrong choice')
 while(1):
     done=input('r u done(yes/no)')
     if (done!='yes' and done!='no'):
         print('wrong input')
     else :
         break
         
print("Your final order is:")
if(len(items)==0):
    print("empty")
else:
 for i,j in zip(items,rates):
      print(i,j)
if (input(("confirm order?(y/n)"))=="y"):
     print("the total price of the items you ordered is:",sum(rates),"INR")
     print("swachh bharath cess(0.5%):",0.005*sum(rates),"INR")
     print("your total bill will end up to:",1.005*sum(rates))
     print("thank you")
else:
    k=input("would you like to create another order or exit?(p/o/e)")
    if(k=="o"):
        import comp.py
    else:
        print("thank you.visit again")
