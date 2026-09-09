'''
645. Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
'''

nums = [1,2,2,4]
Output =  [2,3]

nums = [1,1]
Output = [1,2]

# nums = [2,2]
# Output = [1,2]


# nums = [1,3,3]
# Output = [3,2]


def findErrorNums(nums):
    dict1 = {}
    for i in nums:
        if i in dict1:
            dict1[i] = dict1[i]+1
        else:
            dict1[i] =1

    rslt = []
    for key,val in dict1.items():
        if val==2:
            rslt.append(key)
            if 1 not in nums:
                rslt.append(1)
            elif 1 in nums and key-1 not in nums:
                rslt.append(key-1)
            else:
                rslt.append(key+1)

    return rslt
        
print(findErrorNums(nums))