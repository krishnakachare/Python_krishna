# # # # class Person():
# # # #     age = 12
# # # #     eyecolor = 'white'
# # # #
# # # #     def print(self):
# # # #         print(self.age)
# # # #         print(self.eyecolor)
# # # #
# # # # raju= Person()
# # # # print(raju.age)
# # # # print(raju.eyecolor)
# # #
# # #
# # #
# # #
# # # #
# # # # class Person():
# # # #     age  = 20
# # # #     eyecolor ='white'
# # # #
# # # # #     settet method
# # # #     def setAge(self,age):
# # # #         self.age = age
# # # #     def setEyecolor(self,color):
# # # #         self.eyecolor = color
# # # #
# # # #     def getAge(self):
# # # #        print(self.age)
# # # #
# # # #     def getEyecolor(self):
# # # #        print(self.eyecolor)
# # # #
# # # #     def printAgeColor(self):
# # # #         print(self.age,self.eyecolor)
# # # # sanchu = Person()
# # # # print(sanchu.age)
# # # # print(sanchu.eyecolor)
# # # # sanchu.printAgeColor()
# # # #
# # # #
# # # # qas = Person()
# # # # print(qas.age)
# # # # print(qas.eyecolor)
# # # # qas.printAgeColor()
# # # #
# # #
# # #
# # # # clas0Eye
# # #
# # #
# # #
# # #
# # #
# # #
# # # # class women():
# # # #     age = 20
# # # #     name = "sanchira"
# # # #
# # # #     def printAgeName(self):
# # # #          print(self.age,self.name)
# # # # sanchita= women()
# # # # print(sanchita.name)
# # # # print(sanchita.age)
# # # # sanchita.printAgeName()
# # # #
# # # #
# # # #
# # # #
# # # # sanchita.age=52
# # # # print(sanchita.age)
# # # #
# # # # tanu = women()
# # # # print(tanu.age)
# # # # tanu.age=52
# # # # print(tanu.age)
# # #
# # #
# # #
# # # class women():
# # #     age = 20
# # #     name = "sanchira"
# # # #
# # #     def setAge(self, a):
# # #         self.age = a
# # #     def setName(self, name):
# # #        self.name = name
# # #
# # #     def getAge(self):
# # #         print(self.age)
# # #
# # # #     def getName(self):
# # # #         print(self.name)
# # # #
# # # #     def printAgeName(self):
# # # #         print(self.age,self.name)
# # # #
# # # # sanchita = women()
# # # # print(sanchita.age)
# # # # print(sanchita.name)
# # # # sanchita.printAgeName()
# # # #
# # # # sanchita.setAge(30)
# # # # sanchita.setName('dhanu')
# # # # sanchita.printAgeName()
# # # #
# # # # sanchita.getAge()
# # # # sanchita.getName()
# # # # sanchita.printAgeName()
# # #
# # #
# # #
# # #
# # #
# # # class family():
# # #     member  = 30
# # #     age = 52
# # #     name ="sanchita"
# # #
# # #     def setMember(self, member):
# # #         self.member = member
# # #
# # #     def setAge(self, age):
# # #         self.Age = age
# # #
# # #     def setName(self, name):
# # #         self.name = name
# # #
# # # raju = family()
# # # print(raju.age)
# # # print(raju.name)
# # # raju.name = "sunanda"
# # # print(raju.name)
# # #
# # # raju.name="pranita"
# # # print(raju.name)
# #
# #
# #
# # # class student():
# # #
# # #     def __init__(self,name,mark,age):
# # #         self.name= name
# # #         self.mark =mark
# # #         self.age = age
# # #
# # #     def setVlues(self,name,mark,age):
# # #         self.mark = mark
# # #         self.name = name
# # # #         self.age = age
# # #
# # #     def getValues(self):
# # #         print(self.name,self.mark,self.age)
# # #
# # #     def printMarkAgeaName(self):
# # #         print("Hi My name is {}".format(self.name))
# # #         print("Hi My mark is {}".format(self.mark))
# # #         print("Hi My age is {}".format(self.age))
# # #
# # # sanchita = student("raju",50,12)
# # # sanchita.printMarkAgeaName()
# # # sanchita.setVlues("dhanu",92,12)
# # # sanchita.printMarkAgeaName()
# # # sanchita.getValues()
# #
# # class sample():
# #     def __init__(self):
# #         self.x = 10
# #     def modifiedvaliue(self):
# #         self.x+=1
# #
# #
# # s1= sample()
# # s2= sample()
# # print("x1 in s1" ,format(s1.x))
# # print("x2 in s2" ,format(s2.x))
# #
# # s1.modifiedvaliue()
# # s2.modifiedvaliue()
# #
# # print("x1 in s1" ,format(s1.x))
# # print("x2 in s2" ,format(s2.x))
# # s1.modifiedvaliue()
# # s2.modifiedvaliue()
# # s1.modifiedvaliue()
# # s2.modifiedvaliue()
# # print("x1 in s1" ,format(s1.x))
# # print("x2 in s2" ,format(s2.x))
#
#
# # class Student():
# #     x=10
# #     @classmethod
# #     def modified(cls):
# #
# #         cls.x+=1
# # s1=Student()
# # s2=Student()
# #
# # s1.x= 20
# # s2.x=21
# # Student.modified()
# # Student.modified()
# # s1.modified()
# # print(s1.x)
# # s1.modified()
# # print(s1.x)
#
#
# class School():
#     SchoolName = 'malpani'
#     def __init__(self,name,mark):
#         self.name =name
#         self.mark = mark
#     def displayMethod(self):
#         print("may name is{},my mark is{}")
#     def calculateGrade(self):
#         if self.mark >=50:
#             print('grade c')
#         elif self.mark >50 and self.mark<=90:
#             print('grade b')
#         elif self.mark>90 and self.mark<=100:
#             print('grade a')
#
# listSchool = []
# i = 0
# while (i <= 2):
#       name=input("enter the name")
#       mark = int (input("enter the mark"))
#       listSchool.append((School(name,mark)))
#
#       i += 1
#
#       # listSchool = [obj1,obj2,obj3,obj4]
# for item in listSchool:
#      item.calculateGrade()






