def foo(number):
    n1 = 0
    n2 = 1
    for i in range (number - 1):
        temp = n1 + n2
        yield temp
        n1 = n2
        n2 = temp

for y in foo(6):
    print (y)
