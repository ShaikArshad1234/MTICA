def demo_yield():
    print("coed segment1 executed")
    x=7
    yield x*x
    print("code segment2 executed")
    yield 2
    print("code segment3 executed")
    yield 4
    print("code segment4 executed")


if __name__=="__main__":
    x=demo_yield()
    print(next(x))
    print(next(x))
    print(next(x))
