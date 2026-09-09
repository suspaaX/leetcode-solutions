
'''

680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''




s = "abca"
Output: False


s = "bebeb"
Output =  True


# s = "aba"
# Output =  True

# s = "abc"
# Output =  False

# s = "cbbcc"
# Output =  True

def validPalindrome(s) :
    s2 = s[:]
    s2_rev = s[::-1]
    
    if s == s2_rev:
        return True
    
    elif s != s2_rev:
        result = []
        for i in range(len(s)):
            reslt = s[:i] + s[i+1:]
            result.append(reslt)
        
        result3 = []
        for k in result:
            k2 = k[::-1]
            if k[:] == k2:
                result3.append(True)
            else:
                result3.append(False)
            
        if True in result3:
            return True
        else:
            return False

        
print((validPalindrome(s)))