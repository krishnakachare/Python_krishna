






































#
# # program One
# class Student:
#     def _init_(self):
#         self.name = "chinmay"
#         self.age = 20
#         self.marks = 90
#
#
#     def info(self):
#         print('Hi My name is '+ self.name)
#         print('and age is '+ str(self.age))
#         print('I got  '+str(self.marks) + 'marks')
#
#
# amol = Student()
# amol.info()
#
#
# # program 2
# #----------------------------------------------
# class Student:
#
#     def _init_(self,nm,ag,mrk):
#         self.name = nm
#         self.age = ag
#         self.marks = mrk
#
#
#     def info(self):
#         print('Hi My name is '+ self.name)
#         print('and age is '+ str(self.age))
#         print('I got  '+str(self.marks) + 'marks')
#
#
# chinmay = Student("chinmay",23,90)
# chinmay.info()
# chinmay.language = "hindi"
# print(chinmay.language)
# chinmay.language = "marathi"

# program 3

class Student:

    def _init_(self,n="",m=0):
        self.name = n
        self.marks = m

    def display(self):
        print('Hi',self.name)
        print('My marks', self.marks)

s= Student()
s.display()


y = Student("chinmay",30)
y.display()

#-------------------------->

#class  ----> 4

# name
# age
# language
# adharNo


# 4 Objects --->
# Reference variable only one
# loop ---
# # name
# # age
# # language
# # adharNo

# use constructor to set the values - 4 min
