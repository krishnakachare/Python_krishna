


# methods or functions  of string


def add(x,y):
    return x+y
c = add(10,13)
print(c)

print('hello')


# function do something # action
#  function also returns something


name = "sanket"
c = len(name)
print(type(c))
print(c)


# Number of methods on string

firstName = "Chinmay"

#function do something # action
#function also returns something

# lower method conevert the complete string into the lower case
c = firstName.lower()
print(c)
print(type(c))

# upper()

firstName = "Chinmay"
d = firstName.upper()
print(d)
print(type(d))


firstName = "Chinmayc"
d = firstName.upper().lower() # function chaining
print(d)



y = firstName.lower().count('c')
print(y)
print(type(y))


# lower upper count

name4 = "akash"
# v = name4.capitalize().lower().upper().lower().count('a')
# print(v)

# e = name4.index('k') # first occurence
# print(e)
# e = name4.index('a',2,5) # first occurence
# print(e)

# e = name4.index('a',name4.index('a')+1)  # 2nd occurence
# print(e)

# name4 = "akash"
# e = name4.index('a')
# name4.index('a',e+1) # 2nd occurence

# for char in range(5):
#     if name4[char] == 'a':
#         print(char,name4[char])

# upper lower count index  capitalize


name5 = "Ac12123" # isUpper()  # True or False boolean
print(name5.isupper()) # check all upper
print(name5.islower()) # check all lower
print(name5.istitle()) # check first char upper
print(name5.isnumeric()) # check only for numberic
print(name5.isalpha()) # check only for alpha
print(name5.isalnum()) # it will for alpha or number or alpha








