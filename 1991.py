'''
1991. Find the Middle Index in Array

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

 

Example 1:

Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
Example 2:

Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
Example 3:

Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.


'''

nums = [2,3,-1,8,4]
Output = 3

# nums = [2,5]
# Output = -1

# nums = [1,-1,4]
# Output: 2

# nums = [1]
# Output = 0

# nums = [4,0]
# Output = 0

nums = [0,4]
Output = 1

# nums = [1,3,5,9]
# Output = -1

# nums = [0,0,0,0]
# Output = 0

nums = [4,2,1,-3]
Output = 0

def findMiddleIndex(nums):
    if len(nums) == 1:
        return 0    
    
    elif len(nums) == 2 and nums[0] > 0 and nums[1] == 0:
        return 0
    
    elif len(nums) == 2 and nums[0] == 0 and nums[1] > 0:
        return 1
    
    elif len(nums) >= 2 and nums[0] == 0 :
        return 0
    
    elif len(nums) >=2:
        for i in range(1,len(nums)+1):
            lft = nums[0:i]
            rgt = nums[i+1:len(nums)]
            if sum(lft) == sum(rgt) :
                return i

        else:
            return -1






print(findMiddleIndex(nums))

