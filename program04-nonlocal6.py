
def outer():
    message='global scope'
    print(message)
    def inner():
        nonlocal message
        message='inner scope'
        print('inner:',message)
    inner()
    print('outer:',message)
outer()
