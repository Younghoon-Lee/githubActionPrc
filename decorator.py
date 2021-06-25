def decorator2(func):
    def wrapper2(*args,**kwargs):
        print(f'{func.__name__} has been decorated again by decorator2')
        return func(*args,**kwargs)
    return wrapper2

def decorator1(func):
    def wrapper1(*args,**kwargs):
        print(f"{func.__name__} has been decorated by decorator1")
        return func(*args,*kwargs)
    return wrapper1

@decorator2
@decorator1
def function():
    print('This is original function')


print(function.__closure__[0].cell_contents.__closure__[0].cell_contents.__closure__)
