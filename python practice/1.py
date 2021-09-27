# # # #arithmatic
# # # m = 27
# # # n= 56
# # #
# # # print(m+n)
# # # print(m-n)
# # # print(m/n)
# # # print(m*n)
# # # print(m%n)
# # # print(m+n)
# # #
# # #
# # # # #Comparision
# # # #
# # # # print(m>n)
# # # # print(m<n)
# # # # print(m>=n)
# # # # print(m<=n)
# # # # print(m!=n)
# # #
# # # # logical
# # #
# # # print(23>52 and 51>52)
# # # print(23<52 and 51<52)
# # # print(23<=52 and 51>=52)
# # # print(23 > 52 or 51 ==52 )
# # #
# # #
# # #
# # # def add(x,y):
# # #     print(x+y)
# # #     print(x * y)
# # #     print(x - y)
# # # add(65,8)
# # #
# # #
# # #
# # # conditional
# #
# #
# a=True
# print(type(a))
# a=1
#
# print(type(a))
#
#
# # DRY
# def calculator(x,y):
#     # x = 32
#     # print(x)
#     print(x+y)
#     print(x-y)
# calculator(2,2)
#
# def sub(x,y):
#     print(x-y)
# calculator(5,2)
#
#
#
# def add():
#     print(3+5)
# add()
#
# def add(x,y):
#     print(x+y)
# add(2,3)
#
# def add(x,y):
#    return x+y
# c = add(32,1)
# print(c-2)
#
#
# name = 'sanchita'
# lastname = 'dhole'
# print(name+lastname)
# print(f'my first name is {name} and my last name is{lastname}')
# print('my first name is{} and my last name is{}'.format(name,lastname))


# def ispalindrome(s):
#     return s == s[::-1]
# s = 'malbgbgfbgfayalam'
# ans = ispalindrome(s)
# if ans:
#     print('yes')
# else:
#     print('no')
#
#
#
# a = input('enter a character')
# print(a)



import pandas as pd

# listA = ['a','b','c']
# a = pd.Series(listA)
# print(a)


listA = [1,2]
a = pd.Series(listA)
print(a)

print(a.values)
print(a.ndim)
print(a.dtype)

print(a.sum())
print(a.product())
print(a.max())
print(a.shift())


name = "apple"
for char in name:
    print(char)