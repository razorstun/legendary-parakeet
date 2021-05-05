Find Methods $ Builtin objects

- to get the documentaion on the objects - help(str.index)
- python standard library - https://docs.python.org/3/library/

===================================================================================

Functions

- def keyword to declare a Functions   
    - def name_of_function(): //function name as snake casing as a conventions

- Tuple unpacking in function   
    A , B = function_name(args) - this function returns a tuple with two value

- *args and **kwargs
    - *args - allows us to take n number of arbitariry arguments in a function - returns back a tuple
        - def mufunc(*args):
            return sum(args) * 0.05
    - **kwargs - returns back a dictionary
        - def myfunc(**kwargs):
            print(kwargs)
    - def myfunc(*args,**kwargs):
        print('I would likk {} {}'.format(args[0],kwargs['food']))
    myfunc(10,20,30,fruit='orange',food='eggs',animal='dogs')

===================================================================================

Lambda expressions - quickly create ananymous function that will be used only one time
    - map(function_name, iteratable_items)
        - you get the list(map(function_name, iteratable_items))
    - filter(function_name, iteratable_items)
        - filter take a function that returns a bool and filter the items based on the bool value
    - lambda expressions - also known as ananymous function
        - lambda args: statements
    - lambda expression can be used in conjuction with map to reduce the code
        - list(map(lambda num: num**2, mynums))

===================================================================================

Nested statements and scope

    - LEGB Rule - order python look for variables
        - local
        - Enclosing function
        - Global
        - Built-in
    - we can use global to change reassign the value of global variable by calling global variablename





















































