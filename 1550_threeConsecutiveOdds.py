'''
1550. Three Consecutive Odds
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

'''

arr = [1,2,34,3,4,5,7,23,12]
Output = True
# Explanation: [5,7,23] are three consecutive odds.

arr = [2,6,4,1]
Output =  False


def threeConsecutiveOdds(arr) :
    result = []
    for i,j in enumerate(arr):
        if j%2 != 0 :
            result.append(i)
    
    result2 = []
    for k in result:
        x = (arr[k:k+3])
        if len(x) == 3:
            result2.append(x)


    result3 = []
    for idx,elem in enumerate(result2):
        for e in elem :
            if elem[1]%2 != 0 and elem[2]%2 != 0:
                result3.append(True)
            else:
                result3.append(False)
            
    if True in result3:
        return True
    else:
        return False


            

print(threeConsecutiveOdds(arr))