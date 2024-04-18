# basic while
count = 0
while count < 5:
   print ('Count is:', count)
   count = count + 1

# while can use break also
x = [1,2,3,4,5,6,7,8,9,10] #1-10
count = 0
while count < len(x):
    if x[count] >= 5:
        break
    print ('item ',x[count],' is less than 5')
    count = count + 1

# while can be used as infinite loop
count = 0
while True:
    print (count)
    count = count + 1
    