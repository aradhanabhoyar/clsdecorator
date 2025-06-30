## using class method and static method ##
#def pro(func):
#    def wrapper(*arg,**kwarg):
#        print(f"Calling {func.__name__}")
#        return func(*arg,**kwarg)
#    return wrapper

#class my_class:
#    @staticmethod
#    @pro
#    def show():
#        print("This is static method")

#    @classmethod
#    @pro
#    def display(cls):
#        print("This is class method")

#my_class.show()
#my_class.display()

##Creating decorator inside class##
#class myclass:
#    def deco(func):
#        def wrapper(*arg,**kwarg):
#            print("Inside the class deco")
#            return func(*arg,**kwarg)
#        return wrapper
#    @deco
#    def say_hello(self):
#        print("Hello!")

#s = myclass()
#s.say_hello()

##using a class as a decorator ##
class decorator:
    def __init__(self,name):
        self.name =name
    
    def __call__(self,*arg,**kwarg):
        print("Before name runs ------")
        result = self.name(*arg,**kwarg)
        print("After name runs ------")
        return result
    
@decorator
def Name(name):
        print(f"Hello, {name}!")

Name("Aradhana")