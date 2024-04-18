import time

# delay for 5 seconds
print ("start time")
for i in range(0,5):
    time.sleep(1)
    print ('count is ',i+1)
print ("end time")

# try other delay for 1 seconds
time.sleep_ms(1000)
time.sleep_us(1000000)

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

# measure file creation time
start = time.ticks_ms()
file_name = create_example_file()
end = time.ticks_ms()
print ('creating',file_name,'take ',end - start, 'milli seconds')

# measure file creation time again
start = time.ticks_ms()
file_name = create_example_file(record_len=500)
end = time.ticks_ms()
print ('creating',file_name,'take ',end - start, 'milli seconds')

