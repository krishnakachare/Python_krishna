x = 10
x = "chinmay"
x = True


x = 10
y = 20

#Arthimetic operation

#* , + ,/,%

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

print(45%2)

u = 10
j = 20

print(u+j)
print(u-j)
print(u*j)
print(u/j)
print(u%j)

# Donot repeat yourself --- DRY


def calculator(x,y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

calculator(10,20)
print('--------')
calculator(100,30)

#---------------------

# function without and without return type

def add():
    print(6+7)
add()
add()

# function with parameter and without return type

def sub(x,y):
    print(x-y)

sub(100,20)
sub(500,40)


# function with parameter and return type


def mul(x,y):
    return x*y
h = mul(10,10)
print(h)
print(h+10)
print(h*20)



# 100
# 100 show
# function without parameter and with return type


def piValue():
    return 3.14

vv = piValue()
print(vv)





# // without parameter and with retuen 
    
# // with parameter 

# // with par and with return 

# // without par and with return




















name = "chinmay"
print(type(name))

# string stores the value by index
firstName = "raghav"
#      0   1  2  3  4  5
#      r   a  g  h  a  v
print(firstName[0])
print(firstName[5])


city = "Pune"

# Method len()
# Action - to find the length
# Return number .. i.e the length of string

j = len(city)
print(j)

city = "Nagpur"
kk = len(city)
print(kk)

#     0  1   2  3  4  5
#     n   a  g  p  u  r

print(city[0])
print(city[kk-1])

# len of string -1 will the last index

nameC = "amol"
vv = len(nameC)
print(vv)
print(nameC[4-1])

#------------------------------>
# Methods of string
language = "Hindi"
bb = type(language)
print(bb)

# Method

# Action
# Return
bbc = language.lower()
print(bbc)
# Action
# Return
nn = language.upper()
print(nn)

language = "Hindi"
print(language.lower().upper().count('H'))
# lower() --- string --- string

# count - also consider substring
fruit = "banana"
vv = fruit.count('na')
print(vv)

# lower() upper() count() capitalize

# Method -- capatilize first character of string
# return  - string

oo = fruit.capitalize()
print(oo)













# object --- human
# properties -- age color weight height firstName
# methods -- walk() talk() running()


# object ---- car
# properties --  color type glasses regNo
# methods -- start() stop()


# object ----bank
# properties -- accountName , accountNumber
# methods -- depoist() withdraw()








name = "chinmay"

# strings stores the character by index
#   0     1    2    3     4   5    6
#   c     h    i    n     m    a   y
#  -7    -6   -5   -4    -3   -2  -1


print(name[0])
print(name[-3])

# slice
#name[start:end:step]
print(name[1:5])
print(name[2:6]) #endposition not included
print(name[3:])
print(name[:6])
print(name[-6:6])
print(name[-7:-3])
print(name[-3:-7])
print(name[1:6:2])

fullName = "chinmay deshpande"

print(fullName[0])

#basic two types of for loop

for char in fullName:
    print(char)

# range() function

# for loop with range() func
#
#
# for x in range(1,10):
#     print(x)
#
# for x in range(10):
#     print(x)
#
# for x in range(2,10):
#     print(x)
#
# for x in range(2,99):
#     print(x)
#
# for x in range(2,99,3):
#     print(x)


name = "amol"

# for char in name:
#     print(char)

# for x in range(4):
#     print(name[x])



g = "raghav"

print(g[0])
for char in g:
    print(char)

for char in range(6):
    print(g[char])


fruits = "apple"
print(fruits.count('p'))
count = 0

for char in fruits:
    if char == 'p':
        count = count + 1
print(count)

count2 = 0
for char in range(len(fruits)):
    #print(fruits[char])
    if fruits[char] == 'p':
        count2 = count2 + 1
print(count2)

#--------

m = "chinmaya deshpande"
for index in range(len(m)):
    if m[index] == "a":
        print(index)
# even
for x in range(2,51,2):
    print(x)

for x in range(2,100):
    if x % 2 == 0:
        print(x)

# odd
# steps







# object --- human
# properties -- age color weight height firstName
# methods -- walk() talk() running()


# object ---- car
# properties --  color type glasses regNo
# methods -- start() stop()


# object ----bank
# properties -- accountName , accountNumber
# methods -- depoist() withdraw()