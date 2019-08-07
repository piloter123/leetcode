#-*-coding:utf-8-*- 
# authon:王顺章

def foo(a):
    '''断言成功则继续执行代码，断言失败则程序报错'''
    assert a==2,Exception("不等于2")
    print 'ok',a

if __name__ == '__main__':
    foo(2)
    print  foo.__doc__