Data types
- Integers - int - Whole numbers
- Floating point - float - numbers with a decimal point
- Strings - str - Ordered sequence of characters
Data Structures - it can hold some object in some sort of sequence or mapping
- Lists - list - Ordered sequence of objects: [10,"sachin"]
- Dictionaries - Unordered Key:Value pairs: {"":"","":""}
- Tuples - tup - Ordered immutable sequence of objects: ("",10,"")
- Sets - set - Unordered collection of unique objects: {"a","b"}
- Booleans - bool - Logical value indicating True or False

===================================================================================

Numbers
- operations: +,-,/,*,%,**

- Python uses Dynamic Typing - you can reassign variables to different data types
- type() checks type of a variable

===================================================================================

Strings
String are ordered sequence ad immutable
- indexing/reverse-indexing - [1]/[-1]
- slicing - grabs a subsection of multiple characters - [start:stop:step] - [::-1] to reverse a string
- escape sequence - https://docs.python.org/3/reference/lexical_analysis.html#strings
- len() - check length of a string
- Stirng concatenation + / String multiplication *
- Builtin String methods - https://www.w3schools.com/python/python_ref_string.asp
- String formatting/interpolation
    - .format() 
        - print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
        - float formatting "{value:width:precision f}" - print('{r:.3f}'.format(r=10.3232324))
    - f-string() string result
        - print(f'Hello {'hello'}')

===================================================================================

List

- list = ['one','two']
- we can concatenate two list
- we can change the items in a list
- .append() - add any item to end of the list
- .pop() - remove the last item in list or pass the index posistion with .pop() method
- .sort() - sort the list in place

===================================================================================

Dictionaries

- my_dict = {'key1':'value1', 'key2':'value2'}
- dict can hold list or another dict
- we can rewrite and add new key:value pair
- .keys() & .values() & .items() common builtin methods on Dictionaries

===================================================================================

Tuples
 
- t = ('one',2,'three')
- .index() - get the index of the value

===================================================================================

Sets

- myset = set()
- .add()
- mylist = [1,2,3,4,4,3,5] - set(mylist) - gives {1,2,3,4,5}
- set not necessary returns ordered items

===================================================================================

Booleans

True & False - to deal with logical codes

===================================================================================

we can use None as a placeholder to initilize a variable - a = None

===================================================================================

I/O with basic files in python

- open a file - myfile = open('file.txt')
- read the file - myfile.read()
- to read the file again we have to bring the cursor again abck to top - myfile.seek(0)
- to read each line as a seperate object in a list - myfile.readlines()
- for windows filepath "C:\\users\\username" - for linux "/Users/UserName"
- to close the file myfile.close()
- we can open file as
    - with open('file.txt') as my_new_file: (using this method we dont need to woory to close the file each time we open)
- Reading, Writing, Appending modules
    - mode='r'/'w'/'a'/'r+'/'w+' - example - with open('file.txt',mode='a') as my_new_file:
     




