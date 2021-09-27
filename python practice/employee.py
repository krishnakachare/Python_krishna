import employeecalculations
from employeecalculations import *
def display ():
    basicsalary = float(input('please enter your basic salary'))
    return hra(basicsalary)
print(display())