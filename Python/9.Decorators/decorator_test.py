def new_decorator(original_func):

    def wrapped_func():
        print("wrapper")
        original_func()
        print("wrapper")

    return wrapped_func

'''
def func_needs_decorator():
    print("gift")

decorator_func(func_needs_decorator)
'''

@new_decorator
def func_needs_decorator():
    print("gift")

func_needs_decorator()