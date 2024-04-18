a = {"name":"student a","age":20,"score":3.0}

# simply print a name in member
print (a["name"],a["age"],a["score"])
print (type(a))

# what if we access to something does not exist
#print (a['class'])

# we can add class one the fly
a['class'] = 'class_1'
print (a)

# accessing element in dict
a['score'] = 4.0
print (a)

# accessing all keys
print (a.keys())

# accessing all values
print (a.values())

# creating key,value list
print (a.items())

# removing an element using key
del a["name"]
print (a)
a["name"] = "student_a"

# another way getting without exception
print (a.get("name","No name"))
