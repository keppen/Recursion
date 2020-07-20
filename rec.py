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
        print ('OUT OF a VARIALBE\nnumber after n -1 = ', number)
        b = foo(number - 2, 'n - 2')
        print ('n - 1 =', a, '\nn - 2 =', b)
        fibb = a + b
        print (fibb)
        return fibb

print (foo(7,'init'))

'''
iterates trough a variable, ultill number var hits 1,
afterwards, the number value returns to 2. b varaible is reached, returning 0
subsequntly. n-1 and n-2 is obtained resuliting in first two items of fibonacci
seqience.
Then the number value is equal 3 and the cyce is repeated.

The idea is, when the funcition is called, the spece in the memory is seta for
the function - stac frames.
When more than one function is called, the next stack is prepared and the
previous stays opened, waiting till the active stack is resolved.

In this case, the functions are nested over and over. For number = 5, the number 3
for b variable is called, within it the number 2 and 1 for varaible a is called.
Value for number = 1 is returned immadietely, but in number = 2 step functions is
nested further, considering n - 2 = 0, within n - 1 = 2, where
outermost item is  n - 1 = 5.
'''
