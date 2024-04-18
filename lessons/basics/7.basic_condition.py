# compare basic variable
a = 100
if a == 100:
    print ('a is really 100')
else:
    print ('a is not 100')

# compare some string
x = "Joe"
if x == "Joe":
    print ("Correct")
else:
    print ("Incorrect")

# check if a member is in list
b = [4,5,6,7]
if 4 in b:
    print ('b contains 4')
else:
    print ('b does not contain 4')

# multiple if.
b = {"name":"student_a","score":3.0}
if "name" in b.keys():
    if "student_a" in b.values():
        print ("student_a is in the record")
    else:
        print ("student_a is not in the record")
else:
    print ("invalid record")
    