def foo(number):
    n1 = 0
    n2 = 1
    print (n1, n2, end = ' ')
    for i in range (number - 2):
        print (n2 + n1, end = " ")
        n2 = n1 + n2
        n1 = n2 - n1
    return n1 + n2

print (foo(6))

'''
pretty strightforward, the n2 is the next item of the sequence and
and n1 takes its place
'''
