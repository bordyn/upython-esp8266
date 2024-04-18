# create a list of number
list_number = [i for i in range(0,200)]

# save it to a file
with open('list_number.txt','w') as num_f:
    for num in list_number:
        num_f.write(str(num)+',')

# modify some thing on a file
with open('list_number.txt','a') as num_f:
    num_f.write(str(2020))

# simply read something on a file
with open('list_number.txt','r') as num_f:
    list_number_read = num_f.read()
print (list_number_read)


