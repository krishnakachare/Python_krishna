def da(basic):
    da = basic * 0.8
    return da

def hra (basic):
    hra = basic *0.15
    return  hra

def pf(basic):
    pf = basic * 105
    return pf


if __name__ == '__main__':
    print(hra(12000))
    print(__name__)
    print('running from the original file')
else:
    print(__name__)
    print('call from the another file')


basicSal = float(input('enter the basic salary'))
gross = hra(basicSal)+da(basicSal)+basicSal
print(f'gross salary  is{gross}')