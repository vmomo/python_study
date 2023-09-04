def func():
    return 1

def gen():
    yield 1

print(type(func))   # <class 'function'>
print(type(gen))    # <class 'function'>

print(type(func())) # <class 'int'>
print(type(gen()))  # <class 'generator'>
