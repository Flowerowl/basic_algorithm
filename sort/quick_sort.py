#encoding:utf-8
"""
1.从数列中挑出一个元素，称为 "基准"（pivot），
2.重新排序数列，所有元素比基准值小的摆放在基准前面，
    所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
    在这个分区退出之后，该基准就处于数列的中间位置。
    这个称为分区（partition）操作。
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

time:
    worst: O(n^2)
    best: O(nlogn)
    avg: O(nlogn)
"""
origin_list = [5,3,5,6,8,9,6,5,3,21,45,5,6,5,3]


def quick_sort(lst):
    if len(lst) <= 1:
        print 'current >>>%s' % lst
        return lst
    else:
        print 'current >>>%s' % lst
        pivot = lst[0]
        return quick_sort([x for x in lst[1:] if x <= pivot]) + [pivot] + quick_sort([x for x in lst[1:] if x > pivot])


if __name__ == '__main__':
    print 'origin >>>%s' % origin_list
    result = quick_sort(origin_list)
    print 'last >>>%s' % result

