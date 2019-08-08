#-*-coding:utf-8-*- 
# author :  王顺章
# school :  nuaa
# contact : wangshunzhang@nuaa.edu.cn
# description
def reorganizeString(self, S):
    """
    :type S: str
    :rtype: str
    """
    from collections import Counter
    c = collections.Counter(S)
    if max(c.values()) <= (len(S) + 1) / 2:
        res = ""
        while c:
            out = c.most_common(2)
            if len(out):
                res += out[0][0]
                c[out[0][0]] -= 1
            if len(out) > 1:
                res += out[1][0]
                c[out[1][0]] -= 1
            c += collections.Counter()  # 每次需要重新进行排序
        return res
    return ""