import mysql.connector
mys=mysql.connector.connect(host='localhost',user='root',password='2003')
cursor=mys.cursor()
cursor.execute('create database if not exists Hotel_Management')
mys.commit()
mys=mysql.connector.connect(host='localhost',user='root',password='',database ='Hotel_management')
cursor=mys.cursor()
print("==========================================================",)
print("=========WELCOME TO G.P.A HOTAL & RESTAURANT===========",)
print("==========================================================",)

############Customer Details#############
def room_1():
    cursor.execute("create table if not exists Rooms(Room_no integer(3) primary key,Name varchar(25),Age integer (3),Gender varchar(8),Address varchar(25),Phone_no varchar(13))")
    global Room_no
    Room_no=input('Enter Room No:')
    global Name
    Name=input('Enter Your Name:')
    Age=input('Enter Your Age:')
    Gender=input('Enter Your Gender:')
    Address=input('Enter Your Address:')
    Phone_no=input('Enter Your Phone Number:')
    value="INSERT INTO Rooms (Room_no,Name,Age,Gender,Address,Phone_no) VALUES (%s,%s,%s,%s,%s,%s)"
    record=(Room_no,Name,Age,Gender,Address,Phone_no)
    cursor.execute(value,record)
    mys.commit()


############Billing#####################
def billing():
    cursor.execute("create table if not exists Bills(Room_no integer(3),Name varchar(25),Check_in varchar(20),Check_out varchar(20),Days integer(3),Room_type  varchar(15),Room_charges  integer(5),Total  integer(6))")
    chin=input("Check In [yyyy-mm-dd]:-")
    chout=input("Check Out [yyyy-mm-dd]:-")
    days=int(input("No Of Days:-"))
    room_1()
    bil="INSERT INTO Bills (Room_no,Name,Check_in,Check_out,Days,Room_type,Room_charges,Total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    rec=(Room_no,Name,chin,chout,days,rt,ch,ch*days,)
    cursor.execute(bil,rec)
    mys.commit()
    print("\nNew Customer Details Entered Successfully !")
    print("~~~~~~~~~~BooKing Details~~~~~~~~~~~~~~\n".center(125))
    da="SELECT Room_no,Name,Room_type,Days,Room_charges FROM Bills where Room_no=%s"
    cursor.execute(da,(Room_no,))
    data=cursor.fetchone()
    print("Room.no, Name,	Rtype, Days, Rcharge,")
    print(data)
    co=input("Do You Want To Go Back[Y/N]:")
    if co in["y","Y"]:
        hotel()
    elif co in["n","N"]:
        print("-------------------Thank You For Booking In G.P.A	")
        print("	Visit Again	")
    else:
        print("xxxxxxxxxxxxxxxxxx Invalid Entry xxxxxxxxxxxxxxxxxxxxxxxxxx")

#############Booking info###############
def bookinginfo():
    print("a.Search Your Room by Room Number")
    print("b.Search your room by Coustmer Name")
    print("c.Show All Booking Details")
    info=input("Enter Your choice:")
    if info in["a","A"]:
        p=int(input("Enter Your Room Number:"))
        bookin="SELECT * FROM Bills where Room_no=%s"
        cursor.execute(bookin,(p,))
        book=cursor.fetchall()
        if book==[]:
            print("@@@@@@@@These Room Is Empty@@@@@@@@@@".center(125))
        else:
            print("="*89)
            print("R.NO ,	Name	, Check_in	,Check_out,Days,Room_type R.Charge,Total")
            print("-"*156)
            print(book)
            print("="*89)
        hotel()

    elif info in ["b","B"] :
       p=input("Enter Your Name:")
       bookin="SELECT * FROM Bills where Name=%s"
       cursor.execute(bookin,(p,))
       book=cursor.fetchall()
       if book==[]:
           print("There Is No Booking in The Name Of",p) 
       else:
           print("="*89)
           print("R.NO ,	Name	,	Check_in	,Check_out,Days,Room_type R.Charge,Total")
           print("-"*156)
           for i in book:
               print(i)
               print("-"*156)
           print("="*89)
           hotel()
    elif info in ["c","C"] :
          cursor.execute('SELECT * FROM Bills')
          book=cursor.fetchall()
          print("="*89)
          print("R.NO ,	Name	,	Check_in	,Check_out,Days,Room_type R.Charge,Total")
          print("-"*156)
          for i in book:
              print(i)
              print("-"*156)
          print("="*89)
          hotel()
    else:
        print("	!!Invalid Entry!!	")
        bookinginfo()

       
     
