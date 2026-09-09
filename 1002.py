'''
1002. Find Common Characters
Easy
Topics
premium lock icon
Companies
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]


'''
words = ["cool","lock","cook"]
Output = ["c","o"]


def commonChars(words):
    lst = []
    for i in words[0]:
        for k in words:
            if i in k:
                lst.append(i)
    print(lst)


(commonChars(words))