
class Student:
    age=10
    language="Hindi"
    fullName ="default"

    def display(self):
        print(self.fullName)

amol = Student()
amol.display()

# print(amol.age)
# print(amol.language)
# print(amol.fullName)

archit = Student()
amol.age = 34
archit.display()


print(amol.age)
print(archit.age)
class Student:
    def _init_(self ,nm=0 , ag=0 ,gr=0):
        self.name = nm
        self.age= ag
        self.gender = gr

    def display(self):
        print(self.name)


amol = Student(ag=23,nm="amol", gr="Male")
mayuri = Student("mayuri","24","Female")

mayuri.display()
amol.display()
#------------------------------------------->
class Bank:
    def _init_(self,accNo,accName,bal):
        self.accountNumber = accNo
        self.accName = accName
        self.balance = bal

    def depoist(self,amount):
            self.balance = self.balance+ amount

    def withDrawl(self,amount):
        if(amount < self.balance):
            self.balance = self.balance - amount
        else:
            print('Insufficient Balance')

chinmay = Bank(123,"chinmay deshpande",1000)
chinmay.withDrawl(500)
print(chinmay.balance)
chinmay.depoist(100000)
print(chinmay.balance)

# functions , string , list , dictionary,set
# class
class person:
    def _init_(self,name):
        self.name = name
        self.db = self.Dob()

    def display(self):
        print(self.name)

    class Dob:
        def _init_(self):
            self.dd = 7
            self.mm = 11
            self.yy = 1980

        def display(self):
            print(str(self.dd),str(self.mm),str(self.yy))

p = person('chinmay')
print(p.name)
p.db.display()
h = p.db
print(h.dd)


















































#Encapsulation
#polymorphism
#Inheritance
#Abstraction

# program 1

#
# class Teacher:
#     def setid(self,id):
#         self.id = id
#
#     def getid(self):
#         return self.id
#
#     def setname(self,name):
#         self.name = name
#
#     def getname(self):
#         return self.name
#
#     def setaddress(self, address):
#         self.address = address
#
#     def getaddress(self):
#         return self.address
#
# t = Teacher()
#
# # t.setid(12)
# # print(t.getid())
# #
# # t.setname("chinmay")
# # print(t.getname())
# #
# # t.setaddress("Hadapar pune")
# # print(t.getaddress())
# class Student(Teacher):
#     def setmarks(self,marks):
#         self.marks = marks
#
#     def getmarks(self):
#         return self.marks
#
# amol = Student()
# amol.setid(12)
# print(amol.getid())
#
# amol.setname("chinmay")
# print(amol.getname())
#
# amol.setaddress("Hadapar pune")
# print(amol.getaddress())
#
# amol.setmarks(900)
# print(amol.getmarks())
#



# class Teacher(object):
#
#     def _init_(self,name,address):
#         self.name = name
#         self.address = address
#
#     def display(self):
#         print(self.name)
#
# class Student(Teacher):
#     pass
#
# amol = Student("binay","pune ")
# amol.display()



class Teacher(object):

    def _init_(self,name,address):
        self.name = name
        self.address = address

    def display(self):
        print(self.name)

class Student(Teacher):
    def _init_(self,name,address,marks):
        super()._init_(name,address)
        self.marks = marks

    def display(self):
        print(self.marks)
        super().display()



d = Student("chinmay","pune",900)
d.display()


# Single inheritance
class Bank(object):

    cash = 10000

    @classmethod
    def available_bal(cls):
        print(cls.cash)

class SBI(Bank):
    cash = 20000
    @classmethod
    def available_bal(cls):
        print(cls.cash + Bank.cash)

class PNB(Bank):
    pass
pnb = PNB()
pnb.available_bal()

sbi = SBI()
sbi.available_bal()

#Multi-level inheritance

class GrandFather(object):

    lastName = "Deshpande"
    def _init_(self,firstName):
        self.firstName = firstName

    def display(self):
        print(self.firstName +" "+self.lastName)

class Father(GrandFather):

    def _init_(self,firstName,ffirstName):
        super()._init_(firstName)
        self.ffirstName = ffirstName

    def display(self):
        print(self.ffirstName +" "+self.lastName)
        super().display()

class Son(Father):

    def _init_(self,firstName,ffirstName,sfirstName):
        super()._init_(firstName,ffirstName)
        self.sfirstName = sfirstName

    def display(self):
        print(self.sfirstName+" "+self.ffirstName +" "+self.lastName)
        super().display()



chinmay = Son("manohar","shirsh","chinmay")
chinmay.display()


# Multiple Inheritance

# multiple inheritance


class Father:

    def height(self):
        print('6 feet tall')

class Mother:
    def color(self):
        print('Color is brown')

class Son(Father,Mother):
    pass


chinmay = Son()
chinmay.color()
chinmay.height()

# ---------
class Father:

    def name(self):
        print('name called from father')

class Mother:
    def name(self):
        print('name called from mother')

class Son(Mother,Father):
    pass


chinmay = Son()
chinmay.name()

# ------------------

# Method resolution order

class A(object):
    def method(self):
        print('A class method')
        super().method()

class B(object):
    def method(self):
        print('B class method')
        super().method()

class C(object):
    def method(self):
        print('C class method')

class X(A,B):
    def method(self):
        print('X class method')
        super().method()
class Y(B,C):
    def method(self):
        print('Y class method')
        super().method()
class P(X,Y):
    def method(self):
        print('P class method')
        super().method()

p = P()
p.method()




















# Single inheritance
class Bank(object):

    cash = 10000

    @classmethod
    def available_bal(cls):
        print(cls.cash)

class SBI(Bank):
    cash = 20000
    @classmethod
    def available_bal(cls):
        print(cls.cash + Bank.cash)

class PNB(Bank):
    pass
pnb = PNB()
pnb.available_bal()

sbi = SBI()
sbi.available_bal()

#Multi-level inheritance

class GrandFather(object):

    lastName = "Deshpande"
    def _init_(self,firstName):
        self.firstName = firstName

    def display(self):
        print(self.firstName +" "+self.lastName)

class Father(GrandFather):

    def _init_(self,firstName,ffirstName):
        super()._init_(firstName)
        self.ffirstName = ffirstName

    def display(self):
        print(self.ffirstName +" "+self.lastName)
        super().display()

class Son(Father):

    def _init_(self,firstName,ffirstName,sfirstName):
        super()._init_(firstName,ffirstName)
        self.sfirstName = sfirstName

    def display(self):
        print(self.sfirstName+" "+self.ffirstName +" "+self.lastName)
        super().display()



chinmay = Son("manohar","shirsh","chinmay")
chinmay.display()


# Multiple Inheritance

# multiple inheritance


class Father:

    def height(self):
        print('6 feet tall')

class Mother:
    def color(self):
        print('Color is brown')

class Son(Father,Mother):
    pass


chinmay = Son()
chinmay.color()
chinmay.height()

# ---------
class Father:

    def name(self):
        print('name called from father')

class Mother:
    def name(self):
        print('name called from mother')

class Son(Mother,Father):
    pass


chinmay = Son()
chinmay.name()

# ------------------

# Method resolution order

class A(object):
    def method(self):
        print('A class method')
        super().method()

class B(object):
    def method(self):
        print('B class method')
        super().method()

class C(object):
    def method(self):
        print('C class method')

class X(A,B):
    def method(self):
        print('X class method')
        super().method()
class Y(B,C):
    def method(self):
        print('Y class method')
        super().method()
class P(X,Y):
    def method(self):
        print('P class method')
        super().method()

p = P()
p.method()