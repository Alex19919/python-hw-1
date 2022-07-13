a = int(input('First number: '))
b = int(input('Second number: '))

d = int(input('Choose an arithmetic operation: \n 1 addition \n 2 subtraction \n 3 multiplication \n 4 division \n'))

if d == 1:
    r = a+b
    p ='addition'
    o = p
if d == 2:
    r = a-b
    l = 'subtraction'
    o = l
if d == 3:
    r = a*b
    m = 'multiplication'
    o = m
if d == 4:
    r = float(a/b)
    n = 'division'
    o = n
print('Result',o,'number',a,'and',b,'=',r)
