#-*-coding:utf-8-*- 
class Person:
    def __init__(self):
        self.__age = 12
        self._sex = 'girl'


    def _sexx(self): # 通配符导入时，不导入此函数
        print '男'
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

if __name__ == '__main__':
    p=Person()
    print p._sex
    p._sexx()
    # print p.__age 私有变量只有类对象自己能放问，子类对象都不可以访问
    print p.get_age()
    print p._Person__age#也可以访问私有变量，但最好不
