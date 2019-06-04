# -*- coding：utf-8 -*-
"""
@kn app=leetcode id=167 lang=python

[167] 输入有序数组

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :给定一个已按照升序排列 
        :的有序数组，找到两个数使得它们相加之和等于目标数。
        """
        dict_1={}
        for i in range(len(numbers)):                   #遍历得到下标值
            count=target-numbers[i]                     #将目标值减去列表的值
            if count in dict_1:                         #判断得到的值在不在字典内
                return [dict_1[count],i+1]              #若在就返回
            dict_1[numbers[i]]=i+1                      #若不在就添加到字典内

        


if __name__ == "__main__":
    numbers = [2,5,11,20]
    target = 7

    solution = Solution()
    a = solution.twoSum(numbers,target)
    print(a)