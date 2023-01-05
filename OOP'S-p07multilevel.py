class A:     # Inheritance from more than one base class
    def first_method(self):
        print("Method of class A...")
class B:
    def first_method(self):
        print("Method of class B...")
class C(A,B): #multilevel inheritance
    def third_method(self):
        print("Method of class C...")
if __name__=='__main__':
    ob=C()
    ob.first_method()
    C().third_method()
