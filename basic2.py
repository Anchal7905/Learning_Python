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
#REPRESENTATION
check_list = [
(1,2,4,'green') ,
(2) ,
1, 
]
for data in check_list:
    print(f'{data} is : ',type({data}))   # SHOWS SET

a = (1,2,4,'green') 
print(type(a))        #SHOWS TUPLE (even being same data as written in list)

#Manupulating tuples --> for any change, first convert it into list and then conert to tuple after changes are done.
countries = ("Spain","Italy","India","England", "Germany")
print(countries)
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
temp = tuple(temp)
countries = temp
print(countries)


# methods that will work on tuple such as count, index, etc.


#NOTE :- f  - string is also known as literal string interpolation || focus to make the interpolation easier.

# SET --> unordered collection of similar data items|| enclosed in {}||unchangeable|| do't contain duplicate values

a = set() # empty set
info = {'carla', False, 12, 5.9,12}
print(info)
for i in info :  # accessing information
    print(i)
#SET METHODS --> UNION, INTERSECTION, DIFFERENCE, DISJOINT
set1 = {1,2,5,6}
set2 = {3,6,7}
print(set1.union(set2))   #RETURN NEW SET
print( set1, set2)
set1.update(set2)      #update existing set
print(set1, set2)

print(set1.intersection_update(set2))     #update in existing
print(set1.intersection(set2))    #returns a new set

a = {1,2,3,4,5}
b = {1,3}
print(a.symmetric_difference(b))       #returns difference
print(a,b)
a.symmetric_difference_update(b)           #update in itself
print(a.difference(b))
print(a.isdisjoint(b))          #a n b = 0
'''similarly we can use others such as issuperset(), issubset()
add()--> to add single item
update()--> to add multiple items at a time
pop()--> removes the last element
del()--> delete the set entirely
clear()--> empty the entire set'''
table = {1,2,3,4}
a.remove(0)
print(a)
# a.remove(5)      shows error
a.discard(5)       #return NONE  (benifit of using discard in place of remove method)



#DICTIONARY
dict = {'Anchal':'Student', "course":'B.tech',"id": 31}
print(dict["Anchal"])
print(dict.get("Anchal"))
print(dict.get("stream"))       #return NONE
# print(dict["stream"])    gives error
print(dict.keys)
print(dict.values)
print(dict.items())               #accessing key value pair
dict1 = {"stream": "CSE", "lanuage": "Python"}
dict.update(dict1)
print(dict)
dict.pop("course")   #removes the passed key value pair
print(dict)
dict.popitem() #removes the last key value pair
print(dict)
del(dict["id"])   #also used to remove items,  **if key is not given then del method will delete the entire dictionary
print(dict)
dict.clear()      #removes all the item from the list
print(dict)



# THIS FILE INCLUDES FUNCTIONS, LIST, TUPLE, SET AND DICTIONARY AND SOME OF THEIR COMMON METHODS
