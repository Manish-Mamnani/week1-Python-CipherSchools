#center method
name = "Manish"
# **Manish**
print(name.center(8, "*"))
print(name.center(7, "*"))
print(name.center(10, "*"))

name = input("enter your name: ")
l = len(name)
print(name.center(l+8, "*"))