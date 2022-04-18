#Is a python function that add functionality to an existing function in python without changing the structure

def dec_function(p):
    def inner():
        print("before")
        p()
        print("after")
    return inner
        
def dec_table(p):
    """This is decorater function"""
    def inner():
        fn = p()
        l = [i*fn for i in range(1,11)]
        return l
    return inner

@dec_table
def p():
    print("Hellow")
    return 2

# p = dec_function(p)   #no need to do this when is use @func_name of the top of function
# p()
print(p())


