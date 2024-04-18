a = "Hello I'm a Bascii student"
b = 'for so long'

print (a)
print (b)

# string can be added (concatenated)
c = a + b
print (c)

# simple way to combine string and integer
c = a + ' on ' + str(1)
print (c)

# unsupported string subtraction
#c = a - b
#print (c)

# a way to subtract some element from string
d = "I'm a "
c = a.replace(d,'')
print (c)

# find an index of character in a string
d = 'a'
print (a.index(d))

# some character in a string?
print ('Z' in a)
print ('I' in a)