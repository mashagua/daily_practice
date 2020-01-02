# def func(message):
#     print('Got a message:{}'.format(message))
# send_message=func
# send_message('hello world')
#part2 make function as parameters
# def func(message):
#     return 'Got a message:{}'.format(message)
# def root_call(func,message):
#     print(func(message))
#
# root_call(func,'hello world')
#part3 functions
# def func_closure():
#     def get_message(message):
#         print('Got a message:{}'.format(message))
#     return get_message
#
# send_message=func_closure()
# send_message('hello world')
#

# def my_decorator(func):
#     def wrapper():
#         print('wrapper of decorator')
#         func()
#     return wrapper
#
# @my_decorator
# def greet():
#     print('hello world')
#
# greet()
#decorator with parameters
# def my_decorator(func):
#     def wrapper(messae):
#         print('wrapper of decorator')
#         func(messae)
#     return wrapper
#
# @my_decorator
# def greet(message):
#     print(message)
#
# greet('hello world')
# # decorator with many parameters
# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('wrapper of decorator')
#         func(*args,**kwargs)
#     return wrapper
# with parameters of my own
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator
@repeat(4)
def greet(message):
    print(message)

greet('hello world')
#保持原来的
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('wrapper of decorator')
        func(*args,**kwargs)
    return wrapper


