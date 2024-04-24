import time

# 1. using time.sleep to delay the lopp that keeps on printing the counter
# the delay value is 5 seconds

# time tick used for capturing ms count
print (time.ticks_ms())
time.sleep_ms(1200)
print (time.ticks_ms())

# a function for creating series of number in a file
def create_example_file(file_name='list_number.txt',record_len=200):
    # create a file in file system
    list_number = [i for i in range(0,record_len)]
    with open(file_name,'w') as num_f:
        for num in list_number:
            num_f.write(str(num)+',')
    return  file_name

# 2. using the time.ticks_ms() to capture lapse time calling 
# create_example_file with different record_len


