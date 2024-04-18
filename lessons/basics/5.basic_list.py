a = ["car","bike","plane"]
b = [1,2,3.1,4.1]

# simply print a list
print (a)
print (type(a),type(b))

# referring to a variable in list
print (a[0],b[0])
print (a[2],b[2])

# can not exceed length
#print (a[3])

# find the list length
print (len(a))

# adding element in a list
a.append("rocket")
print (a)

# removing and element from a list
a.remove("car")
print (a)

# insert item into any position
a.insert(0,"car")
print (a)

# list can be added (concatenated) with different type
c = a + b
print (c)

# this will be instead be a member of a
a.append(b)
print (a)
print (a[-1])
# let's remove it
a.remove(b)
print (a)

# check if an element qualify something
vehicle_contain_c_character = [v for v in a if 'c' in v]
print (vehicle_contain_c_character)
score_greater_than_3 = [s for s in b if s > 3]
print (score_greater_than_3)


