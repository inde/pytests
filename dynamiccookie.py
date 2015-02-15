# Python
 
class A(object):
 
    def __init__(self, a):
        self.a = a
 
    def square(self):
        return self.a * self.a
 
a = A(10) # creating an instance
print(a.a) # 10
 
A.b = 20 # new property of the class
print(a.b) # 20 – available via "delegation" for the "a" instance
 
a.b = 30 # own property created
print(a.b) # 30
 
del a.b # removed own property
print(a.b) # 20 - again is taken from the class (prototype)
 
# just like in prototype based model
# it is possible to change "prototype"
# of an object at runtime
 
class B(object): # "empty" class B
    pass
 
b = B() # an instance of the class B
 
b.__class__ = A # changing class (prototype) dynamically
 
b.a = 10 # create new property
print(b.square()) # 100 - method of the class A is available
 
# we can delete explicit references on classes
del A
del B
 
# but the object still have implicit
# reference and the methods are still available
print(b.square()) # 100
 
# but, to change the class on some of build-in
# is impossible (in current version) and this is the
# feature of implementation
b.__class__ = dict # error