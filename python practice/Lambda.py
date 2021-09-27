# Anonoumose function
# Lambda function
# s= [1,5,2,5,1,7]

def square(x):
    return x*x
print (square(5))


f = lambda x:x*x
print(f(5))

def max(x,y):
    if x>y :
        print(x)

y = lambda  x,y:x if x>y else y
print(y(22,5))

c = lambda x,y:x if x<y else y
print(c(55,8))

d = lambda x,y :x+y
print(d(5,2))

# ***********************
a,b= [int(n) for n in input('Enter the number').split(',')]
print(f'bigger number is {y(a,b)}')


a,b = [int(n) for n in input('enter the number').split(',')]
print(f'addition is{(a+b)}')













