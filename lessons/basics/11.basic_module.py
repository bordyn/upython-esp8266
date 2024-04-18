import quad

# this equals to x**2 + x + 1 ,where x = 2
print (quad.quardratic_fn(1,1,1,2))

from quad import quardratic_fn

# this equals to x**2 + x + 1 ,where x = 2
print (quardratic_fn(1,1,1,2))

from quad import quardratic_fn as q2

# this equals to x**2 + x + 1 ,where x = 2
print (q2(1,1,1,2))
