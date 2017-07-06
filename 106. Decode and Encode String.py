'''
Problem:

Given an encoded string, return it's decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


# Solution 1

class Solution(object):
    
    def decodeString(self, s):

        n = 0
        digit = 0
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                digit = digit*10 + int(s[i])
            elif s[i] == "[":
                stack.append(digit)
                stack.append(s[i])
                digit = 0
            elif s[i] == "]":
                pattern = ""
                while stack[-1] != "[":
                    pattern = stack.pop() + pattern    # note
                stack.pop()    # pop out "["
                n = int(stack.pop())
                stack.append(str(pattern*n))
            else:
                stack.append(s[i])

        return "".join(stack)

    
    
    
# Solution 2:    

class Solution(object):
    def decodeString(self, s):

        n = 0
        digit = 0
        pattern = ''
        stack = []
        for char in s:
            if char.isdigit():
                digit = digit*10 + int(char)
            elif char == "[":
                stack.append(pattern)
                stack.append(digit)
                pattern = ''
                digit = 0
            elif char == "]":
                n = stack.pop()
                prevStr = stack.pop()
                pattern = prevStr+pattern*n
            else:
                pattern += char

        return pattern

    
    
    
'''
Problem:

Given a non-empty string, encode the string such that its encoded length is the shortest.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:
k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.

Example 1:
Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.

Example 2:
Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.

Example 3:
Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".

Example 4:
Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".

Example 5:
Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
'''

class Solution(object):

    def encode(self, s):

        def isEncoded(s):
            if not s: return False
            index = s.find('[')
            if index == -1: return False
            val = s[:index]
            if not val.isdigit(): return False
            if s[-1] != ']': return False
            return True


        length = len(s)
        if length <= 1: return s
        res = [[None]*length for _ in range (length)]
        dp = [[0]*length for _ in range (length)]

        for l in range(length):
            for i in range(length - l):
                if s[i:i+l+1] == s[i] * length: 
                    res[i][i+l] = str(length) + '[' + s[i] + ']'
                    dp[i][i+l] = len(res[i][i+l])
                else:
                    res[i][i+l] = s[i:i+l+1]
                    dp[i][i+l] = l+1

                for j in range(i, i + l):
                    string = res[i][j] + res[j+1][i+l]
                    minLength = dp[i][j] + dp[j+1][i+l]
                    string1 = res[i][j][res[i][j].find('[') + 1 : -2] if isEncoded(res[i][j]) else res[i][j]
                    count1 = int(res[i][j][:res[i][j].find('[')]) if isEncoded(res[i][j]) else 1
                    string2 = res[j + 1][i + l][res[j + 1][i + l].find('[') + 1 : -2] if isEncoded(res[j+1][i+l]) else res[j+1][i+l]
                    count2 = int(res[j + 1][i + l][:res[j + 1][i + l].find('[')]) if isEncoded(res[j+1][i+l]) else 1

                    if string1 == string2:
                        string = str(count1 + count2) + '[' + string1 + ']'
                        minLength = len(string)
                    if minLength < dp[i][i+l]: 
                        res[i][i+l] = string 
                        dp[i][i+l] = minLength
        return res[0][-1]