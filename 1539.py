'''
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

'''

arr = [2,3,4,7,11]
k = 5
Output: 9

arr = [1,2,3,4]
k = 2
Output: 6


def findKthPositive(arr, k) :
    lst2 = []
    for i in range(len(arr)-1):
        differnce = arr[i+1] -arr[i]
        lst2.append(differnce)

    diff = 2

    if diff > 1 in  lst2:
        lst = []
        for i in range(1,arr[-1]+1):
            if i not in arr:
                lst.append(i)        
        m = lst[k-1]
        return m
    
    else:
        new_arr = []
        for num in range(arr[-1]+1,(arr[-1]+len(arr)+1)):
            new_arr.append(num)
        print(new_arr)
        m = new_arr[k-1]
        return m
    
print(findKthPositive(arr, k))