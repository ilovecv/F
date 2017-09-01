'''
Problem: Permutaions

Given a collection of numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''



class Solution(object):
    def permute(self, nums):

        def permuteHelper(nums, index, result):
            if index == len(nums):
                result.append(nums)
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permuteHelper(nums[:], index+1, result)
                nums[index], nums[i] = nums[i], nums[index]
            return 


        result = []
        permuteHelper(nums, 0, result)
        return result

    
    
    
'''
Problem 2: Unique Permutations

Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''



from sets import Set
class Solution(object):
    def permuteUnique(self, nums):

        def permuteUniqueHelper(nums, index, path, result):
            if index == len(nums):
                result.append(nums)
                return
            for i in range(index, len(nums)):
                if nums[i] not in path:
                    path.add(nums[i])    # add the current number to the hashset
                    nums[index], nums[i] = nums[i], nums[index]
                    permuteUniqueHelper(nums[:], index+1, Set(), result)
                    nums[index], nums[i] = nums[i], nums[index]
            return


        result = []
        permuteUniqueHelper(nums, 0, Set(), result)
        return result
    

    
    
'''
Problem 3:

A derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

'''
    
    
class Solution(object):
    def findDerangement(self, n):

        dp = [0, 1]
        for x in range(2, n + 1):
            dp.append(x * (dp[- 1] + dp[-2]) % (10**9 + 7))
        return dp[n - 1]
    
    
    
'''
Problem 4: 

A "derangement" of a sequence is a permutation where no element appears in its original position. 
For example ECABD is a derangement of ABCDE, given a string, may contain duplicate char, please out put all the derangement 
public List<char[]> getDerangement(char[]){}. 

'''

def derangement(s):

    def helper(index, ls, path, result):
        if index == len(ls):
            result.append(''.join(ls))
            return
        for i in range(index, len(ls)):
            if ls[i] not in path:
                path.add(ls[i])
                ls[index], ls[i] = ls[i], ls[index]
                if ls[index] != s[index] and ls[i] != s[i]:   # 如果满足条件就继续recusive call，否则就直接换回来
                    helper(index+1, ls[:], set(), result)
                ls[index], ls[i] = ls[i], ls[index]


    result = []
    helper(0,list(s),set(), result)
    return result

