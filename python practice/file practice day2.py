# # import os ,sys
# #
# #
# #
# # fname = input('enter name ')
# # if os.path.isfile(fname):
# #     f = open(fname, 'r')
# # else:
# #     print(fname + ' not present')
# #     sys.exit()
# # #
# # f = open('xyz.png','rb')
# # f2 = open('cde.png','wb')
# # bytes = f.read()
# # f2.write(bytes)
# #
# # f.close()
# # f2.close()
# #
# # with open('mypara.txt','r') as f1:
# #     print(f1.read())
# # # #
# import pickle
# class employee(object):
#     def __init__(self , id, nm, sal):
#         self.id = id;
#         self.name = nm;
#         self.salary = sal;
#     def display(self):
#         print(self.id)
#         print(self.name)
#         print(self.salary)
#
# f = open('emp2.dat','wb')
#
# a = int(input('please enter employee number'))
#
# for i in range (a):
#     id = int(input('enter employee id'))
#     name = input('enter employee name')
#     salary = input('enter employee salary')
# e = employee(id,name,salary)
# pickle.dump(e,f)
# f.seek(10,0)
# print(f.seek)
# #
# # try:
# #     while True:
# #         obj = pickle.load(f)
# #         obj.display()
# # except EOFError:
# #             print('End of file')
#
# # f.close()
#



cl = 20
with open('city','wb')as f:
    n = int(input('enter number of cities'));
    for i in range(n):
        city  = input('enter city name')
        ln = len(city)

        city = city + (cl - ln) * ' '

        city = city.encode()
        f.write(city)
with open('city','rb')as f:
    n=int(input('enter the record number'));
    f.seek(cl*(n-1));

    print(f.read(cl).decode())


