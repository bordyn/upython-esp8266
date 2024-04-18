import os

def create_example_file(file_name='list_number.txt'):
    # create a file in file system
    list_number = [i for i in range(0,200)]
    with open(file_name,'w') as num_f:
        for num in list_number:
            num_f.write(str(num)+',')
    return  file_name

def show_all_files_in_directory(directory):
    dir_list = [f for f in os.listdir(directory)]
    return dir_list

def show_only_files_in_directory(directory):
    dir_list = [f[0] for f in os.ilistdir(directory) if f[1] == 0x8000]
    return dir_list

def show_only_dirs_in_directory(directory):
    dir_list = [f[0] for f in os.ilistdir(directory) if f[1] == 0x4000]
    return dir_list

# get current working directory
print (os.getcwd())

# create an example directory
os.mkdir('example')
print (show_only_files_in_directory(os.getcwd()))
print (show_only_dirs_in_directory(os.getcwd()))
os.rmdir('example')

# create an example file
file_name = create_example_file()
print (show_only_files_in_directory(os.getcwd()))

# delete an example file
os.remove(file_name)
print (show_only_files_in_directory(os.getcwd()))


