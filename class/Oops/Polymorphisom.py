from abc import ABC, abstractmethod
class myClass(ABC):
    @abstractmethod
    def calulate(self,x):
        pass

class Square(myClass):

    def display(self):
        print('hello')
    def calulate(self,x):
        print(x*x)

class Cube(myClass):
    def calulate(self,x):
        print(x*x*x)

    def display2(self):
        print('hello2')

# a = Cube()
# a.display2()
# a.calulate(12)
#
# b= Square()
# b.display()
# b.calulate(2)
c = myClass()


#if abstarct method is present in parent class , then child should have
#abstract method implemation (body)

# If a class contains abtract method , we cannot create object of same class


from abc import ABC, abstractmethod

class Car(ABC):

    def _init_(self,regno):
        self.regno = regno

    def OpenTank(self):
        print('print fuel tank ')

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def braking(self):
        pass

class Audi(Car):
    def steering(self):
        print('audi steering')
    def braking(self):
        print('audi braking')

class BMW(Car):
    def steering(self):
        print('BWM steering')
    def braking(self):
        print('BWM braking')


a = Audi("123")
a.OpenTank()
a.braking()
a.steering()


b = BMW("567")
b.OpenTank()
b.braking()
b.steering()






































# class Duck(object):
#     def talk(self):
#         print('quack quack')
#
#
# class Human(object):
#     def talk(self):
#         print('Hello hi ')
#
# def call_talk(obj):
#     obj.talk()
#
# x = Duck()
# y = Human()
# call_talk(x)
# call_talk(y)

# class Dog:
#     def bark(self):
#         print('Bow Bow')
#
# class Duck(object):
#     def talk(self):
#         print('quack quack')
#
# class Human(object):
#     def talk(self):
#         print('Hello hi ')
#
# def call_talk(obj):
#     obj.talk()
#
#
# x = Dog()
# y = Duck()
# z = Human()
#
# call_talk(x)
# call_talk(y)
# call_talk(z)


class Dog:
    def bark(self):
        print('Bow Bow')

class Duck(object):
    def talk(self):
        print('quack quack')

class Human(object):
    def talk(self):
        print('Hello hi ')

def call_talk(obj):
    if(hasattr(obj,'talk')):
        obj.talk()
    elif(hasattr(obj,'bark')):
        obj.bark()
    else:
        print("Incorrect object passed")


x = Dog()
y = Duck()
z = Human()

call_talk(x)
call_talk(y)
call_talk(z)

#operator overloading

print(6+6)
print("chinmay "+"deshpande")


# class Bookx():
#     def _init_(self,pages):
#         self.pages = pages
#
# class Booky():
#     def _init_(self,pages):
#         self.pages = pages
#
#
# b1 = Bookx(100)
# b2 = Bookx(200)
#
# print(b1+b2)
#----------------------------------->
class Bookx():
    def _init_(self,pages):
        self.pages = pages

    # def _add_(self, other):
    #     return self.pages + other.pages

class Booky():
    def _init_(self,pages):
        self.pages = pages

    def _add_(self, other):
        return self.pages + other.pages


b1 = Bookx(100)
b2 = Booky(200)
print(b2+b1)


# class Bookx():
#     def _init_(self,pages):
#         self.pages = pages

# class Booky():
#     def _init_(self, pages):
#         self.pages = pages
#
#     def _add_(self, other):
#         return self.pages + other.pages
#
# class Bookz():
#     def _init_(self, pages):
#         self.pages = pages
#
#     def _add_(self, other):
#         return self.pages + other.pages
#
#
# b1 = Bookx(100)
# b2 = Booky(200)
# b3 = Bookz(300)
# print(b2+b3+b1)

class Booky():
    def _init_(self, pages):
        self.pages = pages

    def _lt_(self, other):
        return self.pages < other.pages

    def _gt_(self, other):
        return self.pages < other.pages

class Bookz():
    def _init_(self, pages):
        self.pages = pages

y = Booky(100)
z = Bookz(200)

print(y>z)


#amazaon  method overloading

