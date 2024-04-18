# basic for
for i in range(0,10):
    print (i)

# python comprehension
x_list = [i for i in range(0,10)]
print (x_list)

# iterate through dictionary
b = {"name":"student_a","score":3.0}
for name,score in b.items():
    print (name,score)

# iterate through list
num = [1,2,3,4,5]
for n in num:
    print (n)

# break statement
for n in num:
    if n == 4:
        break
    print (n)

# else statement for 'for'
for n in num:
    if n == 6:
        print ('6 found')
        break
else:
    print ('6 not found')

# continue statement for 'for'
odd_num_list = []
for n in num:
    if n % 2 == 0:
        continue
    odd_num_list.append(n)
print (odd_num_list)

# loop can be nested
all_comb = []
for n1 in num:
    for n2 in num:
        all_comb.append((n1,n2))
print (all_comb)
        
        
        