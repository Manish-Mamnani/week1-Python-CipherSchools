#checking two conditions at the same time
name = "abc"
age = 19
if name=="abc" and age==19:
    print("condition true")
else:
    print("condition false")
#################################
name = "abc"
age = 19
if name=="abc" and age==18:
    print("condition true")
else:
    print("condition false")
#or operator
name = "abc"
age = 19
if name=="abc" or age==19:
    print("condition true")
else:
    print("condition false")
#####################################
name = "abc"
age = 19
if name=="abc" or age==18:
    print("condition true")
else:
    print("condition false")
#####################################
name = "abc"
age = 19
if name=="abcd" or age==18:
    print("condition true")
else:
    print("condition false")