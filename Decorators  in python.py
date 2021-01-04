# Decorators 

# decorators are used to add some behavior to existing callable (functions, methods, and classes).
# Additional behavior is achieved by wrapping   existing callable inside another function which adds some functionality to it
# In general, a callable is something that can be called, It is the built in function in python 


# Now we will  write some pyhton code to Measuring Execution Time  with the help of decorators.

# to calculate the decorator


def timer(fn):                                                                    # function 
    from time import perf_counter
    def inner(*args, **kwargs):                                                   # “We use *args and **kwargs as an argument when we have no doubt
                                                                                  # about the number of arguments we should pass in a function.”
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:8f} to execute'.format(fn.__name__, execution_time))
        return to_execute
    
    return inner






@timer
def function_1():
    for i in range(100000):
        pass
    
@timer
def function_2():
    for i in range(100000):
        pass
    
@timer
def function_3():
    for i in range(100000):
        pass
    
@timer
def function_4():
    for i in range(100000):
        pass



function_1()
function_2()
function_3()
function_4()

