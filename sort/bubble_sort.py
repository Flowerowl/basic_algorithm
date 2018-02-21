#encoding:utf-8
"""
1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。
    这步做完后，最后的元素会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

time:
    worst O(n^2)
    best O(n)
    avg O(n^2)

space:
    O(n)
"""
origin_list = [2,6,2,1,5,8,9,5,2,1,8,0,9,7,5,2,1]


def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print 'current >>>%s' % lst


if __name__ == '__main__':
    print 'origin >>>%s' % origin_list
    bubble_sort(origin_list)
