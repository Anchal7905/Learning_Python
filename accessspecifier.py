# access specifiers in python just a convention used by programmers 
#access mpdifier used to limit the access of class variable and class methods outside of class while implementing the concept of inheritance
# by default public, private bahar se access ni kiye ja sakte, protected class ke andar se access kiye ja sakte hai aur sub class se access 
# kiye ja sakte hai(child class)
class employee:
    def __init__(self) -> None:
        self.name = "Harry"      #public access modifier

a = employee()
print(a.name)
 
# private -- if we use double underscore prefix for some variable  (weak internal use indicator)
class emp:
    def __init__(self) -> None:
        self.__name = "Harry 2"

obj = emp()
# print(obj.__name)   shows error but can be accessed
print(obj._emp__name)    # can be accessed like this (name mangling)single leading underscore and then double leading underscore

print(obj.__dir__())


# protected - accessed only by class itself and by its sub classes(varible name followed by single underscore)

class student:
    def __init__(self) -> None:
        self._name  =  "Anchal"

    def _funName(self):         #protected method
        return "Program with me "

class subject(student):
    pass
obj1 = student()
obj2 = subject()
print(obj1._name)
print(obj1._funName())

print(obj2._name)
print(obj2._funName())



# static method     does not recieve an argument when any instance is called or not by any object
class Employee:
    def __init__(self, name) -> None:
        self.name = name
        
    def showDetails(self):
        print(f"the name of the employee is {self.name}")

    @staticmethod
    def add(a,b):
        return print("sum is ",a+b)
obj1 = Employee("Anushka")
Employee.add(4,5)
obj1.showDetails()


# class variable and instance variable concept
