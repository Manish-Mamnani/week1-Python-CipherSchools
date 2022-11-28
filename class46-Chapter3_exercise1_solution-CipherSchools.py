winning_number = 777
a = int(input("enter any number between 100-999: "))
if a==winning_number:
    print("YOU WIN !!!!")
elif a < winning_number:
    print("too low")
elif a > winning_number:
    print("too high")
#by nested if-else
# winning_number = 777
# a = int(input("enter any number between 100-999: "))
# if a==winning_number:
#     print("YOU WIN !!!!")
# else:
#     if a < winning_number:
#         print("too low")
#     else:
#         print("too high")