# passing information from one class to another class
# class Employee:
#     def __init__(self,name,age,color):
#         self.name = name
#         self.age = age
#         self.color = color
#     def display(self):
#         print(self.name,self.age,self.color)
#
# e1 = Employee("chinmay",29,"white")
# e1.display();
# class EmployeeDetails:
#
#
#     @staticmethod
#     def displayIn(obj):
#         obj.display()
#
# EmployeeDetails.displayIn(e1)
# A class inside another class in inner class
# Inner

# class Person:
#     def _init_(self):
#         self.name = "chinmay"
#         self.age = 30
#         self.db = self.Dob()
#     def disply(self):
#         print(self.name,self.age,self.db.display())
#     # inner class
#     class Dob:
#         def _init_(self):
#             self.dd = 10
#             self.mm = 1
#             self.year = 1989
#
#         def display(self):
#             return  self.dd,self.mm,self.year
#
# raju = Person()
# raju.disply()
# # p = Person()
# # p.disply()
# x = p.db
# x.display()
#
#


# class Person:
#     def _init_(self,name):
#         self.name = name
#
#     def display(self):
#         print("My name is {}".format(self.name))
#
#     class Dob:
#
#         def _init_(self):
#             self.dd = 10
#             self.mm = 1
#             self.year = 1989
#
#         def display(self):
#             return self.dd, self.mm, self.year
#
#
#
# p = Person("chinmay")
# p.display()
#
#
# x = Person('chinmay').Dob()
# print(x.display())



# class person:
#
#     age = 20
#     color = 'blue'
#
#
#
#     def walk(self):
#         print('I am walking')
#     def talk(self):
#         print('i am talk')
# sanchita = person()
# print(sanchita.age)
# print(sanchita.color)
#
# age = 23
# age=int(input('please enter your age?'))
# if age > 18:
#     print('you can drink')
# if age > 5 and age < 18:
#     print('you can swim')
# else :
#     print('you can sit at ahome')
#
#
#
# if 'hello':
#     print('hello from new word')
#
# age = int(input('plz enter your age'))
# name = 'sanchita'.lower()
# lastname = 'dhole'.lower()
#
# if age >18:
#     if name.startswith('s') and lastname.startswith('d'):
#         print('city is pune')
#     else:
#         print("city is nagpur")
# else:
#         print('city is mumbai')


list =['A','B','C']
for item in list:
    print(item)
for item in range(len(list)):
    print(item)

i = 0
while(i<=3):
    print('hello')
    break
    i = i+1

i=0
while(i<=3):
    i=i+1
    if i==2:
        continue
    print('hello')