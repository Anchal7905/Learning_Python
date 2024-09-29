# To print a Statement
print("this is a statement")
a = 4
b = 2
print("addition",a+b)
print("Subtraction",a-b)
print("Multiply",a*b)
print("Division",a/b)
print("double division",a//b)
print("Modulous",a%b)
print("Hello",1,1,sep="--")   # use of seperator
print("Hello",1,1,sep="--",end="009\n")  #use of end keyword


# comments in python
print("use # for single line comment ")
#this is a single line comment 
print("use '''....''' for multiline comments")
'''
hii
this is multiline comment
i can write more than one line in a comment section..'''

# escape sequence character
#  \" -> to use " in statement
#  \n -> to change line


# DATA TYPES IN PYTHON
# str, int, float, bool, list, tuple, dict, set complex
ls = [1 ,1.1, "data", "1", True, complex(8,2), [4,5],("one",1,1), {"1: one","2:two"}]
for data in ls:
    print(data,type(data))

# taking user input
print("user input always returns in string data-type")
user = input("text user input")
print(user)
print(eval(input("enter equation to solve")))

# operations on string
name = "!!Anaconda!!"
print("hello python "+ name )   #concatanation
print(''' hello
      in this way we can write 
      multiline strings
      ... bye bye''')
print(name[0:3], name[0:-1])    #indexing
for letter in name:                # for looping concept
    print(letter, sep=" ")
print("the length of string is ",len(name))
print(name.upper())
print(name.lower())
print(name.rstrip('!')) #removes trailing character
print(name.replace('d','n'))
print(name.split("c"))

name1 = "anaconda"
print(name1.capitalize())  #only 1st char uppercase
print(name1.title())   #upper case 1st letter of each word
print(name1.center(50))
print(name1.count('n'))
print(name1.endswith("a"))
print(name1.find('c'))
print(name1.index("con"))
print(name1.swapcase())


# if-elif-else condition
a = 3
b = 7
c = 9
if(a>b and a>c):
    print(f"{a} is greater than {b} and {c}")
elif(b>a and b>c):
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")

#MATCH CASE IN PYHTON
x = int(input("enter the value of x: "))
match x:
    case 0:
        print(" x is 0")
    case 4:
        print("x is 4")
    case _:
        print(" the value is ",x)   # default case allowed in last
    # case _ if x !=90:                # remove comment and run it after removing default case statement
    #     print( x," is not 90")



#WHILE LOOP WITH ELSE STATEMENT
i = 5
while(i>0):
    print(i)
    i -=1
else:
    print("end of the while loop")


# break statement -> breaking out of the loop
# continue statement -> skips the one iteration of loop