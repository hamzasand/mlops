# from functools import wraps
# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello from decorators class from chaicode")


# greet()
# print(greet.__name__)

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Befor the main function excution")
        func()
        print("After the excution of main function")
    return wrapper

@my_decorator
def greet():
    print("hello my name is Hamza")

greet()