#############Room Details#############
def rooms():
    global rt
    global ch
    print('''\n====================
============Rooms & Suites====
============================''')
    print('''What Would U Like To Prefer
1.	Do You Want To Book A Room
2.	Special Suites For You
3.	Booking Info''')
    b=int(input("Enter your choice:-"))
    if b==1:
        print('''~~~~~~Types Of Room~~~~~
1.	Single  Room-AC.........Charges@1000/-.........
2.	Single Room-Non AC.........Charges@700/-.........
3.	Double  Room-AC.........Charges@1500/-.........
4.	Double Room-Non AC.........Charges@1100/-.........
5.	Main Menu''')

        c=int(input("Enter Your Choice:-"))
        if c==1:
            rt="Single AC"
            ch=1000
            billing()
        elif c==2:
            rt="Single Non AC"
            ch=700
            billing()
        elif c==3:
             rt="Double AC"
             ch=1500
             billing()
        elif c==4:
              rt="Double Non AC"
              ch=1100
              billing()
        elif c==5:
              hotel()
    elif b==2:
        print('''~~~~~~Special Suites~~~~~~
1.	Deluxe  suite.........Charges@4000/-.........
2.	Executive  suite.........Charges@5000/-.........
3.	Luxery  suite.........Charges@7000/-.........
4.	Main menu''')
        d=int(input("Enter Your Choice:"))
        if d==1:
            rt="Deluxe suite"
            ch=4000
            billing()
        elif d==2:
            rt="Executive suite"
            ch=5000
            billing()
        elif d==3:
            rt="Luxery suite"
            ch=7000
            billing()
        elif d==4:
            hotel()
    elif b==3:
        print("~~~~~~~~~~~~~~~~!!Booking Info!!~~~~~~~~~~~~~~~~~~~~~~~~~~")
        bookinginfo()
    else:
        print("xxxxxxxxxxxxxxxxxInvaid Entryxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        rooms()

############Cancel Booking####################
def cancelbooking():
    print("!!Do You Want To Cancel Your Booking!! ")
    choice=input("Y or N :-")
    if choice in ["Y","y"]:
        print("a.Cancel Booking by Room No:")
        print("B.Cancel Booking by Your Name")
        q=input("a or b:")
        if q in["a","A"]:
            r=int(input("Enter Your Room Number:"))
            t="SELECT * FROM Rooms where Room_no=%s"
            cursor.execute(t,(r,))
            candata=cursor.fetchall()
            if candata==[]:
                print("@@@@@@@These Room Is Alredy Empty@@@@@".center(125))
            else:
                print(candata)
                delet='Delete from Rooms where Room_no=%s'
                cursor.execute(delet,(r,))
                mys.commit()
                delet='Delete from bills where Room_no=%s'
                cursor.execute(delet,(r,))
                mys.commit()
                print("	Booking Canceled	")
                print("	The Room Is Empty Now	")
        elif q in ["b","B"]:
           r=input("Enter Your Name:")
           t="SELECT * FROM Rooms where Name=%s"
           cursor.execute(t,(r,))
           candata=cursor.fetchall()
           if candata==[]:
               print("@@@@@@There is no booking in the name of",r,"@@@@@@@")
           else:
                print(candata)
                delet='Delete from Rooms where Name=%s'
                cursor.execute(delet,(r,))
                mys.commit()
                delet='Delete from bills where Name=%s'
                cursor.execute(delet,(r,))
                mys.commit()
                print("	Booking Canceled	")
                print("	The Room Is Empty Now	")
    elif choice in ["n","N"]:
        hotel()
              
    else:
        print(" *****Invalid Entry*********")
        cancelbooking()

############Restaurant Items###################
def resitems():
    cursor.execute("create table if not exists resitems(Item_no integer(2),Item_Name varchar(25),Item_price integer(4))")
    cursor.execute('INSERT INTO resitems VALUES (1,"Regular Tea",20)')
    cursor.execute('INSERT INTO resitems VALUES (2,"Masala Tea",25)')
    cursor.execute('INSERT INTO resitems VALUES (3,"Coffee",25)')
    cursor.execute('INSERT INTO resitems VALUES (4,"Cold Drink",25)')
    cursor.execute('INSERT INTO resitems VALUES (5,"Bread Butter",30)')
    cursor.execute('INSERT INTO resitems VALUES (6,"Bread Jam",30)')
    cursor.execute('INSERT INTO resitems VALUES (7,"Veg. Sandwich",50)')
    cursor.execute('INSERT INTO resitems VALUES (8,"Veg. Toast Sandwich",50)')
    cursor.execute('INSERT INTO resitems VALUES (9,"Cheese Toast Sandwich",70)')
    cursor.execute('INSERT INTO resitems VALUES (10,"Grilled Sandwich",70)')
    cursor.execute('INSERT INTO resitems VALUES (11,"Tomato Soup",110)')
    cursor.execute('INSERT INTO resitems VALUES (12,"Hot & Sour",110)')
    cursor.execute('INSERT INTO resitems VALUES (13,"Veg. Noodle Soup",110)')
    cursor.execute('INSERT INTO resitems VALUES (14,"Sweet Corn",110)')
    cursor.execute('INSERT INTO resitems VALUES (15,"Veg. Munchow",110)')
    cursor.execute('INSERT INTO resitems VALUES (16,"Shahi Paneer",110)')
    cursor.execute('INSERT INTO resitems VALUES (17,"Kadai Paneer",110)')
    cursor.execute('INSERT INTO resitems VALUES (18,"Handi Paneer",120)')
    cursor.execute('INSERT INTO resitems VALUES (19,"Palak Paneer",120)')
    cursor.execute('INSERT INTO resitems VALUES (20,"Chilli Paneer",140)')
    cursor.execute('INSERT INTO resitems VALUES (21,"Matar Mushroom",140)')
    cursor.execute('INSERT INTO resitems VALUES (22,"Matar Mushroom",140)')
    cursor.execute('INSERT INTO resitems VALUES (23,"Jeera Aloo",140)')
    cursor.execute('INSERT INTO resitems VALUES (24,"Malai Kofta",140)')
    cursor.execute('INSERT INTO resitems VALUES (25,"Aloo Matar",140)')
    cursor.execute('INSERT INTO resitems VALUES (26,"Dal Fry",140)')
    cursor.execute('INSERT INTO resitems VALUES (27,"Dal Makhani",150)')
    cursor.execute('INSERT INTO resitems VALUES (28,"Dal Tadka",150)')
    cursor.execute('INSERT INTO resitems VALUES (29,"Plain Roti",15)')
    cursor.execute('INSERT INTO resitems VALUES (30,"Butter Roti",15)')
    cursor.execute('INSERT INTO resitems VALUES (31,"Tandoori Roti",20)')
    cursor.execute('INSERT INTO resitems VALUES (32,"Butter Naan",20)')
    cursor.execute('INSERT INTO resitems VALUES (33,"Plain Rice",90)')
    cursor.execute('INSERT INTO resitems VALUES (34,"Jeera Rice",90)')
    cursor.execute('INSERT INTO resitems VALUES (35,"Veg Pulao",110)')
    cursor.execute('INSERT INTO resitems VALUES (36,"Peas Pulao",110)')
    cursor.execute('INSERT INTO resitems VALUES (37,"Plain Dosa",100)')
    cursor.execute('INSERT INTO resitems VALUES (38,"Onion Dosa",110)')
    cursor.execute('INSERT INTO resitems VALUES (39,"Masala Dosa",130)')
    cursor.execute('INSERT INTO resitems VALUES (40,"Paneer Dosa",130)')
    cursor.execute('INSERT INTO resitems VALUES (41,"Rice Idli",130)')
    cursor.execute('INSERT INTO resitems VALUES (42,"Sambhar Vada",140)')
    cursor.execute('INSERT INTO resitems VALUES (43,"Vanilla",60)')
    cursor.execute('INSERT INTO resitems VALUES (44,"Strawberry",60)')
    cursor.execute('INSERT INTO resitems VALUES (45,"Pineapple",60)')
    cursor.execute('INSERT INTO resitems VALUES (46,"Butter Scotch",60)')
    mys.commit()
    print("data entered successfull")

############Restaurant Bills###################

def resbill():
    s=0
    name=input(" Please Enter Your Name:- ")
    cursor.execute("create table if not exists Resbill(Name varchar (25),Room_no int(3),Item_1 varchar(25),Item_2 varchar(25),Item_3 varchar(25),Item_4 varchar(25),Item_5 varchar(25),Item_6 varchar(25),Item_7 varchar(25),Total int (5))")
    bevarages=int(input("Bevarages (1-10):"))
    if bevarages==1:
        rb="Regular Tea"
        rb1="20"
    elif bevarages==2:
        rb="Masala Tea"
        rb1="25"
    elif bevarages==3:
        rb="Coffee Tea"
        rb1="25"
    elif bevarages==4:
        rb="Regular Tea"
        rb1="25"
    elif bevarages==5:
        rb="Regular Tea"
        rb1="30"
    elif bevarages==6:
        rb="Regular Tea"
        rb1="30"
    elif bevarages==7:
        rb="Regular Tea"
        rb1="50"
    elif bevarages==8:
        rb="Regular Tea"
        rb1="50"
    elif bevarages==9:
        rb="Regular Tea"
        rb1="70"
    elif bevarages==10:
        rb="Regular Tea"
        rb1="70"
    soups=int(input("Soups (11-15):"))
    if soups==11:
        rs="Tomata Soup"
        rs1="110"
    elif soups==12:
        rs="Hot & Sour"
        rs1="110"
    elif soups==13:
        rs="Veg Noodle Soup"
        rs1="110"
    elif soups==14:
        rs="Sweet Corn"
        rs1="110"
    elif soups==15:
        rs="Veg. Munchow "
        rs1="110"
    maincourse=int(input("Main Course (16-28):"))
    if maincourse==16:
        rm="Shahi Paneer"
        rm1="110"
    elif maincourse==17:
        rm="Kadai Paneer"
        rm1="110"
    elif maincourse==18:
        rm="Handi Paneer"
        rm1="120"
    elif maincourse==19:
        rm="Palak Paneer"
        rm1="120"
    elif maincourse==20:
        rm="Chilli Paneer"
        rm1="140"
    elif maincourse==21:
        rm="Matar Mushroom"
        rm1="140"
    elif maincourse==22:
        rm="Mix Veg"
        rm1="140"
    elif maincourse==23:
        rm="Jeera Aloo"
        rm1="140"
    elif maincourse==24:
        rm="Malai Kofta"
        rm1="140"
    elif maincourse==25:
        rm="Aloo Matar"
        rm1="140"
    elif maincourse==26:
        rm="Dal Fry"
        rm1="140"
    elif maincourse==27:
       rm="Dal Makhani"
       rm1='150'
    elif maincourse==28:
       rm="Dal Tadka"
       rm1='150'
    roti=int(input("Roti (29-32):"))
    if roti==29:
       ro="Plain Roti"
       ro1='15'
    elif roti==30:
       ro="Butter Roti"
       ro1='15'
    elif roti==31:
       ro="Tandoori Roti"
       ro1='20'
    elif roti==32:
       ro="Butter Naan" 
       ro1='20'
    rice=int(input("Rice (33-36):"))
    if rice==33:
       rc="Plain Rice"
       rc1='90'
    elif rice==34:
       rc="Jeera Rice"
       rc1='90'
    elif rice==35:
       rc="Veg Pulao"
       rc1='110'
    elif rice==36:
       rc="Peas Pulao"
       rc1='110'
    south=int(input("South Indian (37-42):"))
    if south==37:
       ru="Plane Dosa"
       ru1='100'
    elif south==38:
       ru="Onion Dosa"
       ru1='110'
    elif south==39:
       ru="Masala Dosa"
       ru1='130'
    elif south==40:
       ru="Paneer Dosa"
       ru1='130'
    elif south==41:
       ru="Rice Idli"
       ru1='130'
    elif south==42:
       ru="Sambar Vada"
       ru1='140'
    ice=int(input("Ice Cream (43-46):"))
    if ice==43:
       ri="Vanilla"
       ri1= '60'
    elif ice==44:
       ri="Strawberry"
       ri1= '60'
    elif ice==45:
       ri="Pineapple"
       ri1= '60'
    elif ice==46:
       ri="Butter scotch"
       ri1= '60'
    bill="select Item_name, Item_price from resitems where item_no in(%s,%s,%s,%s,%s,%s,%s)"
    billitem=(bevarages,soups,maincourse,roti,rice,south,ice)
    cursor.execute(bill,billitem)
    dat=cursor.fetchall()
    print("	!!Your Order!!	")
    print(name)
    print("Item Name,Item rice")
    for i in dat:
       print(i)
       s+=i[1]
    print("\nTotal Cost :-",s,"/--")
    print("G.S.T  :-",s*(18/100),"/--")
    print("C.S.T :-",s*(18/100),"/--")
    s1=s+(s*(18/100))+(s*(18/100))
    print("Total Amount To Be Paid:-",s1,"/--")
    resbi="INSERT INTO Resbill VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    resdat=(name,None,rb+ rb1,rs+	rs1,rm+	rm1,ro+	ro1,rc+	rc1,ru+ru1,ri+	ri1,s1)
    cursor.execute(resbi,resdat)
    mys.commit()
    print("	Pleses Pay Before You leave	")
    print("	")    

############Restaurant Details:#################
def restaurant():
    #resitems()
       print("\n============================================================================")
       print("============================RESTAURANT====================================")
       print("==============================================================================")
       print("	                                  -:MENU:-	                            ")
       print("---------------------------------------------------------------------------------------")
       print("\n BEVARAGES	                                26 Dal Fry	140.00")
       print("----------------------------------	                27 Dal Makhani	150.00")
       print(" 1 Regular Tea.....................   20.00	28 Dal Tadka	150.00")
       print(" 2 Masala Tea......................   25.00")
       print(" 3  Coffee............................   25.00	ROTI")
       print(" 4  Cold Drink.....................    25.00        -----------------------------------  ")
       print(" 5  Bread Butter.....................30.00	29 Plain Roti	15.00")
       print(" 6  Bread Jam........................ 30.00	30 Butter Roti	15.00")
       print(" 7  Veg. Sandwich.................  50.00	31 Tandoori Roti	20.00")
       print(" 8  Veg. Toast Sandwich........50.00	32 Butter Naan	20.00")
       print(" 9  Cheese Toast Sandwich   70.00")
       print(" 10 Grilled Sandwich.............  70.00	RICE")
       print("	                                              -----------------------------------")
       print(" SOUPS	                                                33 Plain Rice	90.00")
       print("----------------------------------	                34 Jeera Rice	90.00")
       print(" 11 Tomato Soup.............. 110.00	35 Veg Pulao	110.00")
       print(" 12 Hot & Sour.................. 110.00	36 Peas Pulao	110.00")
       print(" 13 Veg. Noodle Soup	110.00")
       print(" 14 Sweet Corn................. 110.00	SOUTH INDIAN")
       print(" 15 Veg. Munchow............ 110.00              -----------------------------------")
       print("	                                                37 Plain Dosa	100.00")
       print(" MAIN COURSE	                                38 Onion Dosa	110.00")
       print("----------------------------------	                39 Masala Dosa	130.00")
       print(" 16 Shahi Paneer.............. 110.00	40 Paneer Dosa	130.00")
       print(" 17 Kadai Paneer.............. 110.00	41 Rice Idli	130.00")
       print(" 18 Handi Paneer.............. 120.00	42 Sambhar Vada	140.00")
       print(" 19 Palak Paneer	        120.00")
       print(" 20 Chilli Paneer............... 140.00	ICE CREAM")
       print(" 21 Matar Mushroom......... 140.00           -----------------------------------")
       print(" 22 Mix Veg....................... 140.00	43 Vanilla	                60.00")
       print(" 23 Jeera Aloo................... 140.00	44 Strawberry	60.00")
       print(" 24 Malai Kofta.................. 140.00	45 Pineapple	60.00")
       print(" 25 Aloo Matar................... 140.00	46 Butter Scotch	60.00")
       print("\nWhat Would You Like To Take	")
       resbill()

 ###########Hotel Details###############
       
def hotel():
    while True:
        print("\n1.Rooms & Suites")
        print("2.Restaurant")
        print("3.Booking Details")
        print("4.Cancel Your Booking")
        print("5.Exit")
        a=int(input("Enter your choice:-"))
        if a==1:
            rooms()
            break
        elif a==2:
            restaurant()
        elif a==3:
            bookinginfo()
        elif a==4:
            cancelbooking()
        elif a==5:
            print("Thank you For Visiting Us".center(165))
            print(" Welcome Again ".center(165))
            print("*****************************!Exiting!****************************************")
            break
        else:
            print('''xxxxxxxxxxxxxxx!! Invalid Entry !!xxxxxxxxxxxxxxx Please Try Again''')
            hotel() ###########################################
            hotel()
