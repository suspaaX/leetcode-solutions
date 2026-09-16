'''
1394. Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
'''
arr = [1,2,2,3,3,3]
Output = 3

# arr = [2,2,2,3,3]
# Output = -1

# arr = [2,2,3,4]
# Output = 2

def findLucky(arr) :
    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1

    rslt = []   
    for key,val in dict1.items():
        if key == val:
            rslt.append(key)
            rslt.sort()  
        
    if len(rslt)>0:
        return rslt[-1]
    else:
        return -1


print(findLucky(arr))