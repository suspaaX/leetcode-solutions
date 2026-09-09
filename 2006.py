'''
2006. Count Number of Pairs With Absolute Difference K

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]
 
'''



# nums = [1,3]
# k = 3
# Output: 0

# nums = [1,2,2,1]
# k = 1
# Output: 4

nums = [3,2,1,5,4]
k = 2
Output: 3

def countKDifference(nums, k):
    pairs = []
    for i in range(len(nums)):
        for j in nums[i+1:len(nums)]:
            x = nums[i],j
            pairs.append(x)
    
    result = []
    for pair in pairs:
        diff = pair[0] - pair[1]
        if diff <0 :
            m = diff*(-1)
            result.append(m)
        else:
            result.append(diff)

    result2 = []
    for m1 in result:
        if m1 == k:
            result2.append(m1)

    return len(result2)

print(countKDifference(nums, k))