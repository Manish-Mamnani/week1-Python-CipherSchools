#show ticket pricing
#1 to 3 (Free)
#4 to 10(150)
#11 to 60(250)
#above 60(200)

age = int(input("enter your age: "))
if age==0 or age<0:
    print("you cannot watch")
elif 0<age<=3:
    print("Ticket price : Free")
elif 4<=age<=10:
    print("Ticket price : 150")
elif 11<=age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")