OOPs

- OOP allows programmers to create their own objects that have methods and attributes
- OOP allows us to create code that is repatable and organized
- class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(seld.param1)

===================================================================================

Attributes and class keywords

- __init__ is like a constructore and called whenever you create an instance of a class
- self keyword reprsents the instance of the object itself

===================================================================================

Class objects attributes & methods

- Class objects are the Attributes that are same for any instance of the class
- Class objects are defined before the constructor
- methods are essentially functions defined inside the body of the class and they are used to perform operations that sometimes used the attributes of the object
- methods are basically functions defined inside of a class and work with the object of the class someway

===================================================================================

Inheritance and Polymorphism

- Inheritance is basically for new classes used classes that are already been defined
- deriving attributes and methods from base class
    - class Derived_class_name(Base_class):
        def __init__(self):
            Base_class.__init__(self)

    - overwriting methods from old class
        - def Base_class_method_name(self):
            logic
- functions can take in different arguments methods belongs to the object they act on
- Polymorphism refers to the way in which different object classes share the same method name and those methods can be called from the same place even though a variety of differnt objects might be passedin
- Abstract classes and Inheritance
    - abstract classes are the classes that never expects to create the instance of the class but they only serve as the base class
    - abstract methods are the methods that are declared but do not contain any implementation

===================================================================================

Special Methods - allows to use some built-in methods in python with our own created object

- __init__ is the special method
- __str__
- __len__
- __del__

