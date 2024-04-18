def func_1(args):
    return args

# basic functions
print (func_1('test'))

# pass by reference
def  func_2(args):
    args = [4,5,6]
    print (args)
a = [1,2,3]
func_2(a)
print(a)

# pass by reference 2
def  func_3(args):
    args.append(4)
    print (args)
a = [1,2,3]
func_3(a)
print(a)

# multiple arguments
def  func_4(args1,args2):
    return args1 + args2
a = [1,2,3]
b = [4,5,6]
print (func_4(a,b))

# default argument 
def  func_5(a,b=5):
    return  a*2 + b
a = 10
print (func_5(a))
print (func_5(a,10))

# keyword argument
def  func_6(a,b):
    return  a*2 + b
print (func_6(a=10,b=5))
print (func_6(b=5,a=10))

# variable length dictionary style
def  func_7(**kwargs):
    a = kwargs.get('a',0)
    b = kwargs.get('b',0)
    return  a*2 + b

args_dict = {'a':10,'b':5 }
print (func_7(**args_dict))


    