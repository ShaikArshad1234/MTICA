message='global scope'
def outer():
    
    print(message)
    def inner():
        nonlocal message
        message='inner scope'
        print(message)
    inner()
    print(message)
outer()
