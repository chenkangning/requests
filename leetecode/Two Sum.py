# -*- coding:utf-8 -*-
"""
@kn app=leetcode id=1 lang=python

[1] 两数之和

"""
class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，
    请你在该数组中找出和为目标值的那两个整数，
    并返回他们的数组下标。（暴力解法）
    """

    def twiSum(self,nums,target):

        nums_lenght = len(nums)                                           #求出列表总数
        for one_num in range(nums_lenght-1):                              #遍历出列表前三位数字的下标，循环列表三次
            for second_num in range(one_num+1,nums_lenght):               #遍历出列表后三位数字的下标
                if nums[one_num] + nums[second_num] == target:            #相加若等等于目标值
                    return [one_num,second_num]                           #就返回数组下标


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 13
    solution = Solution()
    result = solution.twiSum(nums,target)
    print(result)

#----------------------------------------------------------------------------


# -*- coding:utf-8 -*-

class Solutions(object):
    """
    遍历一遍，得到其数组下标，将数
    值减去数值内的数字，得到的数子
    如果在数组内就返回其下标值。
    """
    def twoSum(self,nums,target):
        """
        :type:nums:List[int]
        :type:target[int]
        :type:List[int]
        """

        answer = []
        for left_index in range(len(nums)):
            right = target - nums[left_index]
            if right in nums[left_index + 1:]:
                nums_right = nums[left_index + 1:]
                right_index = nums_right.index(right)+left_index+1    # 得到在nums里的下标值
                answer.extend([left_index, right_index])              # extend()用于在列表未尾追加另一个序列中的多个值                
                break
        return answer



if __name__ == "__main__":
    nums = [-1,-2,-3,-4,-5]
    target = -3
    answer = Solutions().twoSum(nums,target)
    print(answer)
