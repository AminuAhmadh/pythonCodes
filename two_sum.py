""" --- SOME SOLUTIONS TO LEETCODE/HACKER RANK PROBLEMS I FOUND INTERESTING ---

PROBLEM: Given an array of integers nums, and an integer target, return the indices
of the two numbers such that they add up to target. 

SOLUTION: A function that takes an array and a target and return indices that will add up to target
"""


def array(nums: list, target: int):
    for i in range(len(nums)-1):
        elem1 = nums[i]
        for n in nums:
            if elem1 + n == target:
                val1 = elem1
                val2 = n
                output = [nums.index(val1), nums.index(val2)]
                print(output)
                quit()
           


array([2, 7, 11, 3, 15], 17) # will return the indices [0, 4]