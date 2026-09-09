'''
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

 
'''


left = 47
right = 127
Output = [48,55,66,77]


left = 1
right = 22
Output = [1,2,3,4,5,6,7,8,9,11,12,15,22]

def selfDividingNumbers(left, right):

    result = []
    for i in range(left,right+1):
        x = str(i)
        if x[-1] != '0':
            result.append(x)

    result4 = []
    for elem in result:
        for idx,el in enumerate(elem):
            k2 = int(elem)
            if k2%int(elem[idx]) == 0:
                result4.append(k2)           
    print(result4)        
    
selfDividingNumbers(left, right)
