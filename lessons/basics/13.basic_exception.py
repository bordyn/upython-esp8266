# create a list of number
list_number = [11,87,53,0,42,22,18]

# simply try this
x = 50
div_result = []
#for num in list_number:
#    print (x/num)
#    div_result.append(x/num)

# try again
for num in list_number:
    try:
        res = x/num
        div_result.append(x/num)
    except:
        div_result.append('N/A')
print (div_result)

# if user wants to see something happend
div_result = []
log_str = ""
for num in list_number:
    try:
        res = x/num
        div_result.append(x/num)
    except Exception as e:
        div_result.append('N/A')
        log_str += str(e)
print (div_result)
print (log_str)
        