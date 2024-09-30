# FUNCTIONS IN PYHTON
# block of code that performs a specific task whenever it is called.
# build in --> min(),max(),len(),sum(),type(),range(), dict(), list(),tuple(),set(),print(),etc.
# user defined function --v
def function_name(parameter):    #syntax
    pass  
def add(a=2,b=3):             #example
    return a+b
obj = add()
print(obj)
obj =add(1,2)
print(obj)

#LIST --> Ordered collection of multiple types of data items.|| enclosed in [] ||seperated by ",".
lst = [1,2,3.4,"data",True,5,7,9]
#indexing --> list[stat, end, jump]
print(lst[0:-1:2])
#list comprehension --> list = [expression (item) for item in iterable if condition]
ls = [x for x in range(20) if x%2 ==0]
print(ls)

# Basic Operations on list data type
ls.append(3)       #added at last
print(ls)
print(ls.sort())
print(ls.sort(reverse= True))
print(ls.reverse())
print(ls.index(3))
print(ls.count(2))
print(ls.insert(-1,20,54))   #added at start
ls.extend(lst)
print(ls)
print(ls+lst)


#Tuples --> ordered collection of data || store multiple data items || immutable || items are seperated by commas


