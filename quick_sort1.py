#-*-coding:utf-8-*-
#! /usr/bin/env/ python
'''def quick_sort(arr,left,right):
    if left>=right:
        return

    low=left
    high=right
    mid = arr[low]
    while left < right:
        while left < right and mid<=arr[right]:
            right-=1
        arr[left]=arr[right]

        while left < right and arr[left] <=mid:
            left+=1
        arr[right]=arr[left]

    arr[right]=mid

    quick_sort(arr,low,right-1)
    quick_sort(arr,right+1, high)



if __name__ == '__main__':
    l=[2,1,34,5,7,8,9,5,6,55]
    quick_sort(l,0,len(l)-1)
    print l'''

# def merge(l):
#     if len(l) <=1:
#         return l
#     mid=len(l)//2
#     left=merge(l[:mid])
#     right=merge(l[mid:])
#     return merge_sort(left,right)
# def merge_sort(left,right):
#     res=[]
#     i=j=0
#     while i< len(left) and j<len(right):
#         if left[i]<=right[j]:
#             res.append(left[i])
#             i+=1
#         else:
#             res.append(right[j])
#             j+=1
#
#     if i==len(left):
#         res.extend(right[j:])
#     else:
#         res.extend(left[i:])
#     return res
# if __name__=='__main__':
#     l=[2,1,34,5,7,8,9,5,6,55]
#     res=merge(l)
#     for i in res:
#         print i,



