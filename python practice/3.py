# Conditional statements


#if / else

numberOfTickets = 10

# if condition(True):
#     statementOne
#     stamentTwo
#     statementThree
#     statementFour
#     stementFive


if numberOfTickets <= 5:
    print('Total Disocunt : 10')

if numberOfTickets >= 10:
    print('Totoal Discount :20')

#if else (else block is executed with false condtion )



# if numberOfTickets <=5:
#     print('Total Discount : 10')
# else:
#     print('Please Enter valid output')


if numberOfTickets <= 5:
    print('10  discount ')

elif numberOfTickets >= 6:
    print('20 discount ')

else:
    print('please enter the valid input')
#
# #-------------------------------------
#
# if numberOfTickets <= 5:
#     print('10  discount ')
#
# if numberOfTickets >= 6:
#     print('20 discount ')
#
# else:
#     print('please enter the valid input')



# y = input('Please Enter the Number of Tickets')
# print(type(y)) # str
# y = int(y)  # convert int() ----- int
# print(type(y)) # int
# x = str(10)
# #10  ------ '10'
#
# if numberOfTickets <= 5:
#     print('10  discount ')
#
# if numberOfTickets >= 6:
#     print('20 discount ')
#
# else:
#     print('please enter the valid input')