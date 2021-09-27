# f = open('first.txt','w')
# str = input('input the string')
# f.write(str)
# f.close()

# f = open('first.txt','r')
# print(f.read())
# str=f.read()
# print(str)
# f.close()

# f = open('first.txt','r')
# print(f.read().upper())

f = open('second.txt','w')
print('exixt on @')
while str !='@':
    str = input('enter the string')
    if str != '@':
        f.write(str+ '\n')
f.close()
#
# # f = open('first.txt','r')
# # print(f.readline())
#
#
#
# # # line = f.readline()
#
f = open('second.txt','r')
lines = f.readline()
# lines = f.read().splitlines()
print(lines)
# #
class Student():
     def __init__(self, a):
         self.a = a

     def printA(self, a):
         print(self.a)

b =  Student('hello')
b.printA('nk')



