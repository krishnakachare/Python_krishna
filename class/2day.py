










































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


# lists = [Student("chinmay",30),Student("amol",30),Student("poorva",30),Student("amol",30)]
# for item in lists:
#     print(item.display())
#
#
# listC = ["Apple","Mango","Apple"]
#
# for item in listC:
#     print(item)
#
# for item in range(len(listC)):
#     print(listC[item])









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



class Car:

    # class variable
    madeIn = "India"

    def _init_(self,color,type,regNo):
        # instance  variable
        self.color = color
        self.type = type
        self.regNo = regNo


audi = Car("black","SUV",213)
bmw = Car("red","Sedane",456)
jaqour = Car("green","MUV",4546)

print(audi.madeIn)
audi.madeIn = "US"

print(audi.madeIn)
print(jaqour.madeIn)
print(bmw.madeIn)


# program 5

class Sample:
    def _init_(self):
        self.x = 10
    def modify(self):
        self.x = self.x + 1

s1 = Sample()
s2 = Sample()

print(s1.x)
print(s2.x)

s1.modify()
print(s1.x) # 11
print(s2.x) # 10


# program 6

class Car:

    # class variable
    madeIn = "India"

    @classmethod
    def modify(cls):
        cls.madeIn = "USA"

    def modifyI(self):
        self.madeIn = "USA"


    def _init_(self,color,type,regNo):
        # instance  variable
        self.color = color
        self.type = type
        self.regNo = regNo


audi = Car("black","SUV",213)
bmw = Car("red","Sedane",456)
jaqour = Car("green","MUV",4546)

audi.modifyI()
Car.modify()

print(audi.madeIn)
print(audi.madeIn)
print(audi.madeIn)





# print(audi.madeIn)
# audi.madeIn = "US"
#
# print(audi.madeIn)
# print(jaqour.madeIn)
# print(bmw.madeIn)

#program 7

class Student:
    # constructor
    def _init_(self , n = '',m=0):
        self.name= n
        self.marks =m

    def display(self):
        print(self.name)
        print(self.marks)

    def calculate(self):
        if self.marks >= 60:
            print('Division A')
        elif  self.marks > 50 and  self.marks < 60:
            print('Division B')
        else:
            print('Division C')
#
# Student('chinmay',40)
# Student('amol',59)
# Student('poorva',80)

h = [Student('chinmay',40),
Student('amol',59),
Student('poorva',80)]


for item in h :
    item.calculate()