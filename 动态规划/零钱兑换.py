#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description  动态规划  f(11) = min(f(10), f(9), f(6)) + 1
#零钱兑换1
def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    '''动态规划'''
    res = [0 for _ in range(amount + 1)]
    if amount == 0:
        return 0
    if min(coins) > amount:
        return -1

    for i in range(1, amount + 1):
        cost = float('inf')
        for c in coins:
            if i >= c:
                cost = min(cost, res[i - c] + 1)
        res[i] = cost
    if res[-1] == float('inf'):
        return -1
    else:
        return res[-1]
# 零钱兑换2
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0 and coins == []:
            return 1
        res = [0 for _ in range(amount + 1)]
        res[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                res[i] += res[i - coin]
        return res[amount]