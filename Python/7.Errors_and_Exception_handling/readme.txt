Error handling

- we can use error handling as an approach to handle in our code
- keywords - try, except, finally - block of code to be executed, regardless of an error
-   try:
    except:
    else:
-   try:
        f= open('testfile','r')
    except TypeError:
        print("There was a type error")
    except OSError:
        print("Hey you have an OS error")
    finally:
        print("I always run")

===================================================================================

Unit Testing

pylink - this is a library that looks at your code and reports back possible issues
unittest - this build-in library will allow to test your won programs and check you are getting desired outputs

===================================================================================

