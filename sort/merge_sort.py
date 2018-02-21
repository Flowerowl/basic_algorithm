#encoding:utf-8
"""
1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2.设定两个指针，最初位置分别为两个已经排序序列的起始位置
3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4.重复步骤3直到某一指针到达序列尾
5.将另一序列剩下的所有元素直接复制到合并序列尾

time:
    worst:O(nlogn)
    best:O(n)
    avg:O(nlogn)
space:
    O(n)
"""
origin_list = [6,4,8,2,1,0,8,8,4,1,2,0,8,9,11,2,1]


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        print 'current >>>%s' % merged
        return merged

    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    print 'left >>>%s right >>>%s' % (left, right)
    return merge(left, right)


if __name__ == '__main__':
    print 'origin >>>%s' % origin_list
    merge_sort(origin_list)
