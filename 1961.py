'''
1961. Check If String Is a Prefix of Array

Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.

 

Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.
Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.

'''
s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
Output: True

# s = "iloveleetcode"
# words = ["apples","i","love","leetcode"]
# Output: False

# s = "a"
# words = ["aa","aaaa","banana"]
# Output: False

# s = "a"
# words = ["a","ad","cookie"]
# Output: True

# s = "cccc"
# words = ["cccccccccc"]
# Output: False


def isPrefixString(s,words) :
    if len(words) == 1 and len(s) != len(words):
        return False
    else:
        word = ''
        for i in words:
            word = word+i
        # print(word)
        
        prfx = word[0:len(s)]
        # print(prfx)

        if s == prfx:
            return True
        else:
            return False
   

print(isPrefixString(s,words))