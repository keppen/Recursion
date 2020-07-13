# n0 = 0, n1 = 1 nx = nx-1 + nx+2 

def foo (number, var):
    print ('beggining\nnumber =', number, 'item = ', var)
    if number == 0:
        print ('= 0')
        return 0
    elif number == 1:
        print ('= 1')
        return 1
    else:
        a = foo(number - 1, 'n - 1')
        b = foo(number - 2, 'n - 2')
        print ('n - 1 =', a, '\nn - 2 =', b)
        fibb = a + b
        print (fibb)
        return fibb

print (foo(7,'init'))
