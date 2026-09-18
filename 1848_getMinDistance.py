'''
1848. Minimum Distance to the Target Element

Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.

 

Example 1:

Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
Example 2:

Input: nums = [1], target = 1, start = 0
Output: 0
Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
Example 3:

Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.


'''


nums = [1,2,3,4,5]
target = 5
start = 3
Output: 1

# nums = [1,1,1,1,1,1,1,1,1,1]
# target = 1
# start = 0
# Output: 0

# nums = [1]
# target = 1
# start = 0
# Output: 0

# nums = [5,3,6]
# target = 5
# start = 2
# output = 2

# nums = [5,7,7,5]
# target = 5
# start = 2
# output = 1



def getMinDistance(nums, target, start) :
    lst = []
    for i,j in enumerate(nums): 
        if target == j:
            lst.append(i)

    lst2 = []
    for m in lst:
        x = m-start
        lst2.append(abs(x))


    return min(lst2)

print(getMinDistance(nums, target, start))  
