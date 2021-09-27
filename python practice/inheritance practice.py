# # # multilevel inheritance
# #
# class person():
#     name ='sanchita'
#     age = 20
#
#     def displayNameage(self):
#         print(self.name,self.age)
#     def walk(self):
#         print("walking")
#     def talk(self):
#         print("talking")
#
# class student(person):
#     rollno= 2
#     subject ="marathi"
#
#     def displyRollnoSub(self):
#         print(self.rollno,self.subject)
#
# class teacher(student):
#      salary =500000
#
#      def displaySalary(self):
#          print(self.salary)
#
# # s1 = person()
# s1.displayNameage()
# # s1.walk()
# # s1.talk()
#
# s2=student()
# s2.walk()
# # s2.talk()
# s2.displyRollnoSub()
#
# s3=teacher()
# s3.displaySalary()
# s3.talk()
# s3.walk()
# s3.displyRollnoSub()


# # # single inheritance
# #
# # # class animal():
# # #     leg = 2
# # #     head = 1
# # #
# # #     def Printleghead(self):
# # #         print(self.leg,self.head)
# # #
# # # class dog(animal):
# # #     color ="white"
# # #
# # #     def Printcolor(self):
# # #         print(self.color)
# # #
# # #
# # # class cat(animal):
# # #     eye = "brown"
# # #
# # #     def Printeye(self):
# # #         print(self.eye)
# # # s1=animal()
# # #
# # # s1.Printleghead()
# # # s2=dog()
# # # s2.Printleghead()
# # # s2.Printcolor()
# # # s3=cat()
# # # s3.Printleghead()
# # # s3.Printeye()
# # #
# # # multiple inheritance
# # class mother():
# #     mothername ="shobha"
# #     age =52
# #
# #     def displayNameAge(self):
# #          print(self.mothername,self.age)
# #
# # class father():
# #     fathername = "machhindra"
# #     age = 56
# #
# #     def displayNameAge(self):
# #         print(self.fathername,self.age)
# #
# # class son(father,mother):
# #     sonname = "sanchita"
# #     age = 20
# #
# #     def displaySnameAge(self):
# #         print(self.sonname,self.age)
# # a=son()
# # a.displayNameAge()
#
#
#
#
# class person():
#     def __init__(self,name,lastname):
#         self.name = name
#         self.lastname = lastname
#
#     def diaplayName(self):
#         print(self.name,self.lastname)
#
# class student(person):
#     def __init__(self, rollno,name,lastname):
#         super().__init__(name,lastname)
#         self.rollno=rollno
#
#     def displayrollno(self):
#         print(self.rollno)
#
# s1 = student(12,"sanchi","dholi")
# s1.diaplayName()
#


# class X():
#     def __init__(self):
#         self.a = "a"
#         print(self.a)

# class Y():
#     def __init__(self):
#         self.y="y"
#         print(self.y)

# class Z(X,Y):
#     def __init__(self):
#         super().__init__()
#         self.z = "z"
#         print(self.z)

# a=Z()
