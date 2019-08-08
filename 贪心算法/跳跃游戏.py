#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description   总是记录当前能达到的最远位置，若存在一个位置i，前面所有节点能够达到的最远位置小于i，则无法继续走下去，返回False。
def canJump(self,nums):

    x=0
    for i in range(nums):
        if x < i :
            return False
        else:
            x=max(x,i+nums[i])
    return True