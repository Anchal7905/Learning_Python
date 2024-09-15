import random
print('''
      
!!WELCOME TO S-W-G!!
**********YOU'LL GET 10 CHANCES TO WIN THIS GAME***********
      ''')
c=0
for i in range(10):
    user = int(input(' Press \n0: snake\n1:water\n2:gun \n'))
    comp = random.randrange(0,2)
# print("user:",user,"comp:",comp)
    
    if( user == 0):
        print('user:','snake')
        if comp == 0:
            print('comp: snake')
            print('draw')
        elif comp == 1:
            print('comp:water')
            print('1 point')
        else:
            print('comp: gun')
            print('0 points')
    if( user == 1):
        print('user:','water')
        if comp == 1:
            print('comp:water')
            print('draw')
        elif comp == 2:
            print('comp: gun')
            print('1 point')
        else:
            print('comp: snake')
            print('0 points')
    if( user == 2):
        print('user:','gun')
        if comp == 2:
            print('comp: gun')
            print('draw')
        elif comp == 0:
            print('comp: snake')
            print('1 point')
        else:
            print('comp:water')
            print('0 points')
    
    if user == comp:
        c = c+1
print('total score', c)