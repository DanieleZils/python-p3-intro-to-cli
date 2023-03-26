#!/usr/bin/env python3

class MyClass:
    def __init__(self, user_input):
        self.value = user_input

def my_function(my_object):
    # returns a final value for the CLI workflow

 if __name__ == '__main__':
    user_input = input("Enter something here: ")
    my_object = MyClass(user_input)
    print(my_function(my_object))
 