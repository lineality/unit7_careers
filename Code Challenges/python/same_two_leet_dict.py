# issue: two same number
# 2020.04.28-29
# https://leetcode.com/problems/two-sum/

# assigned instructions:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# (user)Problem:
# you have one list of numbers
# but you do not know, you need to know,
# the indices of which two different number entries (maybe same value)
# sum to the target (a + b = target)
# without using the same index twice (same value is ok)

# Solution(product):
# the tricky part is to compare indices not values (to not self-compare)
# but the good news is you only need to find one match
# (where: (target - number_in_list) is also in list)
# for each item in list, look for that: target-number in list?
# exit after first success
# return indices of those two numbers
# alternative solution my be a table storing the target-value values or indices


class Solution:
    def twoSum(self, nums, target):

        answer_list = [None, None]

        # Make 2 dictionaries, for looking up values and indices
        index_dict = {}
        values_dict = {}
        for i in range(len(nums)):
            index_dict[i] = nums[i]
        for i in range(len(nums)):
            values_dict[nums[i]] = i

        # look for: (target-number) in list
        # save and return those indices
        for i in range(len(nums)):
            #   if matches target         and          not compared to self-index
            if (target - nums[i]) in nums and values_dict[target - index_dict[i]] != i:
                answer_list[0] = i
                answer_list[1] = values_dict[target - nums[i]]
                break

        return answer_list


# testing
ss = Solution()
print(ss.twoSum([2, 7, 11, 15], 9))
print(ss.twoSum([3, 2, 4], 6))
print(ss.twoSum([3, 3], 6))
