import sys
# !=	Проверяет равны ли оба операнда. Если нет, то условие становится истинным.
if len(sys.argv) != 4:
    # raise  --- Возбуждает указанное исключение. Инструкция позволяет прервать штатный поток исполнения при помощи возбуждения исключения.
    raise Exception("Необхідна підтримка 4 базових арифметичних операцій")
    #sys.argv - список аргументов командной строки, передаваемых сценарию Python. sys.argv[0] является именем скрипта(пустой строкой в интерактивной оболочке).
if not type(sys.argv[1]) and type(sys.argv[3]) is int:
    raise TypeError("Помилка")

s = sys.argv[2]
if s in ('+', '-', '*', '/'):
    x = int(sys.argv[1])
    y = int(sys.argv[3])
    if s == '+':
        print(x+y)
    if s == '-':
        print(x-y)
    if s == '*':
        print(x*y)
    if s == '/':
        print(x/y)

# НЕ РОЗІБРАВСЯ 

