Control flow

- to control flow of logic we use special keywords
    - if, elif,else
- control flow syntax makes use of colons and indentations
-   if condition:
        # execution code
    elif condition:
        # execution code
    else:
        # execution code

===================================================================================

For loop

- for iterable_item in iterable_list:
    # execution code

- To iterate through an iterable_list where we do not need to use the iterable_item we can use iterable_item
    for _ in iterable_list:
        # execution code

- Tuple unpacking
    mylist = [(1,2),(2,3),(3,4)]
    for a,b in mylist:
        print(a)
        print(b)

- Iterate through the dictionaries - bydefault iterating through dict only gives key
    d = {'k1':1,'k2':2}
    for key,value in d.items():
        print(key)
        print(value)

===================================================================================

While loop

- while:
    #do something

===================================================================================

break

continue

pass - put it as a place holder in function or loops if we do not intend to do anythingwith the loop

===================================================================================

Useful Operators

- range(start,stop,step) - can be used for iteration
    - for num innnnnge(0,11,2):
        print(num)

- enumerate() - can be used to enumerate a iterable object - by default enumerate generates a tuple containing - (index,item)
    - word = 'abcde'
    for index,letter in enumerate(word):
    print(index)
    print(letter)

- zip(list1,listn) - can be used to zip together multiple list
    -   mylist1 = [1,2,3,4]
        mylist2 = ['a','b','c','d']
        for item in zip(mylist1,mylist2):
            print(item)
    -   list(zip(mylist1,mylist2))

- in operator - to check if something is in a list
    - 'a' in 'a world'

- min()

- max()

-random
    - shuffle - inplace shuffle a list
    - randint - picks a random integer from a list

- input() - takes input from the user - bydefault takes everything as a string
    casting - int(input('input a number: '))

- list comprehensions - quickly create a list with python
    - mylist = [letter for letter in mystring]
    - mylist = [num**2 for num in range(0,11)]
    - mylist = [num for num in range(0,11) if x%2==0]  if
    - fahrenehit = [((9/5)*temp +32) for temp in celcius_list]
    - even = [x if x%3 == 0 else 'ODD' for x in range(0,11)] - if else
    - mylist = [x*y for x in [2,3,4] for y in [5,6,7]]
    - mylist = [x*y for x, y in zip([2,3,4],[5,6,7])] - nested for loop