# search(a)
# search(a,b)
# search(a,b,c)
#
#
# class ClassMy:
#
#     def sum(self, a = None , b = None, c = None):
#         if(a != None and b != None and c != None):
#             print(a+b+c)
#         elif(a!=None and b!=None):
#             print(a+b)
#         else:
#             print('Please enter a valid input ')
#
# b = ClassMy()
#
# b.sum(1,3)
# b.sum(1,3,4)
# b.sum(1)

# Overiding

# different class,same method name ,same signature
# inheritance -- overide inheritance

#world- save(a)
#sbi - save(a)
#a = sbi()

class WorldBank():
    def Saving(self,amount):
        if(amount > 1000):
            print('Saving successful')

class SBIBank(WorldBank):
    def saving(self,amount):
        if(amount > 500):
            print('SBI Saving successful')
        else:
            print('Minimum bal should be 500')

class BOIBank(WorldBank):
    def saving(self,amount):
        if(amount > 500):
            print('SBI Saving successful')
        else:
            print('Minimum bal should be 500')

SBIBank().saving(499)

# same class , same method name , different signature - overload
# Different class have interitance , same method , same signature
# overriding

import math
class Square():
    def area(self,x):
        print(x*x)

class Circle(Square):
    def area(self,x):
        print(math.pi * x * x)

c = Circle()
c.area(23)

d = Square()
d.area(23)


# oops

#Abstraction
# a.should('have.text',"hello")
# b.should('have.att','href','value')
































































# class Duck(object):
#     def talk(self):
#         print('quack quack')
#
#
# class Human(object):
#     def talk(self):
#         print('Hello hi ')
#
# def call_talk(obj):
#     obj.talk()
#
# x = Duck()
# y = Human()
# call_talk(x)
# call_talk(y)

# class Dog:
#     def bark(self):
#         print('Bow Bow')
#
# class Duck(object):
#     def talk(self):
#         print('quack quack')
#
# class Human(object):
#     def talk(self):
#         print('Hello hi ')
#
# def call_talk(obj):
#     obj.talk()
#
#
# x = Dog()
# y = Duck()
# z = Human()
#
# call_talk(x)
# call_talk(y)
# call_talk(z)


class Dog:
    def bark(self):
        print('Bow Bow')

class Duck(object):
    def talk(self):
        print('quack quack')

class Human(object):
    def talk(self):
        print('Hello hi ')

def call_talk(obj):
    if(hasattr(obj,'talk')):
        obj.talk()
    elif(hasattr(obj,'bark')):
        obj.bark()
    else:
        print("Incorrect object passed")


x = Dog()
y = Duck()
z = Human()

call_talk(x)
call_talk(y)
call_talk(z)

#operator overloading

print(6+6)
print("chinmay "+"deshpande")


# class Bookx():
#     def _init_(self,pages):
#         self.pages = pages
#
# class Booky():
#     def _init_(self,pages):
#         self.pages = pages
#
#
# b1 = Bookx(100)
# b2 = Bookx(200)
#
# print(b1+b2)
#----------------------------------->
class Bookx():
    def _init_(self,pages):
        self.pages = pages

    # def _add_(self, other):
    #     return self.pages + other.pages

class Booky():
    def _init_(self,pages):
        self.pages = pages

    def _add_(self, other):
        return self.pages + other.pages


b1 = Bookx(100)
b2 = Booky(200)
print(b2+b1)


# class Bookx():
#     def _init_(self,pages):
#         self.pages = pages

# class Booky():
#     def _init_(self, pages):
#         self.pages = pages
#
#     def _add_(self, other):
#         return self.pages + other.pages
#
# class Bookz():
#     def _init_(self, pages):
#         self.pages = pages
#
#     def _add_(self, other):
#         return self.pages + other.pages
#
#
# b1 = Bookx(100)
# b2 = Booky(200)
# b3 = Bookz(300)
# print(b2+b3+b1)






class Booky():
    def _init_(self, pages):
        self.pages = pages

    def _lt_(self, other):
        return self.pages < other.pages

    def _gt_(self, other):
        return self.pages < other.pages

class Bookz():
    def _init_(self, pages):
        self.pages = pages

y = Booky(100)
z = Bookz(200)

print(y>z)