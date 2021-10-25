 #extension py
#
# number = 10
# print(type(number))
#
# number = 10.0
# print(type(number))
#
# isAdult = True
# print(type(isAdult))
#
# char = "c"
# print(type(char))
#
# #--------------------------------
# name = "chinmayd"
# print(name[0])
# print(name[2:len(name)])
#
# # for loop
#
# for char in name:
#     print(char)
#
# for x in range(len(name)):
#     print(name[x])
#
# # list
#
#
# listA = [1,3,4,5,66,77,88]
# print(type(listA))
#
# for item in listA:
#     print(item)
#
# for x in range(len(listA)):
#     print(listA[x])
#
#
# # dictionary
#
# human = {
#     'fullName':'chinmay',
#     'age':23
#
# }
#
# # Does not stores the value by index
#
# print(human['fullName'])
# print(human.get('fullName'))
# for k in human:
#     print(k,human[k])
#
#
# #-------------------------------
#
# setA = {33,44,55,66,77,77}
# print(setA)
#
# #-----------------------------
#
# h = 'book'
# #{
# # #   'b':1,
# # #   'o':2,
# # #   'k':1
# # #
# # # }
#
# g = {}
#
#
# j = {
#     'a':2,
#     'b':3,
#     'a':4
# }
#
# # updating the dict value
# j['a'] = 5
# # inserting the new value
# j['x']= 3
#
# #print(j.get('a',"no return"))
#
# #print(j)
#
# h = 'book'
# j = {'b':1,'o':2,'k':1}
# for char in h:
#     print(char)
#     j[char] = j.get(char,0) + 1
# #   j['b'] = 1
# #   j['o'] = 1
# #   j['o']= 2
# #   j['k'] = 1
#
#
# hh = [334,44,55,55,66,77,88,99]
# min = hh[0]
# max = hh[0]
#
# for x in hh:
#     if max < x:
#         max = x
#     elif min > x:
#         min = x    # -334
#
# print(min)
# print(max)
#
#
# h = '4a3b2c'
# # #aaaabbbcc
# # print(int('4'))
#
# # print(h)
# #
# # for x in h:
# #     if type(x) == "<class 'str'>":
# #         print("hello")
#
# rev = " "
#
# for i in range(len(h)):
#     if(i%2 == 0):   # 4
#         num = int(h[i])
#         print(num)
#         rev = rev + num * h[i+1]
#
# print(rev)
#
class student():

    language = "Hindi"
    count = 0

    def _init_(self,name,rollNum):
        self.name = name
        self.roll = rollNum
        student.countinfo()

    @classmethod
    def changeLan(cls):
        cls.language = "Marathi"

    def display(self):
        print('printing from display')

    @staticmethod
    def countinfo():
        student.count = student.count + 1
        return student.count

class Teacher(student):

    def _init_(self,name,rollNum,salary):
        super()._init_(name,rollNum)
        self.salary = salary

    #overriding
    def display(self):
        print('hello')
        super().display()

    # overloading
    def add(self,a=None,b=None,c=None):
        if(a != None and b !=None and c != None):
            print(a+b+c)
        elif(a!= None and b != None):
            print(a+b)
        else:
            print('please enter the correct vlues')

a = Teacher("chinm",12,2134)

a.display()
a.add(12,3,4)
a.add(12,4)
a.add(3)

n = student("ram",23)
print(student.language)
student.changeLan()
print(student.language)
nn = student("nn",23)

print(student.count)

































































































from abc import ABC,abstractmethod
class worldBank(ABC):

    def _init_(self,country):
        self.country = country

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def loan(self):
        pass


class SBI(worldBank):
    def save(self):
        print('SBI saving method')

    def loan(self):
        print('SBI loan saving method')

    def personalLoan(self):
        print('New values SBI')


class BOI(worldBank):
    def save(self):
        print('BOI saving method')

    def loan(self):
        print('BOI saving method')

    def personalLoan(self):
        print('New values BOI')


chinmay = SBI("India")
print(chinmay.country)

chinmay.save()
chinmay.loan()

#------------------------------------------->
#
#
# class Myclass(ABC):
#
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class Oracle(Myclass):
#     def connect(self):
#         print('connecting to the oracle database')
#
#     def disconnect(self):
#         print('Disconnecting from the oracle db')
#
#
# class Postgres(Myclass):
#     def connect(self):
#         print('connecting to the postgres database')
#
#     def disconnect(self):
#         print('Disconnecting from the postgres db')
#
# class MongoDb(Myclass):
#     def connect(self):
#         print('connecting to the MongoDb database')
#
#     def disconnect(self):
#         print('Disconnecting from the MongoDb db')
#
# class Database:
#     str = input('Enter the name of db you wish to connect') #oracle
#     # convert the string into the className
#     className = globals()[str]
#     h = className()
#     h.connect()
#     h.disconnect()
#
# class Hi:
#     print("hello")