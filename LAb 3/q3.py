#function_name.__code__.co_nlocals


def function1():
    pass

def function2():
    a=1

def function3(a):
    b=2
    return a+b


print("The number of local variable in function1 = ", function1.__code__.co_nlocals)
print("The number of local variable in function2 = ", function2.__code__.co_nlocals)
print("The number of local variable in function3 = ", function3.__code__.co_nlocals) 
