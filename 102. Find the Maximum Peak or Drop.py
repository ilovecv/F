'''
Problem 1:

Given a list of number, there is only one peak or one drop. Find the maximum drop.
Exps:
1 -> 2 -> 3 -> 9 -> 3 -> 0 = 9;
10 -> 4 -> 3 -> 8 = 7 ;
'''



'''
Problem 2:

Given an array will have either a valley or a mountain, only one, not one of each, find out the index of the valley or peak element
And with one more assumption: array[i - 1] = array[i] + 1 or array[i - 1] = array[i] - 1.
Example 1: [1,2,3,4,3,2,1] --> return 3
Example 2: [6,5,4,3,2,3,4] --> return 4
'''

'''
Solution:

使用那个assumption可以达到O(1) 复杂度：首先判断isUp or not，仅以isUp为例, 假设A[x] 是最高点，则有：
A[x] - A[i] = x - i
A[x] - A[j] = j - x

or 

A[x] - A[0] = x - 0
A[x] - A[len(A)-1] = len(A)-1 - x

由此可以解出 x = 1/2 * (A[-1] - A[0] + len(A)-1)，isdown同理可求

'''

def findPeak(nums):
    if not nums: return None

    if len(nums) < 2: return nums[0]

    if nums[1] > nums[0]: 
        return (nums[-1] - nums[0] + len(nums)-1)/2
    else:
        return (nums[0] - nums[-1] + len(nums)-1)/2

