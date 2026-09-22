'''


1876. Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

'''
s = "xyzzaz"
Output= 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# s = "aababcabc"
# Output = 4


def countGoodSubstrings(s):

    lst = []
    for i in range(len(s)):
        k = s[i:i+3]
        if len(k) == 3:
            lst.append(k)

    result = []
    for m in lst:
        len3 = set(m)
        if len(len3) == 3:
            result.append(len3)

    return len(result)

print(countGoodSubstrings(s))