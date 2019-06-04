# -*- coding:utf-8 -*-

"""
@kn app=leetcode id=134 lang=python
[134] 加油站

"""
class Solution:
    def canCompleteCircuit(self,gas,cost):
        n = len(gas)
        total_tank, curr_tank = 0,0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank  += gas[i] - cost[i]
            if curr_tank < 0:
               starting_station = i + 1
               curr_tank = 0

        return starting_station if total_tank >= 0 else -1




if __name__ == "__main__":
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    eaw = Solution()
    pp  = eaw.canCompleteCircuit(gas,cost)
    print(pp)