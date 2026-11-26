#thoda decoration ye lie ye krte hai ..

print("*" * 40)
print("        SMART RENT CALCULATOR")
print("*" * 40)
#user say input lenge 
rent = int(input("enter your house rent:"))
electricity = float(input("Enter your electricity bill:"))
water = float(input("enter your water bill:"))
maintenance = float(input("enter your maintenance charges:"))
person = int(input("how many person you are :"))
#add all expense
total = (rent+electricity+water+maintenance)
#valdiate the number of person
if person <= 0:
    print("\nError::: number of person must be greater than zero")
else:
    #calculation per person expense
    per_person = (total/person)
    #its time to show result to user
    print("\n" + "*" *40)
    print("             monthly rent report")
    print("\n" + "*" *40)
    print(f"house rent:{rent:2f}")
    print(f"electricity bill :{electricity:2f}")
    print(f"water bill:{water:2f}")
    print(f"maintance bill:{maintenance}")
    print("-" *40)
    print(f"total monthly expense:{total}")
    print(f"Per person bill:{per_person}")
    print("-" *40)
    print("-" *40)
    print("         THANK YOU")
    print("-" *40)


