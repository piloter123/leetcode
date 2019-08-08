#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description  如果sum（gas[i]-cost[i])小于0,则一定不能转圈，如果gas[i]-cost[i]<0 则应该从i+1开始走。
def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    res = 0
    total_gas = 0
    total = 0
    for i in range(len(gas)):
        sum = gas[i] - cost[i]
        total += sum
        total_gas += sum
        if total_gas < 0:
            res = i + 1
            total_gas = 0
            continue
        else:
            continue
    return res if total >= 0 else -1