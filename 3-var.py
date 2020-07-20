def foo(number):
    n1 = 0
    n2 = 1
    print (n1, n2, end = ' ')
    for i in range (number - 2):
        n3 =  n1 + n2
        print (n3, end = ' ')
        n1 = n2
        n2 = n3
    return n1 + n2

print (foo(6))

'''
the idea is to pass the value of an item to next one, there n3 is kind of
temporary
'''

