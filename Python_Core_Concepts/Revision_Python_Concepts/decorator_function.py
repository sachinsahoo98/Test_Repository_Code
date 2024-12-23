
def greetname(func):
    def wrapper(*args, **kwargs):
        print("Inside function call")
        func(*args, **kwargs)
        print("Outside function call")
    return wrapper

@greetname # greet = greetname (greet)
def greet():
    print("Hello")

greet()