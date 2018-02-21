#encoding:utf-8
"""
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5

time:
    worst: O(n^2)
    best: O(n)
    avg: O(n^2)
space:
    O(n)
"""
origin_list = [3,5,23,1,54,6,7,4,2,2,5,7,7,8,4,3,1,4,5,63]


def insert_sort(lst):
    if len(lst) <= 1:
        return lst

    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
        print 'current >>>%s' % lst


if __name__ == '__main__':
    print 'origin >>>%s' % origin_list
    insert_sort(origin_list)
