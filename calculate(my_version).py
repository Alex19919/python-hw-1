# Спробував зробити по ось цьому відео: https://www.youtube.com/watch?v=k4A5H6nNWQs&list=PLIVOoSN7YV-iQ5XgENvV0qevsv6PsndLC&index=27&ab_channel=%D0%9A%D0%B0%D0%B1%D1%96%D0%BD%D0%B5%D1%82%D1%96%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8

# але чомусь в output не можу  внести значення (((     на відео все на сайті в коснолі

a = int(input('First number: '))
b = int(input('Second number: '))

d = int(input('Choose an arithmetic operation: \n 1 addition \n 2 subtraction \n 3 multiplication \n 4 division \n'))

if d == 1:
    r = a+b
    p = 'addition'
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
print('Result', o, 'number', a, 'and', b, '=', r)
