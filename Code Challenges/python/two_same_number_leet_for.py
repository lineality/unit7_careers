# issue: two same number
# 2020.04.28-29
# https://leetcode.com/problems/two-sum/

# assigned instructions:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# (user)Problem:
# you have a list of numbers
# but you do not know, you need to know,
# the indices of which two different number entries (maybe same value)
# sum to the target (a + b = target)

# Solution(product):
# the tricky part is to compare indices not values (to not self-compare)
# but the good news is you only need to find one match
# (where number-target is in list)
# return indices
# alternative solution my be a table storing the target-value values or indices


class Solution:
    def twoSum(self, nums, target):

        # answer goes here
        answer_set = set()
        list_of_answer_indices = []

        index_dict = {}
        values_dict = {}

        # make index lookup dict: { list_index : value }
        for i in range(len(nums)):
            index_dict[i] = nums[i]

        # make index lookup dict: { value : list_index }
        for i in range(len(nums)):
            values_dict[nums[i]] = i

        for i in range(len(nums)):
            #   if matches target               and          not compared to self
            if (target - nums[i]) in nums and values_dict[target - index_dict[i]] != i:
                # record answer indices in answer set
                answer_set.add(i)
                answer_set.add(values_dict[target - nums[i]])

        list_of_answer_indices = list(answer_set)  # save only one set

        return list_of_answer_indices


# [3,3]
# ss = Solution()
# ss.twoSum([2, 7, 11, 15],9)
# ss.twoSum([3,2,4],6)
# ss.twoSum([3,3], 6)
